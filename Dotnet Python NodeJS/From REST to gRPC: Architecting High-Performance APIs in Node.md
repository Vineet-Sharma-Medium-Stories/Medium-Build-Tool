# From REST to gRPC: Architecting High-Performance APIs in Node.js

![**A 20-Minute Architectural Deep Dive**](<images/From REST to gRPC: Architecting High-Performance APIs in NodeJS.png>)

The architectural decision between REST and gRPC is rarely just about data formats. It is a fundamental choice that dictates the entire lifecycle of an API—from contract definition and client generation to performance characteristics, streaming capabilities, deployment strategies, and operational observability. This decision ripples through every layer of the application stack, influencing how teams collaborate, how systems scale, and how efficiently resources are utilized in production environments.

This document explores this evolution through a practical use case: a real-time **Fleet Management System**. The journey begins with a traditional REST API, highlighting its operational friction and architectural limitations, and culminates in a high-performance gRPC service built with Node.js modern ecosystem—leveraging **Fastify**, **TypeScript**, **Prisma ORM**, **gRPC with @grpc/grpc-js**, **BullMQ**, **Redis**, and **OpenTelemetry** for observability.

> **Note:** This Node.js-based architectural story parallels the .NET 10 and Python implementations covered in the companion documents. While the underlying principles remain consistent—contract-first design, streaming patterns, and performance optimization—the Node.js ecosystem offers its own unique capabilities through Fastify's high-performance HTTP framework, TypeScript's type safety, Prisma's type-safe database access, and Node.js's event-driven, non-blocking I/O model. The .NET 10 version focused on AI-enhanced Minimal APIs and Native AOT compilation; the Python version emphasized FastAPI and Pydantic; this Node.js version highlights Fastify's performance, Prisma's developer experience, and Node.js's exceptional handling of concurrent connections.

---

## The Scenario: Fleet Management System

Modern logistics and transportation companies face increasing demands for real-time visibility, operational efficiency, and seamless communication between drivers, dispatchers, and management systems. A typical fleet management platform must handle thousands of vehicles simultaneously, each generating continuous streams of telemetry data while receiving time-sensitive commands from central operations.

Consider a system with two primary consumers, each with distinct communication patterns and performance requirements:

1.  **A Mobile Driver App (React Native):** Deployed on iOS and Android devices across a distributed fleet of vehicles. This application requires sending location updates (telemetry) every 2 seconds, including GPS coordinates, speed, heading, engine diagnostics, and driver status. The app operates in varying network conditions—from 5G in urban areas to intermittent connectivity in rural regions—demanding efficient data transmission and resilient communication patterns. Each vehicle generates approximately 43,200 telemetry updates per 12-hour shift, creating significant data ingress requirements.

2.  **A Web Dashboard (React):** Accessed by dispatchers, fleet managers, and operations personnel through modern web browsers. This interface displays a live map of all vehicles with real-time position updates, shows vehicle status indicators, allows command dispatch (e.g., "re-route," "maintenance alert," "emergency stop"), and provides historical trip data. The dashboard requires near-instantaneous updates to provide accurate situational awareness, with any latency beyond 2-3 seconds creating operational blind spots.

The core backend service, **Telemetry & Dispatch**, is responsible for ingesting high-volume location data from the mobile fleet, maintaining real-time vehicle state, broadcasting commands to specific vehicles or groups, and serving aggregated data to the dashboard and other downstream systems. This service must handle hundreds of concurrent connections, maintain low-latency data processing, and ensure reliable command delivery even under failure conditions.

---

## The REST Approach: A Foundation of Friction

### Initial API Design with Fastify

Initially, a REST API is designed using **Fastify**—Node.js's high-performance web framework. Fastify provides built-in schema validation through JSON Schema, automatic OpenAPI documentation via @fastify/swagger, and exceptional performance with low overhead. The endpoints are clean, intuitive, and adhere to HTTP semantics.

#### REST Endpoint Structure

- **`POST /api/v1/vehicles/:vehicleId/telemetry`** : The mobile app sends a JSON payload for each location update. Fastify validates the request against JSON Schema automatically.
- **`GET /api/v1/vehicles`** : The web dashboard polls this endpoint every 3 seconds to fetch the current status and location of all active vehicles.
- **`POST /api/v1/vehicles/:vehicleId/commands`** : Dispatchers use this endpoint to send operational commands to specific vehicles.
- **`GET /api/v1/vehicles/:vehicleId/commands/pending`** : The mobile app polls this endpoint every 10 seconds to check for new commands.

The API contract is automatically generated as OpenAPI (Swagger) documentation by Fastify Swagger, providing interactive API exploration.

#### REST API Implementation with Fastify and TypeScript

```typescript
/**
 * Fastify REST Implementation for Fleet Management System
 * Node.js 20+ with TypeScript, Fastify, Prisma, and BullMQ
 */

import Fastify from 'fastify';
import fastifySwagger from '@fastify/swagger';
import fastifySwaggerUi from '@fastify/swagger-ui';
import fastifyCors from '@fastify/cors';
import fastifyRateLimit from '@fastify/rate-limit';
import { Type, type Static } from '@sinclair/typebox';
import { PrismaClient } from '@prisma/client';
import Redis from 'ioredis';
import { Queue, Worker } from 'bullmq';
import { randomUUID } from 'crypto';
import pino from 'pino';

// =========================================================================
// TypeBox Schemas for Request/Response Validation
// =========================================================================
// TypeBox provides runtime validation with TypeScript inference

const TelemetryUpdateSchema = Type.Object({
  latitude: Type.Number({ minimum: -90, maximum: 90 }),
  longitude: Type.Number({ minimum: -180, maximum: 180 }),
  speed_kph: Type.Number({ minimum: 0, maximum: 300, default: 0 }),
  heading: Type.Number({ minimum: 0, maximum: 360, default: 0 }),
  engine_status: Type.Optional(Type.Union([
    Type.Literal('running'),
    Type.Literal('idle'),
    Type.Literal('off')
  ])),
  battery_level: Type.Optional(Type.Number({ minimum: 0, maximum: 100 })),
  timestamp: Type.Optional(Type.String({ format: 'date-time' }))
});

type TelemetryUpdateRequest = Static<typeof TelemetryUpdateSchema>;

const TelemetryAcceptanceResponseSchema = Type.Object({
  tracking_id: Type.String(),
  message: Type.String(),
  estimated_processing_time_ms: Type.Number(),
  status_url: Type.String()
});

const VehicleStatusResponseSchema = Type.Object({
  vehicle_id: Type.String(),
  latitude: Type.Number(),
  longitude: Type.Number(),
  speed_kph: Type.Number(),
  heading: Type.Number(),
  status: Type.String(),
  is_online: Type.Boolean(),
  last_update_at: Type.String({ format: 'date-time' }),
  pending_commands: Type.Array(Type.Any())
});

const DispatchCommandRequestSchema = Type.Object({
  command_type: Type.Union([
    Type.Literal('REROUTE'),
    Type.Literal('MAINTENANCE'),
    Type.Literal('EMERGENCY'),
    Type.Literal('LOCATION_REQUEST')
  ]),
  payload: Type.Object({}, { additionalProperties: true }),
  priority: Type.Union([
    Type.Literal('LOW'),
    Type.Literal('NORMAL'),
    Type.Literal('HIGH'),
    Type.Literal('CRITICAL')
  ], { default: 'NORMAL' })
});

type DispatchCommandRequest = Static<typeof DispatchCommandRequestSchema>;

// =========================================================================
// Fastify Application Setup
// =========================================================================

const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  transport: {
    target: 'pino-pretty',
    options: { colorize: true, translateTime: true }
  }
});

const app = Fastify({
  logger,
  trustProxy: true,
  requestIdHeader: 'x-request-id',
  requestIdLogLabel: 'requestId'
});

// Register plugins
await app.register(fastifyCors, {
  origin: true,
  credentials: true
});

await app.register(fastifyRateLimit, {
  max: 100,
  timeWindow: '1 minute',
  keyGenerator: (req) => req.ip
});

await app.register(fastifySwagger, {
  openapi: {
    info: {
      title: 'Fleet Management REST API',
      description: 'REST API for vehicle telemetry and command dispatch',
      version: '1.0.0'
    },
    servers: [{ url: 'http://localhost:3000', description: 'Development Server' }],
    components: {
      securitySchemes: {
        bearerAuth: { type: 'http', scheme: 'bearer' }
      }
    }
  },
  hideUntagged: false
});

await app.register(fastifySwaggerUi, {
  routePrefix: '/docs',
  uiConfig: { docExpansion: 'full', deepLinking: false }
});

// =========================================================================
// Database and Redis Clients
// =========================================================================

const prisma = new PrismaClient({
  log: process.env.NODE_ENV === 'development' ? ['query', 'info', 'warn'] : ['error']
});

const redis = new Redis({
  host: process.env.REDIS_HOST || 'localhost',
  port: parseInt(process.env.REDIS_PORT || '6379'),
  maxRetriesPerRequest: null,
  enableReadyCheck: false
});

// BullMQ Queue for background processing
const telemetryQueue = new Queue('telemetry-processing', {
  connection: redis,
  defaultJobOptions: {
    attempts: 3,
    backoff: { type: 'exponential', delay: 1000 },
    removeOnComplete: 100,
    removeOnFail: 1000
  }
});

// =========================================================================
// REST Endpoints
// =========================================================================

app.post<{
  Params: { vehicleId: string };
  Body: TelemetryUpdateRequest;
}>('/api/v1/vehicles/:vehicleId/telemetry', {
  schema: {
    params: Type.Object({ vehicleId: Type.String() }),
    body: TelemetryUpdateSchema,
    response: {
      202: TelemetryAcceptanceResponseSchema,
      404: Type.Object({ error: Type.String() })
    }
  }
}, async (request, reply) => {
  const { vehicleId } = request.params;
  const telemetry = request.body;
  const trackingId = randomUUID();
  
  request.log.info(
    { vehicleId, latitude: telemetry.latitude, longitude: telemetry.longitude, trackingId },
    'REST: Received telemetry update'
  );

  // Check if vehicle exists
  const vehicle = await prisma.vehicle.findUnique({
    where: { id: vehicleId },
    select: { id: true }
  });

  if (!vehicle) {
    return reply.status(404).send({ error: `Vehicle ${vehicleId} not found` });
  }

  // Add to BullMQ queue for async processing
  await telemetryQueue.add('process-telemetry', {
    vehicleId,
    telemetry: {
      ...telemetry,
      timestamp: telemetry.timestamp ? new Date(telemetry.timestamp) : new Date()
    },
    trackingId
  });

  // Update Redis cache with latest position (for real-time subscribers)
  await redis.hset(`vehicle:${vehicleId}`, {
    latitude: telemetry.latitude,
    longitude: telemetry.longitude,
    speed_kph: telemetry.speed_kph,
    heading: telemetry.heading,
    last_update: new Date().toISOString()
  });
  await redis.expire(`vehicle:${vehicleId}`, 5); // TTL 5 seconds

  // Publish to Redis pub/sub for real-time dashboard updates
  await redis.publish(
    'vehicle:updates',
    JSON.stringify({
      vehicleId,
      latitude: telemetry.latitude,
      longitude: telemetry.longitude,
      speed_kph: telemetry.speed_kph,
      timestamp: new Date().toISOString()
    })
  );

  return reply.status(202).send({
    tracking_id: trackingId,
    message: 'Telemetry update accepted for processing',
    estimated_processing_time_ms: 50,
    status_url: `/api/v1/telemetry/status/${trackingId}`
  });
});

app.get<{
  Querystring: {
    fleetId?: string;
    status?: string;
    page?: number;
    pageSize?: number;
  };
}>('/api/v1/vehicles', {
  schema: {
    querystring: Type.Object({
      fleetId: Type.Optional(Type.String()),
      status: Type.Optional(Type.String()),
      page: Type.Optional(Type.Number({ minimum: 1, default: 1 })),
      pageSize: Type.Optional(Type.Number({ minimum: 1, maximum: 200, default: 50 }))
    }),
    response: {
      200: Type.Array(VehicleStatusResponseSchema)
    }
  }
}, async (request, reply) => {
  const { fleetId, status, page = 1, pageSize = 50 } = request.query;
  const cacheKey = `vehicles:fleet:${fleetId || 'all'}:status:${status || 'all'}`;
  
  // Try Redis cache first
  const cached = await redis.get(cacheKey);
  if (cached) {
    request.log.debug('REST: Cache hit for vehicles query');
    return reply.status(200).send(JSON.parse(cached));
  }

  // Query database with Prisma
  const vehicles = await prisma.vehicle.findMany({
    where: {
      ...(fleetId && { fleetId }),
      ...(status && { status }),
      isActive: true
    },
    skip: (page - 1) * pageSize,
    take: pageSize,
    include: {
      pendingCommands: {
        where: { status: 'PENDING' },
        take: 5,
        orderBy: { priority: 'desc' }
      }
    }
  });

  const responses = vehicles.map(vehicle => ({
    vehicle_id: vehicle.id,
    latitude: vehicle.currentLatitude,
    longitude: vehicle.currentLongitude,
    speed_kph: vehicle.currentSpeed,
    heading: vehicle.currentHeading,
    status: vehicle.status,
    is_online: Date.now() - vehicle.lastTelemetry.getTime() < 5 * 60 * 1000,
    last_update_at: vehicle.lastTelemetry.toISOString(),
    pending_commands: vehicle.pendingCommands.map(cmd => ({
      command_id: cmd.id,
      command_type: cmd.commandType,
      dispatched_at: cmd.dispatchedAt.toISOString()
    }))
  }));

  // Cache for 2 seconds
  await redis.setex(cacheKey, 2, JSON.stringify(responses));
  
  return reply.status(200).send(responses);
});

app.post<{
  Params: { vehicleId: string };
  Body: DispatchCommandRequest;
}>('/api/v1/vehicles/:vehicleId/commands', {
  schema: {
    params: Type.Object({ vehicleId: Type.String() }),
    body: DispatchCommandRequestSchema,
    response: {
      201: Type.Object({
        command_id: Type.String(),
        status: Type.String(),
        estimated_delivery_time: Type.Optional(Type.String({ format: 'date-time' })),
        message: Type.String()
      })
    }
  }
}, async (request, reply) => {
  const { vehicleId } = request.params;
  const { command_type, payload, priority } = request.body;
  const commandId = randomUUID();

  request.log.info(
    { vehicleId, commandType: command_type, commandId },
    'REST: Dispatching command'
  );

  // Create command in database
  const command = await prisma.command.create({
    data: {
      id: commandId,
      vehicleId,
      commandType: command_type,
      payload: JSON.parse(JSON.stringify(payload)),
      priority,
      status: 'PENDING',
      dispatchedAt: new Date(),
      dispatchedBy: request.headers['x-user-id'] as string || 'system'
    }
  });

  // Publish to Redis stream for immediate delivery to gRPC subscribers
  await redis.publish(
    `vehicle:${vehicleId}:commands`,
    JSON.stringify({
      commandId: command.id,
      commandType: command.commandType,
      payload: command.payload,
      priority: command.priority,
      dispatchedAt: command.dispatchedAt
    })
  );

  return reply.status(201).send({
    command_id: command.id,
    status: command.status,
    estimated_delivery_time: new Date(Date.now() + 1000).toISOString(),
    message: `Command ${command_type} queued for delivery`
  });
});

app.get<{
  Params: { vehicleId: string };
}>('/api/v1/vehicles/:vehicleId/commands/pending', {
  schema: {
    params: Type.Object({ vehicleId: Type.String() }),
    response: {
      200: Type.Array(Type.Object({
        command_id: Type.String(),
        command_type: Type.String(),
        payload: Type.Any(),
        priority: Type.String(),
        dispatched_at: Type.String({ format: 'date-time' })
      }))
    }
  }
}, async (request, reply) => {
  const { vehicleId } = request.params;

  // Get pending commands from database
  const commands = await prisma.command.findMany({
    where: {
      vehicleId,
      status: 'PENDING'
    },
    orderBy: [
      { priority: 'desc' },
      { dispatchedAt: 'asc' }
    ],
    take: 10
  });

  return reply.status(200).send(commands.map(cmd => ({
    command_id: cmd.id,
    command_type: cmd.commandType,
    payload: cmd.payload,
    priority: cmd.priority,
    dispatched_at: cmd.dispatchedAt.toISOString()
  })));
});

// Background worker for telemetry processing
const telemetryWorker = new Worker('telemetry-processing', async (job) => {
  const { vehicleId, telemetry, trackingId } = job.data;
  
  try {
    // Store telemetry in database
    await prisma.telemetry.create({
      data: {
        id: trackingId,
        vehicleId,
        latitude: telemetry.latitude,
        longitude: telemetry.longitude,
        speedKph: telemetry.speed_kph,
        heading: telemetry.heading,
        timestamp: new Date(telemetry.timestamp)
      }
    });

    // Update vehicle current state
    await prisma.vehicle.update({
      where: { id: vehicleId },
      data: {
        currentLatitude: telemetry.latitude,
        currentLongitude: telemetry.longitude,
        currentSpeed: telemetry.speed_kph,
        currentHeading: telemetry.heading,
        lastTelemetry: new Date(telemetry.timestamp)
      }
    });

    request.log.info({ vehicleId, trackingId }, 'Telemetry processed successfully');
  } catch (error) {
    request.log.error({ error, vehicleId, trackingId }, 'Failed to process telemetry');
    throw error;
  }
}, { connection: redis });

// Start server
const start = async () => {
  try {
    await app.listen({ port: 3000, host: '0.0.0.0' });
    app.log.info('REST API server listening on http://localhost:3000');
    app.log.info('Swagger UI available at http://localhost:3000/docs');
  } catch (err) {
    app.log.error(err);
    process.exit(1);
  }
};

start();
```

#### The Operational Friction

While this Fastify REST implementation is functional and benefits from Fastify's excellent performance, several critical issues emerge as the system scales:

1.  **Chatty Communication & Protocol Overhead:** Each telemetry update requires a full HTTP request/response cycle with JSON serialization. JSON parsing overhead becomes significant at scale despite Node.js's efficient V8 engine.

2.  **Polling Inefficiency:** The dashboard polls every 3 seconds, with Fastify executing database queries and serialization for each request, most of which return unchanged data.

3.  **Schema Coordination:** Even with TypeBox providing runtime validation and TypeScript types, the schema must be manually synchronized between Node.js backend, React Native mobile app, and React dashboard.

4.  **No Native Real-Time Communication:** Command delivery relies on polling, introducing 0-30 second latency. HTTP/1.1 and HTTP/2 do not provide native bidirectional streaming for web clients without WebSockets.

5.  **Connection Overhead:** Each HTTP request consumes Node.js event loop resources, limiting concurrent connection capacity despite Node.js's non-blocking I/O.

### REST Architecture Flow Diagram

```mermaid
sequenceDiagram
    participant DriverApp as Mobile App (REST Client)
    participant API as Fastify REST<br/>Node.js
    participant Redis as Redis Cache
    participant DB as PostgreSQL<br/>Prisma ORM
    participant Dashboard as Web Dashboard
    participant Queue as BullMQ Queue

    Note over DriverApp,API: High Overhead per Request
    
    loop Every 2 seconds
        DriverApp->>API: POST /vehicles/123/telemetry (JSON)
        Note right of API: 500-700 bytes overhead<br/>JSON Schema validation
        API->>API: Validate with TypeBox
        API->>Redis: Check vehicle exists
        API->>Queue: Add to BullMQ (async)
        API->>Redis: Publish to pub/sub
        API-->>DriverApp: 202 Accepted (with tracking)
        Note left of DriverApp: ACK received, next request in 2s
    end

    Note over Dashboard,API: Inefficient Polling Pattern
    
    loop Every 3 seconds
        Dashboard->>API: GET /vehicles (JSON)
        API->>Redis: Check cache
        alt Cache Miss
            API->>DB: Prisma query all vehicles
            API->>Redis: Store cache (2s TTL)
        end
        API-->>Dashboard: 200 OK (JSON payload)
        Dashboard->>Dashboard: Re-render map
        Note over Dashboard: 99% of responses unchanged
    end

    Note over Dashboard,DriverApp: Latent Command Delivery
    
    Dashboard->>API: POST /vehicles/123/commands (JSON)
    API->>DB: Prisma create command
    API->>Redis: Publish to Redis stream
    API-->>Dashboard: 201 Created
    
    loop Every 10 seconds
        DriverApp->>API: GET /vehicles/123/commands/pending
        API->>DB: Prisma query pending commands
        alt Command exists
            API-->>DriverApp: 200 OK (Command data)
            DriverApp->>DriverApp: Execute command
        else No commands
            API-->>DriverApp: 200 OK (Empty array)
        end
    end
    
    Note over DriverApp,API: Command delivery latency: 0-10 seconds
```

---

## The gRPC Solution: A Contract-First, Streamlined Architecture

### Rethinking the Communication Paradigm

To address the limitations of REST, the team refactors the Telemetry & Dispatch service to use **gRPC** with Node.js's `@grpc/grpc-js` library. This shift moves the architecture to a contract-first model where Protocol Buffers define the API contract.

gRPC leverages HTTP/2 as its transport protocol, bringing several critical advantages:
- **Multiplexing:** Multiple concurrent requests and responses can be sent over a single TCP connection without head-of-line blocking.
- **Binary Framing:** All data is transmitted in a compact binary format, reducing overhead.
- **Bidirectional Streaming:** Both client and server can initiate streams of messages simultaneously.
- **Header Compression:** HTTP/2 header compression (HPACK) significantly reduces header overhead.

Combined with Protocol Buffers (Protobuf) as the interface definition language and serialization format, gRPC provides a comprehensive solution for high-performance service communication.

### Step 1: Defining the Contract with Protocol Buffers

The source of truth becomes a `.proto` file. This file defines the service methods, message structures, and data types in a language-agnostic format. From this single file, Node.js code is generated using `@grpc/proto-loader`, providing strongly-typed client and server stubs.

**`telemetry.proto`** - Complete Service Definition

```protobuf
syntax = "proto3";

package fleetmanagement.telemetry.v1;

option csharp_namespace = "FleetManagement.Grpc.Protos.V1";
option java_package = "com.fleetmanagement.grpc";
option go_package = "fleetmanagement/grpc/telemetry";
option py_package = "fleetmanagement.grpc.protos";

import "google/protobuf/timestamp.proto";
import "google/protobuf/empty.proto";

// Service definition: Complete telemetry and command API
service TelemetryService {
    // Client-side streaming for efficient telemetry ingestion
    rpc SendTelemetryStream (stream TelemetryUpdate) returns (TelemetryAck);
    
    // Server-side streaming for real-time dashboard updates
    rpc SubscribeToVehicleUpdates (SubscribeRequest) returns (stream VehicleStatusUpdate);
    
    // Bidirectional streaming for advanced command/response
    rpc BidirectionalCommandChannel (stream CommandEnvelope) returns (stream CommandResponseEnvelope);
    
    // Unary call for simple command dispatch
    rpc DispatchCommand (CommandRequest) returns (CommandResponse);
    
    // Unary call for vehicle history
    rpc GetVehicleHistory (HistoryRequest) returns (HistoryResponse);
    
    // Health check
    rpc HealthCheck (google.protobuf.Empty) returns (HealthStatus);
}

// Telemetry update from vehicle
message TelemetryUpdate {
    string vehicle_id = 1;
    double latitude = 2;
    double longitude = 3;
    double speed_kph = 4;
    double heading_degrees = 5;
    double acceleration_ms2 = 6;
    EngineStatus engine_status = 7;
    google.protobuf.Timestamp captured_at = 8;
    map<string, string> metadata = 9;
}

message EngineStatus {
    bool is_running = 1;
    int32 rpm = 2;
    double engine_temperature_celsius = 3;
    double fuel_level_percent = 4;
}

message TelemetryAck {
    int32 updates_received = 1;
    int32 updates_failed = 2;
    google.protobuf.Timestamp last_processed_at = 3;
    string session_id = 4;
    repeated PendingCommand pending_commands = 5;
}

message SubscribeRequest {
    string fleet_id = 1;
    repeated string vehicle_ids = 2;
    int32 preferred_interval_ms = 3;
    string client_id = 4;
}

message VehicleStatusUpdate {
    string vehicle_id = 1;
    double latitude = 2;
    double longitude = 3;
    double speed_kph = 4;
    double heading_degrees = 5;
    VehicleOperationalStatus status = 6;
    bool is_online = 7;
    google.protobuf.Timestamp last_update_at = 8;
    repeated PendingCommand pending_commands = 9;
}

enum VehicleOperationalStatus {
    VEHICLE_STATUS_UNSPECIFIED = 0;
    VEHICLE_STATUS_ACTIVE = 1;
    VEHICLE_STATUS_IDLE = 2;
    VEHICLE_STATUS_OFFLINE = 3;
    VEHICLE_STATUS_MAINTENANCE = 4;
    VEHICLE_STATUS_EMERGENCY = 5;
}

message PendingCommand {
    string command_id = 1;
    string command_type = 2;
    string payload_json = 3;
    string priority = 4;
    google.protobuf.Timestamp dispatched_at = 5;
}

message CommandRequest {
    string vehicle_id = 1;
    string command_type = 2;
    oneof payload {
        RouteCommand route = 3;
        MaintenanceCommand maintenance = 4;
        AlertCommand alert = 5;
        ControlCommand control = 6;
        string raw_json = 7;
    }
    string priority = 8;
    google.protobuf.Timestamp expires_at = 9;
    string dispatched_by = 10;
}

message RouteCommand {
    repeated Waypoint waypoints = 1;
    string route_id = 2;
    int32 estimated_distance_km = 3;
}

message Waypoint {
    double latitude = 1;
    double longitude = 2;
    string address = 3;
    google.protobuf.Timestamp estimated_arrival = 4;
}

message MaintenanceCommand {
    string maintenance_type = 1;
    string service_center_id = 2;
    google.protobuf.Timestamp scheduled_at = 3;
}

message AlertCommand {
    string severity = 1;
    string title = 2;
    string message = 3;
}

message ControlCommand {
    string action = 1;
    map<string, string> parameters = 2;
}

message CommandResponse {
    string command_id = 1;
    bool success = 2;
    string message = 3;
    google.protobuf.Timestamp estimated_delivery_at = 4;
    string status = 5;
}

message CommandEnvelope {
    oneof message_type {
        CommandRequest command = 1;
        CommandAck ack = 2;
        TelemetryUpdate telemetry = 3;
        KeepAlive keep_alive = 4;
    }
}

message CommandResponseEnvelope {
    oneof message_type {
        CommandResponse command_response = 1;
        TelemetryAck telemetry_ack = 2;
        ServerKeepAlive keep_alive = 3;
    }
}

message CommandAck {
    string command_id = 1;
    string status = 2;
    string message = 3;
    google.protobuf.Timestamp acknowledged_at = 4;
}

message KeepAlive {
    int64 sequence_number = 1;
    google.protobuf.Timestamp sent_at = 2;
}

message ServerKeepAlive {
    int64 last_sequence_received = 1;
    google.protobuf.Timestamp server_time = 2;
}

message HistoryRequest {
    string vehicle_id = 1;
    google.protobuf.Timestamp start_time = 2;
    google.protobuf.Timestamp end_time = 3;
    int32 limit = 4;
    string cursor = 5;
}

message HistoryResponse {
    repeated TelemetryUpdate telemetry_history = 1;
    string next_cursor = 2;
    bool has_more = 3;
}

message HealthStatus {
    string service_name = 1;
    string status = 2;
    google.protobuf.Timestamp checked_at = 3;
    map<string, ComponentStatus> components = 4;
    string version = 5;
}

message ComponentStatus {
    string name = 1;
    string status = 2;
    string message = 3;
    int64 latency_ms = 4;
}
```

### Step 2: Loading Protocol Buffers in Node.js

```typescript
/**
 * gRPC Service Implementation for Fleet Management System
 * Node.js 20+ with @grpc/grpc-js, TypeScript, Prisma, and Redis
 */

import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import { PrismaClient } from '@prisma/client';
import Redis from 'ioredis';
import { randomUUID } from 'crypto';
import { EventEmitter } from 'events';

// =========================================================================
// Load Protocol Buffers
// =========================================================================

const PROTO_PATH = './protos/telemetry.proto';

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
  includeDirs: ['./protos']
});

const proto = grpc.loadPackageDefinition(packageDefinition) as any;
const telemetry = proto.fleetmanagement.telemetry.v1;

type TelemetryService = typeof telemetry.TelemetryService;

// =========================================================================
// Vehicle State Manager (In-Memory with EventEmitter)
// =========================================================================

class VehicleStateManager extends EventEmitter {
  private states: Map<string, any> = new Map();
  private subscribers: Map<string, Set<(state: any) => void>> = new Map();

  updateState(vehicleId: string, update: Partial<any>): void {
    const current = this.states.get(vehicleId) || {};
    const newState = {
      ...current,
      ...update,
      lastUpdate: new Date()
    };
    this.states.set(vehicleId, newState);
    
    // Notify subscribers
    const vehicleSubscribers = this.subscribers.get(vehicleId);
    if (vehicleSubscribers) {
      vehicleSubscribers.forEach(callback => callback(newState));
    }
    
    // Emit global update event
    this.emit('update', { vehicleId, state: newState });
  }

  getState(vehicleId: string): any {
    return this.states.get(vehicleId);
  }

  getAllStates(): Map<string, any> {
    return new Map(this.states);
  }

  subscribe(vehicleId: string, callback: (state: any) => void): () => void {
    if (!this.subscribers.has(vehicleId)) {
      this.subscribers.set(vehicleId, new Set());
    }
    this.subscribers.get(vehicleId)!.add(callback);
    
    // Return unsubscribe function
    return () => {
      this.subscribers.get(vehicleId)?.delete(callback);
      if (this.subscribers.get(vehicleId)?.size === 0) {
        this.subscribers.delete(vehicleId);
      }
    };
  }
}

// =========================================================================
// Command Processor with BullMQ
// =========================================================================

class CommandProcessor {
  private pendingCommands: Map<string, any[]> = new Map();
  private prisma: PrismaClient;
  private redis: Redis;

  constructor(prisma: PrismaClient, redis: Redis) {
    this.prisma = prisma;
    this.redis = redis;
  }

  async queueCommand(command: any): Promise<string> {
    const commandId = randomUUID();
    
    // Store in memory
    if (!this.pendingCommands.has(command.vehicleId)) {
      this.pendingCommands.set(command.vehicleId, []);
    }
    this.pendingCommands.get(command.vehicleId)!.push({
      commandId,
      ...command
    });
    
    // Persist to database
    await this.prisma.command.create({
      data: {
        id: commandId,
        vehicleId: command.vehicleId,
        commandType: command.commandType,
        payload: command.payload,
        priority: command.priority,
        status: 'PENDING',
        dispatchedAt: new Date(),
        dispatchedBy: command.dispatchedBy
      }
    });
    
    // Publish to Redis for immediate delivery
    await this.redis.publish(
      `vehicle:${command.vehicleId}:commands`,
      JSON.stringify({ commandId, ...command })
    );
    
    return commandId;
  }

  async getPendingCommands(vehicleId: string, limit: number = 10): Promise<any[]> {
    const commands = this.pendingCommands.get(vehicleId) || [];
    const toDeliver = commands.slice(0, limit);
    this.pendingCommands.set(vehicleId, commands.slice(limit));
    return toDeliver;
  }

  async acknowledgeCommand(commandId: string, status: string, message: string): Promise<void> {
    await this.prisma.command.update({
      where: { id: commandId },
      data: {
        status,
        statusMessage: message,
        acknowledgedAt: new Date()
      }
    });
  }
}
```

### Step 3: Implementing the gRPC Service in Node.js

```typescript
/**
 * Complete gRPC Service Implementation
 * Node.js 20+ with @grpc/grpc-js, TypeScript, and streaming support
 */

import * as grpc from '@grpc/grpc-js';
import { Timestamp } from 'google-protobuf/google/protobuf/timestamp_pb';
import { EventEmitter } from 'events';
import { randomUUID } from 'crypto';

class TelemetryServiceImpl {
  private stateManager: VehicleStateManager;
  private commandProcessor: CommandProcessor;
  private activeStreams: Map<string, grpc.ServerWritableStream<any, any>> = new Map();

  constructor(stateManager: VehicleStateManager, commandProcessor: CommandProcessor) {
    this.stateManager = stateManager;
    this.commandProcessor = commandProcessor;
    
    // Subscribe to state updates for server-side streaming
    this.stateManager.on('update', ({ vehicleId, state }) => {
      this.activeStreams.forEach((stream, clientId) => {
        const update = this.buildVehicleStatusUpdate(vehicleId, state);
        if (update) {
          stream.write(update);
        }
      });
    });
  }

  // ========================================================================
  // 1. Client-Side Streaming: Efficient Telemetry Ingestion
  // ========================================================================

  async sendTelemetryStream(
    call: grpc.ServerDuplexStream<ITelemetryUpdate, ITelemetryAck>
  ): Promise<void> {
    const sessionId = randomUUID();
    let vehicleId: string | null = null;
    let updateCount = 0;
    let failedCount = 0;
    let lastUpdateTime = new Date();
    const pendingCommands: any[] = [];

    console.log(`gRPC: Telemetry stream started - Session: ${sessionId}`);

    call.on('data', async (update: ITelemetryUpdate) => {
      try {
        vehicleId = update.vehicle_id;
        updateCount++;

        // Validate telemetry
        if (update.latitude < -90 || update.latitude > 90) {
          console.warn(`Invalid latitude from ${vehicleId}`);
          failedCount++;
          return;
        }

        // Update in-memory state
        this.stateManager.updateState(vehicleId, {
          latitude: update.latitude,
          longitude: update.longitude,
          speed_kph: update.speed_kph,
          heading_degrees: update.heading_degrees,
          engine_running: update.engine_status?.is_running,
          rpm: update.engine_status?.rpm
        });

        lastUpdateTime = new Date();

        // Check for pending commands
        const commands = await this.commandProcessor.getPendingCommands(vehicleId, 5);
        for (const cmd of commands) {
          pendingCommands.push({
            command_id: cmd.commandId,
            command_type: cmd.commandType,
            payload_json: JSON.stringify(cmd.payload),
            priority: cmd.priority,
            dispatched_at: {
              seconds: Math.floor(cmd.dispatchedAt.getTime() / 1000),
              nanos: (cmd.dispatchedAt.getTime() % 1000) * 1e6
            }
          });
        }

        if (updateCount % 100 === 0) {
          console.debug(`gRPC: Processed ${updateCount} updates for ${vehicleId}`);
        }
      } catch (error) {
        console.error('Error processing telemetry:', error);
        failedCount++;
      }
    });

    call.on('end', async () => {
      console.log(`gRPC: Telemetry stream completed - Vehicle: ${vehicleId}, Updates: ${updateCount}, Failed: ${failedCount}`);
      
      const response: ITelemetryAck = {
        updates_received: updateCount,
        updates_failed: failedCount,
        last_processed_at: {
          seconds: Math.floor(lastUpdateTime.getTime() / 1000),
          nanos: (lastUpdateTime.getTime() % 1000) * 1e6
        },
        session_id: sessionId,
        pending_commands: pendingCommands
      };
      
      call.write(response);
      call.end();
    });

    call.on('error', (error) => {
      console.error(`gRPC: Telemetry stream error - Session: ${sessionId}`, error);
      call.emit('error', error);
    });
  }

  // ========================================================================
  // 2. Server-Side Streaming: Real-time Dashboard Updates
  // ========================================================================

  subscribeToVehicleUpdates(
    call: grpc.ServerWritableStream<ISubscribeRequest, IVehicleStatusUpdate>
  ): void {
    const clientId = call.request.client_id || randomUUID();
    const fleetId = call.request.fleet_id || 'all';
    const updateInterval = call.request.preferred_interval_ms || 1000;
    
    console.log(`gRPC: Dashboard subscription started - Client: ${clientId}, Fleet: ${fleetId}`);
    
    let lastVehicleStates = new Map<string, any>();
    let interval: NodeJS.Timeout;
    
    // Function to send updates
    const sendUpdates = async () => {
      const allStates = this.stateManager.getAllStates();
      const updates: IVehicleStatusUpdate[] = [];
      
      for (const [vehicleId, state] of allStates) {
        const lastState = lastVehicleStates.get(vehicleId);
        
        // Only send if state changed
        if (lastState &&
            lastState.latitude === state.latitude &&
            lastState.longitude === state.longitude) {
          continue;
        }
        
        const pendingCommands = await this.commandProcessor.getPendingCommands(vehicleId, 5);
        
        const update: IVehicleStatusUpdate = {
          vehicle_id: vehicleId,
          latitude: state.latitude || 0,
          longitude: state.longitude || 0,
          speed_kph: state.speed_kph || 0,
          heading_degrees: state.heading_degrees || 0,
          status: state.engine_running ? 1 : 2, // ACTIVE or IDLE
          is_online: state.lastUpdate && 
            (Date.now() - state.lastUpdate.getTime()) < 5 * 60 * 1000,
          last_update_at: {
            seconds: Math.floor((state.lastUpdate || new Date()).getTime() / 1000),
            nanos: ((state.lastUpdate || new Date()).getTime() % 1000) * 1e6
          },
          pending_commands: pendingCommands.map(cmd => ({
            command_id: cmd.commandId,
            command_type: cmd.commandType,
            payload_json: JSON.stringify(cmd.payload),
            priority: cmd.priority,
            dispatched_at: {
              seconds: Math.floor(cmd.dispatchedAt.getTime() / 1000),
              nanos: (cmd.dispatchedAt.getTime() % 1000) * 1e6
            }
          }))
        };
        
        updates.push(update);
        lastVehicleStates.set(vehicleId, state);
      }
      
      // Send all updates
      for (const update of updates) {
        call.write(update);
      }
    };
    
    // Start interval
    interval = setInterval(sendUpdates, updateInterval);
    
    // Handle client disconnect
    call.on('cancelled', () => {
      console.log(`gRPC: Dashboard subscription ended - Client: ${clientId}`);
      clearInterval(interval);
    });
    
    call.on('error', (error) => {
      console.error(`gRPC: Dashboard subscription error - Client: ${clientId}`, error);
      clearInterval(interval);
    });
  }

  // ========================================================================
  // 3. Bidirectional Streaming: Advanced Command/Response Channel
  // ========================================================================

  bidirectionalCommandChannel(
    call: grpc.ServerDuplexStream<ICommandEnvelope, ICommandResponseEnvelope>
  ): void {
    let vehicleId: string | null = null;
    let keepAliveSeq = 0;
    
    console.log(`gRPC: Bidirectional channel opened`);
    
    // Send keep-alive periodically
    const keepAliveInterval = setInterval(() => {
      const response: ICommandResponseEnvelope = {
        keep_alive: {
          last_sequence_received: keepAliveSeq,
          server_time: {
            seconds: Math.floor(Date.now() / 1000),
            nanos: (Date.now() % 1000) * 1e6
          }
        }
      };
      call.write(response);
    }, 30000);
    
    // Handle incoming messages
    call.on('data', async (envelope: ICommandEnvelope) => {
      if (envelope.command) {
        // Handle command from vehicle
        const cmd = envelope.command;
        vehicleId = cmd.vehicle_id;
        console.log(`Received command from vehicle ${vehicleId}: ${cmd.command_type}`);
        
      } else if (envelope.ack) {
        // Handle command acknowledgment
        const ack = envelope.ack;
        await this.commandProcessor.acknowledgeCommand(ack.command_id, ack.status, ack.message);
        console.log(`Command ${ack.command_id} acknowledged: ${ack.status}`);
        
      } else if (envelope.telemetry) {
        // Process telemetry through the channel
        const telemetry = envelope.telemetry;
        this.stateManager.updateState(telemetry.vehicle_id, {
          latitude: telemetry.latitude,
          longitude: telemetry.longitude,
          speed_kph: telemetry.speed_kph
        });
        
      } else if (envelope.keep_alive) {
        // Respond to keep-alive
        keepAliveSeq = envelope.keep_alive.sequence_number;
      }
    });
    
    // Periodically send pending commands
    const sendCommandsInterval = setInterval(async () => {
      if (vehicleId) {
        const pendingCommands = await this.commandProcessor.getPendingCommands(vehicleId, 5);
        for (const cmd of pendingCommands) {
          const response: ICommandResponseEnvelope = {
            command_response: {
              command_id: cmd.commandId,
              success: true,
              message: 'Command delivered via bidirectional channel',
              status: 'DELIVERED'
            }
          };
          call.write(response);
        }
      }
    }, 2000);
    
    call.on('end', () => {
      console.log(`gRPC: Bidirectional channel closed for vehicle ${vehicleId || 'unknown'}`);
      clearInterval(keepAliveInterval);
      clearInterval(sendCommandsInterval);
      call.end();
    });
    
    call.on('error', (error) => {
      console.error('gRPC: Bidirectional channel error:', error);
      clearInterval(keepAliveInterval);
      clearInterval(sendCommandsInterval);
    });
  }

  // ========================================================================
  // 4. Unary Call: Simple Command Dispatch
  // ========================================================================

  async dispatchCommand(
    call: grpc.ServerUnaryCall<ICommandRequest, ICommandResponse>,
    callback: grpc.requestCallback<ICommandResponse>
  ): Promise<void> {
    const request = call.request;
    
    console.log(`gRPC: Dispatching ${request.command_type} command to ${request.vehicle_id} with priority ${request.priority}`);
    
    // Extract payload based on command type
    let payload = {};
    if (request.route) {
      payload = {
        waypoints: request.route.waypoints.map((wp: any) => ({
          lat: wp.latitude,
          lng: wp.longitude,
          address: wp.address
        })),
        route_id: request.route.route_id,
        estimated_distance_km: request.route.estimated_distance_km
      };
    } else if (request.maintenance) {
      payload = {
        maintenance_type: request.maintenance.maintenance_type,
        service_center_id: request.maintenance.service_center_id,
        scheduled_at: request.maintenance.scheduled_at
      };
    } else if (request.alert) {
      payload = {
        severity: request.alert.severity,
        title: request.alert.title,
        message: request.alert.message
      };
    } else if (request.control) {
      payload = {
        action: request.control.action,
        parameters: request.control.parameters
      };
    } else if (request.raw_json) {
      payload = JSON.parse(request.raw_json);
    }
    
    // Queue the command
    const commandData = {
      vehicleId: request.vehicle_id,
      commandType: request.command_type,
      payload,
      priority: request.priority,
      dispatchedBy: request.dispatched_by || 'system'
    };
    
    const commandId = await this.commandProcessor.queueCommand(commandData);
    
    const response: ICommandResponse = {
      command_id: commandId,
      success: true,
      message: `Command ${request.command_type} queued for delivery`,
      status: 'PENDING'
    };
    
    callback(null, response);
  }

  // ========================================================================
  // 5. Unary Call: Vehicle History
  // ========================================================================

  async getVehicleHistory(
    call: grpc.ServerUnaryCall<IHistoryRequest, IHistoryResponse>,
    callback: grpc.requestCallback<IHistoryResponse>
  ): Promise<void> {
    const request = call.request;
    
    console.log(`gRPC: Getting history for vehicle ${request.vehicle_id}`);
    
    // Query database (simplified for example)
    const response: IHistoryResponse = {
      telemetry_history: [],
      has_more: false
    };
    
    callback(null, response);
  }

  // ========================================================================
  // 6. Health Check
  // ========================================================================

  async healthCheck(
    call: grpc.ServerUnaryCall<google.protobuf.Empty, IHealthStatus>,
    callback: grpc.requestCallback<IHealthStatus>
  ): Promise<void> {
    const response: IHealthStatus = {
      service_name: 'FleetManagement.TelemetryService',
      status: 'HEALTHY',
      checked_at: {
        seconds: Math.floor(Date.now() / 1000),
        nanos: (Date.now() % 1000) * 1e6
      },
      version: '1.0.0',
      components: {
        state_manager: {
          name: 'StateManager',
          status: 'HEALTHY',
          latency_ms: 1
        }
      }
    };
    
    callback(null, response);
  }

  // Helper method to build vehicle status update
  private buildVehicleStatusUpdate(vehicleId: string, state: any): IVehicleStatusUpdate | null {
    if (!state) return null;
    
    return {
      vehicle_id: vehicleId,
      latitude: state.latitude || 0,
      longitude: state.longitude || 0,
      speed_kph: state.speed_kph || 0,
      heading_degrees: state.heading_degrees || 0,
      status: state.engine_running ? 1 : 2,
      is_online: state.lastUpdate && (Date.now() - state.lastUpdate.getTime()) < 5 * 60 * 1000,
      last_update_at: {
        seconds: Math.floor((state.lastUpdate || new Date()).getTime() / 1000),
        nanos: ((state.lastUpdate || new Date()).getTime() % 1000) * 1e6
      },
      pending_commands: []
    };
  }
}
```

### Step 4: Starting the gRPC Server

```typescript
/**
 * gRPC Server Entry Point
 */

import * as grpc from '@grpc/grpc-js';

async function startGrpcServer() {
  const prisma = new PrismaClient();
  const redis = new Redis({
    host: process.env.REDIS_HOST || 'localhost',
    port: parseInt(process.env.REDIS_PORT || '6379')
  });
  
  const stateManager = new VehicleStateManager();
  const commandProcessor = new CommandProcessor(prisma, redis);
  const serviceImpl = new TelemetryServiceImpl(stateManager, commandProcessor);
  
  const server = new grpc.Server();
  
  server.addService(telemetry.TelemetryService.service, {
    sendTelemetryStream: serviceImpl.sendTelemetryStream.bind(serviceImpl),
    subscribeToVehicleUpdates: serviceImpl.subscribeToVehicleUpdates.bind(serviceImpl),
    bidirectionalCommandChannel: serviceImpl.bidirectionalCommandChannel.bind(serviceImpl),
    dispatchCommand: serviceImpl.dispatchCommand.bind(serviceImpl),
    getVehicleHistory: serviceImpl.getVehicleHistory.bind(serviceImpl),
    healthCheck: serviceImpl.healthCheck.bind(serviceImpl)
  });
  
  const port = process.env.GRPC_PORT || 50051;
  server.bindAsync(
    `0.0.0.0:${port}`,
    grpc.ServerCredentials.createInsecure(),
    (err, boundPort) => {
      if (err) {
        console.error('Failed to bind gRPC server:', err);
        return;
      }
      console.log(`gRPC server started on port ${boundPort}`);
      server.start();
    }
  );
}

startGrpcServer();
```

### Step 5: Node.js gRPC Client Example

```typescript
/**
 * Node.js gRPC Client for Fleet Management System
 */

import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import { randomUUID } from 'crypto';

class TelemetryClient {
  private client: any;
  private metadata: grpc.Metadata;

  constructor(target: string = 'localhost:50051') {
    const packageDefinition = protoLoader.loadSync('./protos/telemetry.proto', {
      keepCase: true,
      longs: String,
      enums: String,
      defaults: true,
      oneofs: true
    });
    
    const proto = grpc.loadPackageDefinition(packageDefinition) as any;
    this.client = new proto.fleetmanagement.telemetry.v1.TelemetryService(
      target,
      grpc.credentials.createInsecure()
    );
    
    this.metadata = new grpc.Metadata();
    this.metadata.set('client-id', randomUUID());
  }

  async sendTelemetryStream(vehicleId: string, updates: number = 100): Promise<void> {
    const call = this.client.sendTelemetryStream(this.metadata);
    
    call.on('data', (response: any) => {
      console.log(`Telemetry stream completed: ${response.updates_received} updates, Session: ${response.session_id}`);
      if (response.pending_commands?.length) {
        console.log(`Pending commands received: ${response.pending_commands.length}`);
      }
    });
    
    call.on('end', () => {
      console.log('Stream ended');
    });
    
    call.on('error', (error: Error) => {
      console.error('Stream error:', error);
    });
    
    // Send telemetry updates every 500ms
    for (let i = 0; i < updates; i++) {
      const update = {
        vehicle_id: vehicleId,
        latitude: 37.7749 + (i * 0.0001),
        longitude: -122.4194 + (i * 0.0001),
        speed_kph: 60 + (i % 20),
        heading_degrees: 180 + (i % 360),
        captured_at: {
          seconds: Math.floor(Date.now() / 1000),
          nanos: (Date.now() % 1000) * 1e6
        }
      };
      
      call.write(update);
      await new Promise(resolve => setTimeout(resolve, 500));
    }
    
    call.end();
  }

  async subscribeToVehicles(fleetId: string = 'all'): Promise<void> {
    const call = this.client.subscribeToVehicleUpdates({
      fleet_id: fleetId,
      preferred_interval_ms: 1000,
      client_id: 'dashboard_001'
    });
    
    call.on('data', (update: any) => {
      console.log(`Vehicle ${update.vehicle_id}: (${update.latitude}, ${update.longitude}) Speed: ${update.speed_kph} km/h`);
      
      if (update.pending_commands?.length) {
        for (const cmd of update.pending_commands) {
          console.log(`  Pending command: ${cmd.command_type} (ID: ${cmd.command_id})`);
        }
      }
    });
    
    call.on('end', () => {
      console.log('Subscription ended');
    });
    
    call.on('error', (error: Error) => {
      console.error('Subscription error:', error);
    });
  }

  async dispatchCommand(vehicleId: string, commandType: string): Promise<string> {
    return new Promise((resolve, reject) => {
      const request: any = {
        vehicle_id: vehicleId,
        command_type: commandType,
        priority: 'HIGH',
        dispatched_by: 'dispatcher_001'
      };
      
      if (commandType === 'REROUTE') {
        request.route = {
          route_id: 'ROUTE_123',
          waypoints: [
            { latitude: 37.7749, longitude: -122.4194, address: 'San Francisco' },
            { latitude: 37.8044, longitude: -122.2712, address: 'Oakland' }
          ],
          estimated_distance_km: 20
        };
      }
      
      this.client.dispatchCommand(request, this.metadata, (error: Error | null, response: any) => {
        if (error) {
          reject(error);
        } else {
          console.log(`Command dispatched: ${response.command_id} - ${response.message}`);
          resolve(response.command_id);
        }
      });
    });
  }

  async bidirectionalChannel(vehicleId: string): Promise<void> {
    const call = this.client.bidirectionalCommandChannel(this.metadata);
    
    call.on('data', (response: any) => {
      if (response.command_response) {
        console.log(`Command received: ${response.command_response.command_id} - ${response.command_response.status}`);
      } else if (response.keep_alive) {
        console.log(`Server keep-alive: last seq ${response.keep_alive.last_sequence_received}`);
      }
    });
    
    call.on('end', () => {
      console.log('Channel closed');
    });
    
    // Send keep-alive every 5 seconds
    let seq = 0;
    const interval = setInterval(() => {
      call.write({
        keep_alive: {
          sequence_number: seq++,
          sent_at: {
            seconds: Math.floor(Date.now() / 1000),
            nanos: (Date.now() % 1000) * 1e6
          }
        }
      });
    }, 5000);
    
    // Send telemetry through the channel
    setInterval(() => {
      call.write({
        telemetry: {
          vehicle_id: vehicleId,
          latitude: 37.7749 + Math.random() * 0.01,
          longitude: -122.4194 + Math.random() * 0.01,
          speed_kph: 60 + Math.random() * 20
        }
      });
    }, 2000);
    
    // Clean up after 30 seconds
    setTimeout(() => {
      clearInterval(interval);
      call.end();
    }, 30000);
  }
}

// Example usage
async function main() {
  const client = new TelemetryClient();
  
  try {
    // Send telemetry stream
    await client.sendTelemetryStream('VEHICLE_001', 10);
    
    // Dispatch a command
    await client.dispatchCommand('VEHICLE_001', 'REROUTE');
    
    // Subscribe to vehicle updates (runs until cancelled)
    // await client.subscribeToVehicles('east_region');
    
    // Bidirectional channel
    // await client.bidirectionalChannel('VEHICLE_001');
    
  } catch (error) {
    console.error('Client error:', error);
  }
}

main();
```

---

## The New Architecture in Motion: Communication Patterns Transformed

With the complete gRPC implementation in place, the communication model for the Fleet Management System is fundamentally transformed. Each interaction pattern is now optimized for its specific requirements.

### Telemetry Ingestion: From Chatty REST to Persistent Stream

**Before (REST):** 500 vehicles × 21,600 updates/day = 10.8 million HTTP requests daily. Each request requires connection establishment, TLS negotiation, HTTP header processing, and JSON parsing.

**After (gRPC):** 500 vehicles × 1 persistent stream = 500 connections total. Each connection remains open and transmits binary-encoded Protobuf messages with minimal overhead.

### Telemetry Ingestion Flow Diagram

```mermaid
sequenceDiagram
    participant Vehicle as Vehicle Telemetry (Node.js gRPC Client)
    participant gRPC as gRPC Server<br/>Node.js @grpc/grpc-js
    participant State as VehicleStateManager<br/>(In-Memory Map)
    participant Command as CommandProcessor
    participant Stream as EventEmitter

    Note over Vehicle,gRPC: Single Persistent Connection - 24/7 Operation
    
    Vehicle->>gRPC: SendTelemetryStream (Open Stream)
    activate gRPC
    gRPC->>Stream: Register stream (Vehicle ID)
    Stream-->>gRPC: Stream Registered
    
    loop Every 2 seconds (Continuous)
        Vehicle-->>gRPC: TelemetryUpdate (Protobuf, ~50 bytes)
        Note over gRPC: Binary serialization<br/>No HTTP overhead<br/>No connection setup<br/>Event-driven I/O
        gRPC->>State: Update vehicle state (Map)
        gRPC->>Command: Check pending commands
        alt Commands Pending
            Command-->>gRPC: Return pending commands
            gRPC-->>Vehicle: TelemetryAck (includes commands)
            Vehicle->>Vehicle: Execute commands
        else No Commands
            gRPC-->>Vehicle: TelemetryAck (acknowledgment only)
        end
    end
    
    Note over Vehicle,gRPC: Stream remains open<br/>Zero connection overhead per update<br/>Node.js handles thousands of concurrent streams
```

### Dashboard Visualization: From Polling to Push-Based Real-Time

**Before (REST):** Dashboard polls every 3 seconds, receiving full vehicle state regardless of changes. Each poll triggers database queries and full serialization.

**After (gRPC):** Dashboard subscribes once and receives incremental updates only when vehicle state changes. Server maintains connection and pushes updates as they occur using server-side streaming.

### Dashboard Streaming Flow Diagram

```mermaid
sequenceDiagram
    participant Dashboard as Web Dashboard (gRPC-Web)
    participant gRPC as gRPC Server<br/>Node.js @grpc/grpc-js
    participant State as VehicleStateManager
    participant Redis as Redis Cache

    Dashboard->>gRPC: SubscribeToVehicleUpdates (fleet_id="east_region")
    activate gRPC
    gRPC->>State: Register subscription with EventEmitter
    State-->>gRPC: Subscription confirmed
    gRPC-->>Dashboard: VehicleStatusUpdate (initial snapshot)
    
    Note over Dashboard,gRPC: Connection remains open for real-time updates<br/>Server-Side Streaming with Node.js
    
    loop Every 100ms or on change
        State->>State: Detect vehicle position changes
        State-->>gRPC: Emit 'update' event
        gRPC->>Redis: Get cached vehicle data
        gRPC-->>Dashboard: VehicleStatusUpdate (only changed vehicles)
        Dashboard->>Dashboard: Update map (incremental render)
        Note right of Dashboard: Server push eliminates polling<br/>Sub-second latency
    end
    
    Note over Dashboard,gRPC: Push-based updates<br/>Zero polling overhead<br/>Sub-second latency
```

### Command Dispatch: From Latent Polling to Instant Delivery

**Before (REST):** Commands stored in database, mobile app polls every 10-30 seconds, creating 0-30 second latency window.

**After (gRPC):** Commands delivered instantly through the active bidirectional stream or server-streaming channel.

### Command Dispatch Flow Diagram

```mermaid
sequenceDiagram
    participant Dashboard as Web Dashboard
    participant gRPC as gRPC Server
    participant Vehicle as Vehicle (Active Stream)
    participant Redis as Redis Stream
    participant DB as PostgreSQL<br/>Prisma ORM

    Dashboard->>gRPC: DispatchCommand (Unary)
    activate gRPC
    gRPC->>DB: Prisma create command
    DB-->>gRPC: Command stored
    gRPC->>Redis: Publish to Redis stream
    gRPC->>Vehicle: Check for active stream
    
    alt Vehicle Has Active Stream
        Note over gRPC,Vehicle: Immediate delivery via existing stream
        gRPC-->>Vehicle: CommandEnvelope or TelemetryAck with command
        Vehicle->>Vehicle: Process command instantly
        Vehicle-->>gRPC: CommandAck (via stream)
        gRPC-->>Dashboard: CommandResponse (delivered)
    else No Active Stream
        gRPC-->>Dashboard: CommandResponse (queued)
        Note over Vehicle: Vehicle will receive on next connection
    end
    
    deactivate gRPC
    
    Note over Dashboard,Vehicle: Delivery latency: <100ms with active stream<br/>0-2 seconds without stream
```

### Bidirectional Streaming: Full-Duplex Communication

The bidirectional streaming pattern enables true real-time, two-way communication between the vehicle and the server.

### Bidirectional Streaming Flow Diagram

```mermaid
sequenceDiagram
    participant Vehicle as Vehicle (Node.js Client)
    participant gRPC as gRPC Server
    participant State as VehicleStateManager
    participant Command as CommandProcessor

    Note over Vehicle,gRPC: Full-Duplex Channel - Both Directions Simultaneously
    
    Vehicle->>gRPC: BidirectionalCommandChannel (Open)
    activate gRPC
    
    par Incoming Stream (Vehicle to Server)
        loop Continuous
            Vehicle-->>gRPC: TelemetryUpdate (via channel)
            gRPC->>State: Update vehicle state
            Vehicle-->>gRPC: CommandAck (command execution confirmation)
            gRPC->>Command: Update command status
            Vehicle-->>gRPC: KeepAlive (heartbeat)
            gRPC-->>Vehicle: ServerKeepAlive (response)
        end
    and Outgoing Stream (Server to Vehicle)
        loop Continuous
            gRPC->>Command: Check pending commands
            alt New Command Available
                Command-->>gRPC: Command to deliver
                gRPC-->>Vehicle: CommandEnvelope (instant delivery)
                Note over Vehicle: Command executed immediately
            end
            gRPC-->>Vehicle: ServerKeepAlive (periodic)
        end
    end
    
    Note over Vehicle,gRPC: True real-time communication<br/>No polling, no latency<br/>Node.js event loop handles concurrent streams efficiently
```

### Architecture Comparison: REST vs. gRPC

### High-Level Architecture Comparison Diagram

```mermaid
graph TB
    subgraph "REST Architecture"
        direction TB
        Mobile1[Mobile App] -->|HTTP/1.1 JSON| LB1[Load Balancer]
        Web1[Web Dashboard] -->|Polling HTTP| LB1
        LB1 --> API1[Fastify REST<br/>Node.js]
        API1 --> Cache1[Redis Cache]
        API1 --> DB1[(PostgreSQL<br/>Prisma ORM)]
        API1 --> Queue1[BullMQ Queue]
        
        Mobile1 -.->|43,200 req/day/vehicle| API1
        Web1 -.->|Poll every 3s| API1
    end
    
    subgraph "gRPC Architecture"
        direction TB
        Mobile2[Mobile App] -->|Persistent gRPC Stream| LB2[gRPC Load Balancer]
        Web2[Web Dashboard] -->|gRPC-Web Stream| LB2
        LB2 --> API2[Node.js gRPC Server<br/>@grpc/grpc-js]
        API2 --> State2[VehicleStateManager<br/>In-Memory Map]
        API2 --> Cache2[Redis Streams]
        API2 --> DB2[(PostgreSQL<br/>Prisma ORM)]
        
        Mobile2 -.->|1 persistent connection| API2
        Web2 -.->|1 streaming connection| API2
    end
    
    style REST Architecture fill:#e1f5fe
    style gRPC Architecture fill:#e8f5e9
```

### Communication Pattern Comparison Diagram

```mermaid
graph LR
    subgraph "REST Communication Patterns"
        A1[Client] -->|Request 1| B1[Server]
        B1 -->|Response 1| A1
        A1 -->|Request 2| B1
        B1 -->|Response 2| A1
        
        C1[Client] -->|Poll| D1[Server]
        D1 -->|Data or Empty| C1
        C1 -->|Poll| D1
    end
    
    subgraph "gRPC Communication Patterns"
        A2[Client] <-->|Bidirectional Stream| B2[Server]
        
        C2[Client] -->|Client Stream| D2[Server]
        D2 -->|Single Response| C2
        
        E2[Client] -->|Single Request| F2[Server]
        F2 -->|Server Stream| E2
    end
    
    style REST Communication Patterns fill:#ffebee
    style gRPC Communication Patterns fill:#e8f5e9
```

---

## Node.js Ecosystem Features Powering the gRPC Service

Node.js's modern ecosystem provides several powerful features that make gRPC service implementation productive and performant:

### 1. Fastify - High-Performance HTTP Framework

Fastify provides exceptional performance with low overhead, making it ideal for REST endpoints:

```typescript
import Fastify from 'fastify';
import fastifySwagger from '@fastify/swagger';

const app = Fastify({
  logger: true,
  trustProxy: true,
  requestIdHeader: 'x-request-id'
});

// JSON Schema validation with TypeBox
import { Type } from '@sinclair/typebox';

const schema = {
  body: Type.Object({
    latitude: Type.Number({ minimum: -90, maximum: 90 }),
    longitude: Type.Number({ minimum: -180, maximum: 180 })
  })
};

app.post('/telemetry', { schema }, async (request, reply) => {
  // TypeScript infers the body type automatically
  const { latitude, longitude } = request.body;
  return { status: 'ok' };
});
```

### 2. Prisma ORM - Type-Safe Database Access

Prisma provides type-safe database queries with auto-completion:

```typescript
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

// Type-safe queries with auto-completion
const vehicle = await prisma.vehicle.findUnique({
  where: { id: vehicleId },
  include: {
    telemetry: { take: 10, orderBy: { timestamp: 'desc' } },
    commands: { where: { status: 'PENDING' } }
  }
});

// Type-safe updates
await prisma.vehicle.update({
  where: { id: vehicleId },
  data: {
    currentLatitude: latitude,
    currentLongitude: longitude,
    lastTelemetry: new Date()
  }
});
```

### 3. BullMQ - Redis-Based Job Queue

BullMQ provides robust background job processing with retries and delays:

```typescript
import { Queue, Worker } from 'bullmq';

const telemetryQueue = new Queue('telemetry-processing', {
  connection: redis,
  defaultJobOptions: {
    attempts: 3,
    backoff: { type: 'exponential', delay: 1000 },
    removeOnComplete: 100
  }
});

const worker = new Worker('telemetry-processing', async (job) => {
  const { vehicleId, telemetry } = job.data;
  await processTelemetry(vehicleId, telemetry);
}, { connection: redis });
```

### 4. ioredis - Advanced Redis Client

ioredis provides comprehensive Redis features with promise-based API:

```typescript
import Redis from 'ioredis';

const redis = new Redis({
  host: 'localhost',
  port: 6379,
  maxRetriesPerRequest: null,
  enableReadyCheck: false
});

// Redis Pub/Sub for real-time updates
await redis.publish('vehicle:updates', JSON.stringify(update));

// Redis Streams for command delivery
await redis.xadd(`vehicle:${vehicleId}:commands`, '*', 'command', JSON.stringify(command));

// Redis Cache with TTL
await redis.setex(`vehicle:${vehicleId}`, 5, JSON.stringify(state));
```

### 5. OpenTelemetry for Observability

OpenTelemetry provides comprehensive tracing and metrics:

```typescript
import { NodeTracerProvider } from '@opentelemetry/sdk-trace-node';
import { GrpcInstrumentation } from '@opentelemetry/instrumentation-grpc';
import { registerInstrumentations } from '@opentelemetry/instrumentation';

const provider = new NodeTracerProvider();
provider.register();

registerInstrumentations({
  instrumentations: [
    new GrpcInstrumentation(),
    new HttpInstrumentation()
  ]
});

const tracer = provider.getTracer('fleet-telemetry');

// Use in service
const span = tracer.startSpan('process-telemetry');
span.setAttribute('vehicle.id', vehicleId);
// ... processing
span.end();
```

### 6. TypeScript - Type Safety at Scale

TypeScript provides compile-time type checking and excellent IDE support:

```typescript
// Type-safe gRPC client
interface TelemetryServiceClient {
  sendTelemetryStream(
    request: AsyncIterable<TelemetryUpdate>
  ): Promise<TelemetryAck>;
  subscribeToVehicleUpdates(
    request: SubscribeRequest
  ): AsyncIterable<VehicleStatusUpdate>;
}

// Type-safe event emitters
interface StateManagerEvents {
  update: (data: { vehicleId: string; state: VehicleState }) => void;
  disconnect: (vehicleId: string) => void;
}

class VehicleStateManager extends EventEmitter {
  emit<K extends keyof StateManagerEvents>(
    event: K,
    ...args: Parameters<StateManagerEvents[K]>
  ): boolean {
    return super.emit(event, ...args);
  }
  
  on<K extends keyof StateManagerEvents>(
    event: K,
    listener: StateManagerEvents[K]
  ): this {
    return super.on(event, listener);
  }
}
```

### 7. Pino - High-Performance Logging

Pino provides structured logging with minimal overhead:

```typescript
import pino from 'pino';

const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  formatters: {
    level: (label) => ({ level: label }),
    bindings: (bindings) => ({ pid: bindings.pid, host: bindings.hostname })
  },
  transport: process.env.NODE_ENV !== 'production'
    ? { target: 'pino-pretty', options: { colorize: true, translateTime: true } }
    : undefined
});

// Structured logging
logger.info({ vehicleId, trackingId, latency: 25 }, 'Telemetry processed');
logger.error({ error, vehicleId }, 'Failed to process telemetry');
```

---

## Comparative Analysis: REST vs. gRPC in Node.js

| Aspect | REST (Fastify/JSON) | gRPC (@grpc/grpc-js/Protobuf) with Node.js |
|--------|---------------------|---------------------------------------------|
| **Framework** | Fastify (HTTP/1.1) | @grpc/grpc-js (HTTP/2) |
| **Data Format** | JSON (text) | Protobuf (binary) |
| **Serialization** | JSON.stringify (~200-500 bytes) | Protobuf (~30-100 bytes) |
| **Validation** | TypeBox JSON Schema | Protobuf (generated code) |
| **Performance** | ~10,000-20,000 req/sec per core | ~20,000-30,000 req/sec per core |
| **Streaming** | WebSocket required | Native (unary, server, client, bidirectional) |
| **Contract** | OpenAPI (auto-generated) | Protobuf (single source) |
| **Code Generation** | OpenAPI generators | @grpc/proto-loader |
| **Browser Support** | Native (HTTP/JSON) | gRPC-Web via envoy/grpc-gateway |
| **Caching** | HTTP caching + Redis | Application layer |
| **Async Support** | Native (async/await) | Native (async/await with streams) |
| **Observability** | OpenTelemetry + Pino | OpenTelemetry with gRPC instrumentation |
| **Type Safety** | TypeScript + TypeBox | Generated types + TypeScript |
| **Memory Footprint** | Moderate | Low |
| **Event Loop** | Non-blocking I/O | Non-blocking I/O with streaming |

---

## Conclusion: Node.js gRPC Ecosystem for High-Performance Services

The move from REST to gRPC in Node.js represents a significant architectural evolution. For the Fleet Management System, the benefits are substantial:

### Key Takeaways

**Performance and Efficiency:**
- **80% reduction in data transfer:** Protobuf binary encoding reduces payload size from ~500 bytes to ~50 bytes.
- **95% reduction in connection overhead:** Persistent streams replace millions of individual HTTP requests.
- **2-3x throughput increase:** gRPC on Node.js with `@grpc/grpc-js` outperforms Fastify for high-volume scenarios, leveraging Node.js's event-driven architecture.

**Real-Time Capabilities:**
- **Sub-second command delivery:** Bidirectional streams deliver commands within 100ms.
- **True push-based dashboards:** Server-side streaming eliminates polling overhead.
- **Full-duplex communication:** Vehicles and server can exchange messages simultaneously using bidirectional streaming.

**Developer Experience:**
- **Contract-first development:** Single `.proto` file defines the entire API.
- **Type-safe generated code:** `@grpc/proto-loader` produces strongly-typed TypeScript stubs.
- **Rich ecosystem:** Fastify for REST fallbacks, Prisma for type-safe database access, BullMQ for job queues.

**Operational Excellence:**
- **Event-driven:** Node.js's event loop handles thousands of concurrent streams efficiently.
- **Comprehensive observability:** OpenTelemetry provides distributed tracing, metrics, and logging.
- **Simplified deployment:** Container-ready with minimal dependencies and fast startup times.

### Node.js vs. Python vs. .NET 10: A Comparative Note

This Node.js implementation parallels the .NET 10 and Python architectural stories covered earlier. While all three achieve the same architectural goals, they leverage different ecosystem strengths:

| Aspect | Node.js (Fastify + gRPC) | Python (FastAPI + grpcio) | .NET 10 (gRPC + ASP.NET Core) |
|--------|--------------------------|---------------------------|-------------------------------|
| **Primary Strengths** | Event-driven I/O, npm ecosystem, TypeScript | Developer productivity, data science, async/await | Performance, Native AOT, enterprise features |
| **Streaming Performance** | Excellent with event loop | Excellent with asyncio | Exceptional with native threading |
| **Concurrency Model** | Single-threaded event loop | Async/await cooperative multitasking | Thread pool / async I/O |
| **Type Safety** | TypeScript (compile-time) | Mypy + Pydantic (runtime) | Compile-time (C#) |
| **Deployment** | Container images ~100-300 MB | Container images ~200-500 MB | Native AOT images ~30-50 MB |
| **Startup Time** | 50-150 ms | 200-500 ms | 20-50 ms (AOT) |
| **Memory Footprint** | Low (50-200 MB) | Moderate (100-300 MB) | Very low (20-50 MB AOT) |
| **Package Ecosystem** | npm (largest ecosystem) | PyPI (scientific computing) | NuGet (enterprise) |
| **AI Integration** | TensorFlow.js, LangChain | PyTorch, TensorFlow, scikit-learn | AI Minimal APIs, Semantic Kernel |
| **Best For** | I/O-bound apps, real-time, microservices | Data-intensive, ML integration, rapid dev | High-performance, low-memory, enterprise |

### When to Choose Which

**Node.js remains the appropriate choice when:**
- Event-driven, non-blocking I/O patterns are optimal
- Real-time applications with high concurrency requirements
- JavaScript/TypeScript ecosystem alignment (full-stack JavaScript)
- Rapid development with npm's extensive package ecosystem
- Microservices that need fast startup times

**gRPC with Node.js is the superior choice when:**
- Real-time bidirectional streaming is required
- Mobile clients need efficient data transfer
- Polyglot environments benefit from Protobuf contracts
- High-concurrency I/O-bound workloads are common
- Full-stack TypeScript teams want shared types

The Node.js ecosystem, with Fastify for REST and `@grpc/grpc-js` for gRPC, provides a flexible, high-performance foundation for building modern real-time systems. The combination of TypeScript, event-driven architecture, and comprehensive observability makes Node.js a compelling choice for gRPC-based architectures, particularly in teams that value the JavaScript/TypeScript ecosystem and need to handle high-concurrency I/O workloads.

---

## The .NET 10 and Python Parallels: A Brief Recap

For readers interested in other ecosystems, the companion architectural documents explore the same Fleet Management System use case:

### .NET 10 Implementation Highlights:
- **AI-Enhanced Minimal APIs:** Intelligent service discovery with natural language descriptions
- **Native AOT Compilation:** Startup times under 50ms and container images under 50MB
- **Hybrid Cache:** Combined in-memory and distributed caching with automatic stale-while-revalidate
- **Enhanced gRPC Middleware:** Per-method middleware and streaming-aware interceptors
- **Deep OpenTelemetry Integration:** Built-in metrics, traces, and structured logging for gRPC

### Python Implementation Highlights:
- **FastAPI with Pydantic v2:** Automatic OpenAPI docs and runtime data validation
- **SQLAlchemy 2.0 Async:** Fully async ORM with improved typing
- **grpcio with asyncio:** Native async gRPC support
- **Rich Data Science Ecosystem:** Easy integration with ML and analytics pipelines
- **Developer Velocity:** Rapid prototyping with Python's expressiveness

All three implementations—Node.js, Python, and .NET 10—achieve the same architectural goals of high-performance, real-time communication through gRPC. The choice between them depends on team expertise, ecosystem requirements, operational constraints, and specific workload characteristics. What remains constant is the architectural shift from REST's request-response model to gRPC's streaming-first, contract-driven paradigm—a transformation that enables the next generation of real-time, scalable distributed systems.

### Final Architecture Overview Diagram

```mermaid
graph TB
    subgraph "Clients"
        Mobile[React Native Mobile App<br/>gRPC Client]
        Web[React Web Dashboard<br/>gRPC-Web Client]
    end
    
    subgraph "Edge & Load Balancing"
        LB[gRPC Load Balancer<br/>Envoy / NGINX]
        GW[gRPC Gateway<br/>REST-to-gRPC Proxy]
    end
    
    subgraph "Core Services"
        direction TB
        GRPC[Node.js gRPC Service<br/>@grpc/grpc-js]
        State[VehicleStateManager<br/>In-Memory Map + EventEmitter]
        Cache[Redis Streams & Cache<br/>Real-time Pub/Sub]
    end
    
    subgraph "Data Layer"
        DB[(PostgreSQL<br/>Prisma ORM)]
        Queue[BullMQ Job Queue<br/>Background Processing]
    end
    
    subgraph "Observability"
        OTEL[OpenTelemetry<br/>Traces & Metrics]
        LOG[Structured Logging<br/>Pino]
    end
    
    Mobile -->|Persistent gRPC Stream| LB
    Web -->|gRPC-Web Stream| LB
    LB --> GRPC
    GW -->|REST Fallback| GRPC
    
    GRPC --> State
    GRPC --> Cache
    GRPC --> DB
    GRPC --> Queue
    
    GRPC -.-> OTEL
    GRPC -.-> LOG
    
    style Clients fill:#e3f2fd
    style Edge & Load Balancing fill:#fff3e0
    style Core Services fill:#e8f5e9
    style Data Layer fill:#fce4ec
    style Observability fill:#f3e5f5
```

---

**Vineet Sharma**  
*Architect, Fleet Management Systems*