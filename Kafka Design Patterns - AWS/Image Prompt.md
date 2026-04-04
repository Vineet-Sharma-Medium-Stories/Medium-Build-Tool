
## Main Prompt
```
Now create gemini image prompts for all 4 stories and 11 patterns in code block as readme. The images should be in AWS style with light background, infrastructure at background, technology and pattern logos with text. Include title and sub title, all 4 story title starts with "11 Kafka Design Patterns -". Place "Vineet Sharma" at bottom right.
```

# 🎨 Gemini Image Prompts for Kafka Design Patterns Series (Light Background)

## Series Title: **11 Kafka Design Patterns for Every Backend Engineer**

**Author:** Vineet Sharma (placed at bottom right of all images)

**Style:** AWS architecture style with **light background** — clean white/off-white canvas, light gray grid, blue/orange/teal color palette for icons and accents, infrastructure diagrams, technology and pattern logos, clear text hierarchy.

---

## 📸 Cover Image (Series Master Story)

```markdown
Generate a professional AWS-style architectural hero image for a technical blog series titled "11 Kafka Design Patterns for Every Backend Engineer" with a LIGHT BACKGROUND.

Background: Clean white or off-white canvas with a subtle light gray grid pattern. Soft abstract cloud infrastructure outlines in very light blue (#E3F2FD). AWS service icons (Amazon MSK, S3, DynamoDB, Lambda, RDS, OpenSearch) in light gray with darker blue accents. Flowing data streams in teal (#00A8C6) and orange (#FF6B35) colors connecting the services. A large Amazon MSK logo centered in the background with data flowing outward like a hub.

Foreground: 11 glowing pattern icons arranged in a circular or grid pattern around the center. Each icon represents a pattern: Outbox (envelope with database), Idempotent Consumer (checkmark with duplicate symbol), Partition Key (key with ordered list), DLQ (skull with queue), Retry (recycling arrows), Event Sourcing (timeline with events), CQRS (split command/query arrows), Compacted Topic (compressed folder with key), Event Carried State Transfer (package with data), Claim Check (ticket with S3), Stream-Table (overlapping stream and table), Saga (chain of circles with checkmarks).

Top text in large bold dark navy font: "11 KAFKA DESIGN PATTERNS". Below in medium dark gray font: "For Every Backend Engineer". Bottom right corner: "Vineet Sharma" in small dark gray text.

Overall style: Clean whiteboard or documentation aesthetic, AWS QuickSight or AWS Training slide style, light background, crisp icons, professional diagrammatic look, no realistic people.
```

---

## 📖 Story 1: Overview (All 11 Patterns)

```markdown
Generate an AWS-style technical illustration for a blog story titled "11 Kafka Design Patterns - Part 1: Overview of All 11 Patterns" with a LIGHT BACKGROUND.

Background: Clean white canvas with light gray grid. AWS cloud infrastructure diagram with Amazon MSK cluster in the center, surrounded by connection lines to other AWS services: S3 bucket, DynamoDB table, Lambda function, RDS database, OpenSearch domain, and ECS containers. All service icons in light gray with dark blue outlines. Subtle data flow arrows in teal and orange.

Foreground: A large central hub representing Kafka with 11 labeled pattern cards radiating outward in a semicircle or wheel arrangement. Each card has a small icon and pattern name on a white card with light gray border and soft shadow: Outbox, Idempotent Consumer, Partition Key, DLQ, Retry, Event Sourcing, CQRS, Compacted Topic, Event Carried State Transfer, Claim Check, Stream-Table Duality, Saga.

Top title text: "11 KAFKA DESIGN PATTERNS" in bold dark navy (#0A1929). Subtitle: "Part 1 — Overview of All 11 Patterns" in dark teal (#006B6B). Bottom right corner: "Vineet Sharma" in small dark gray text.

Color scheme: White background (#FFFFFF), light gray grid (#F0F0F0), dark navy text (#0A1929), teal accent (#00A8C6), orange accent (#FF6B35). Icons should be clean and modern, similar to AWS architecture diagram icons in dark blue.
```

---

## 📖 Story 2: Reliability & Ordering Patterns

```markdown
Generate an AWS-style technical illustration for a blog story titled "11 Kafka Design Patterns - Part 2: Reliability & Ordering Deep Dive" with a LIGHT BACKGROUND.

Background: Clean white canvas with light gray grid. AWS infrastructure showing Amazon MSK brokers, DynamoDB table (for idempotency), RDS/Aurora database (for outbox table), SQS queue (for DLQ), and CloudWatch alarms. All icons in light gray with dark blue outlines. Orange and teal connection lines.

Foreground: Five pattern icons prominently displayed in a horizontal or circular arrangement:

1. Transactional Outbox — Envelope merging into a database cylinder, with green checkmark.
2. Idempotent Consumer — Circular arrow with a checkmark inside, and a duplicate symbol crossed out in red.
3. Partition Key — A key with ordered list items (1,2,3) flowing into partitions.
4. Dead Letter Queue — A skull icon inside a queue/message box, with an alert bell in orange.
5. Retry with Backoff — Clock with curved arrows showing increasing delays (1s, 2s, 4s).

Top title: "11 KAFKA DESIGN PATTERNS" in bold dark navy. Subtitle: "Part 2 — Reliability & Ordering Deep Dive" in dark orange (#CC5500). Bottom right: "Vineet Sharma".

Color scheme: White background, dark navy text, orange and teal accents for icons. Icons should have clean dark blue outlines. Use green for success paths, red for warnings/duplicates.
```

---

## 📖 Story 3: Data & State Patterns

```markdown
Generate an AWS-style technical illustration for a blog story titled "11 Kafka Design Patterns - Part 3: Data & State Deep Dive" with a LIGHT BACKGROUND.

Background: Clean white canvas with light gray grid. AWS infrastructure showing Amazon MSK with compacted topic visualization (stack of messages collapsing into one), S3 Glacier for long-term event archive (light blue icon), ksqlDB or Kafka Streams processor, DynamoDB for materialized views, and Glue Schema Registry. Data lineage arrows in teal showing events flowing from producers to storage to materialized views.

Foreground: Four pattern icons prominently displayed:

1. Event Sourcing — A timeline with event dots leading to a database snapshot. Icons for "past", "present", "replay" in teal.
2. CQRS — Split design: left side "Command" (pencil/arrow in dark blue), right side "Query" (magnifying glass in green). Connected by Kafka in center with orange arrow.
3. Compacted Topic — A folder or database icon with a key, showing only the latest version retained. Old versions fading to light gray.
4. Event Carried State Transfer — An event envelope that is "full" or "bulging" with data, with a "no fetch needed" symbol (crossed-out network icon in red).

Top title: "11 KAFKA DESIGN PATTERNS" in bold dark navy. Subtitle: "Part 3 — Data & State Deep Dive" in dark teal (#006B6B). Bottom right: "Vineet Sharma".

Color scheme: White background, dark navy text, teal and green accents conveying "data persistence" and "state management". Icons should feel solid and durable, like database or storage symbols, with dark blue outlines.
```

---

## 📖 Story 4: Performance & Integration Patterns

```markdown
Generate an AWS-style technical illustration for a blog story titled "11 Kafka Design Patterns - Part 4: Performance & Integration Deep Dive" with a LIGHT BACKGROUND.

Background: Clean white canvas with light gray grid. AWS infrastructure showing Amazon MSK connected to S3 (for Claim Check — large arrow to S3 bucket), ECS/EKS containers running Kafka Streams (light gray container icons), Step Functions workflow for saga orchestration (connected circles), and API Gateway for external integration. High-speed data flow lines in orange and teal.

Foreground: Three pattern icons prominently displayed:

1. Claim Check — A ticket or claim stub with an S3 bucket icon. Visual of large file (red) going to S3, small reference (green) going to Kafka.
2. Stream-Table Duality — Overlapping icons: a flowing stream (blue wave lines) and a stable table (green grid). Joining symbol (orange overlap) in center.
3. Saga (Choreography) — A chain of connected circles, each with a checkmark or cross. Compensating arrows looping back in red. Event-driven messaging symbols.

Top title: "11 KAFKA DESIGN PATTERNS" in bold dark navy. Subtitle: "Part 4 — Performance & Integration Deep Dive" in dark orange (#CC5500). Bottom right: "Vineet Sharma".

Color scheme: White background, dark navy text, bright cyan (#00A8C6) and orange (#FF6B35) accents to convey "speed", "integration", and "throughput". Icons should feel dynamic and connected, with arrow flows in teal.
```

---

## 🎯 Individual Pattern Images (12 total) — Light Background

### 1. Transactional Outbox Pattern

```markdown
Generate an AWS-style technical diagram for the "Transactional Outbox" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. Left side shows an application service icon (dark blue) writing to a database cylinder (light gray with dark blue outline). Inside the database, two tables represented as grids: "Orders" and "Outbox" (Outbox highlighted in orange). A transaction boundary (dashed dark blue box) surrounds both writes. Right side shows a Debezium connector (or Lambda icon) reading from the Outbox and publishing to an Amazon MSK topic (Kafka icon in dark blue). A consumer icon reads from the topic.

Text labels in dark navy: "1. BEGIN TX", "2. INSERT Order", "3. INSERT Outbox", "4. COMMIT", "CDC / Poller", "Publish to Kafka", "Consumer".

Top title in bold dark navy: "Transactional Outbox Pattern — Exactly-Once Between DB and Kafka". Bottom right corner: "Vineet Sharma" in small dark gray text.

Color scheme: White background, dark navy text and outlines, orange highlight on Outbox table, teal arrows. The transaction boundary should be a dashed dark blue line.
```

### 2. Idempotent Consumer Pattern

```markdown
Generate an AWS-style technical diagram for the "Idempotent Consumer" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. Kafka topic icon sending duplicate messages (visualized as two identical envelopes with same offset number, one in green, one in light gray) to a consumer icon (dark blue). The consumer checks a DynamoDB table icon (light gray with dark outline, labeled "Idempotency Store") with conditional write. First message writes marker (green check) and processes; second message sees existing marker and skips (red X).

Text labels in dark navy: "Duplicate Message", "Conditional PUT (attribute_not_exists)", "First → Process", "Duplicate → Skip", "DynamoDB TTL 7 days".

Top title in bold dark navy: "Idempotent Consumer Pattern — Making Duplicates Harmless". Bottom right: "Vineet Sharma".

Color scheme: White background, dark navy text, green for success path, red for duplicate skip. DynamoDB icon prominently displayed in light gray with dark blue outline.
```

### 3. Partition Key / Ordering Pattern

```markdown
Generate an AWS-style technical diagram for the "Partition Key / Ordering" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A producer icon (dark blue) sending three messages with the same key "order_123" (orange highlight on key). The key hashes to Partition 2 of a Kafka topic with 4 partitions shown as horizontal bars. All three messages stack in order within Partition 2 (shown as 1,2,3). A consumer icon (dark blue) reads from Partition 2, processing messages in sequence.

Text labels in dark navy: "Key: order_123", "Hash → Partition 2", "Partition 0", "Partition 1", "Partition 2 (ordered)", "Partition 3", "Consumer → Sequential Processing".

Top title in bold dark navy: "Partition Key Pattern — Preserving Order Per Entity". Bottom right: "Vineet Sharma".

Color scheme: White background, dark navy text, Partition 2 highlighted in teal or orange. Show the hash function visually with an arrow.
```

### 4. Dead Letter Queue (DLQ) Pattern

```markdown
Generate an AWS-style technical diagram for the "Dead Letter Queue (DLQ)" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A main Kafka topic icon (dark blue) with messages. A poison message (skull icon in red) enters the consumer icon. Consumer fails (red X), retries 3 times (counters shown), then sends to DLQ topic (red queue icon). Main topic continues processing good messages (green checkmarks). CloudWatch alarm icon monitors DLQ topic with bell icon. An engineer silhouette (gray) reviews DLQ and replays fixed messages (green arrow).

Text labels in dark navy: "Main Topic", "Poison Message", "Retry 1,2,3", "DLQ Topic", "CloudWatch Alarm", "Manual Replay".

Top title in bold dark navy: "Dead Letter Queue Pattern — Isolating Poison Messages". Bottom right: "Vineet Sharma".

Color scheme: White background, red for poison message and DLQ, green for normal flow, dark navy text. Alarm bell icon on CloudWatch in orange.
```

### 5. Retry with Backoff Pattern

```markdown
Generate an AWS-style technical diagram for the "Retry with Backoff" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A consumer icon (dark blue) fails to process a message (red X). The message routes to retry topics shown as three horizontal bars: "retry_1s" (1 second delay with small clock), then "retry_5s" (5 second delay with medium clock), then "retry_30s" (30 second delay with large clock). Each retry topic has its own consumer icon. After max retries, message goes to DLQ (red queue). Exponential curve showing increasing delays.

Text labels in dark navy: "Transient Failure", "Retry 1s", "Retry 5s", "Retry 30s", "Exponential Backoff + Jitter", "DLQ after 3 retries".

Top title in bold dark navy: "Retry with Backoff Pattern — Handling Transient Failures". Bottom right: "Vineet Sharma".

Color scheme: White background, dark navy text, orange for retry topics, red for DLQ. Clock icons in dark blue.
```

### 6. Event Sourcing Pattern

```markdown
Generate an AWS-style technical diagram for the "Event Sourcing" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A horizontal timeline from left to right showing events as envelopes: "OrderCreated" (teal), "PaymentProcessed" (teal), "OrderShipped" (teal). Each event appended to a Kafka topic icon (dark blue). A "State Builder" consumer icon reads all events and applies them to build current state in a database cylinder (light gray with dark outline). A "Snapshot" icon periodically saves state to S3 bucket (orange) for faster recovery.

Text labels in dark navy: "Immutable Event Log", "Replay from beginning", "Apply Event → New State", "Snapshot to S3", "Current State Cache".

Top title in bold dark navy: "Event Sourcing Pattern — Kafka as Source of Truth". Bottom right: "Vineet Sharma".

Color scheme: White background, dark navy text, teal events in order, orange S3 icon for snapshots.
```

### 7. CQRS Pattern

```markdown
Generate an AWS-style technical diagram for the "CQRS (Command Query Responsibility Segregation)" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. Split design with a vertical divider line. Left side labeled "Command Side" in dark blue: API icon receives commands, validates (checkmark), publishes events to Kafka center icon. Right side labeled "Query Side" in teal: Multiple read models as icons — DynamoDB (mobile), OpenSearch (analytics), Aurora (admin). Events flow from Kafka center to each read model updater (downward arrows).

Text labels in dark navy: "Command → Validate → Publish", "Event Bus (Kafka)", "Read Model Updaters", "DynamoDB (Mobile)", "OpenSearch (Analytics)", "Aurora (Admin)".

Top title in bold dark navy: "CQRS Pattern — Separate Read and Write Models". Bottom right: "Vineet Sharma".

Color scheme: White background, dark navy text, dark blue for command side, teal for query side, Kafka in center as orange bridge icon.
```

### 8. Compacted Topic Pattern

```markdown
Generate an AWS-style technical diagram for the "Compacted Topic" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A Kafka topic icon (dark blue) with multiple messages for the same key "product_123". Messages shown as stacked rectangles: v1: price=19.99 (light gray), v2: price=24.99 (medium gray), v3: price=24.99 (dark teal, highlighted). After compaction (compression arrows), only v3 remains. A new consumer icon starts from end (green arrow) and immediately sees only the latest value. Multiple service icons (Order, Inventory, Pricing) read from the same compacted topic.

Text labels in dark navy: "Key: product_123", "v1, v2, v3 (only latest kept)", "Compaction", "Latest per key", "All services get same current data".

Top title in bold dark navy: "Compacted Topic Pattern — Distributed Key-Value Store". Bottom right: "Vineet Sharma".

Color scheme: White background, dark navy text, stack of messages collapsing into one highlighted in teal. Multiple consumer icons in dark blue.
```

### 9. Event Carried State Transfer Pattern

```markdown
Generate an AWS-style technical diagram for the "Event Carried State Transfer" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A producer icon (User Service in dark blue) publishes an event. The event envelope is visibly "full" — containing user data fields (name, email, preferences) inside or next to it. Multiple consumer icons (Email, Notification, Analytics in teal) receive the same event via Kafka (center icon). Each consumer processes using data from the event — no arrows back to User Service. A crossed-out network icon in red emphasizes "no fetching".

Text labels in dark navy: "UserUpdated Event (carries full profile)", "Email Service → uses email field", "Notification → uses preferences", "Analytics → uses all data", "NO FETCHING NEEDED".

Top title in bold dark navy: "Event Carried State Transfer — Decouple Consumers from Source". Bottom right: "Vineet Sharma".

Color scheme: White background, dark navy text, full event envelope in orange, consumers in teal, crossed-out fetch icon in red.
```

### 10. Claim Check Pattern

```markdown
Generate an AWS-style technical diagram for the "Claim Check" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A producer icon (dark blue) with a large file icon showing "100MB" in red. Large arrow points upward to S3 bucket icon (orange). Producer sends small reference message (ticket icon in green) to Kafka topic icon (dark blue). Consumer icon (teal) receives small message, then downloads from S3 using presigned URL (arrow from S3 to consumer). S3 lifecycle rule icon shows calendar with "Expire after 90 days".

Text labels in dark navy: "Large Payload (100MB)", "Upload to S3", "Claim Check (small reference)", "Kafka Message < 1KB", "Download from S3", "Process", "S3 Lifecycle → Expire after 90 days".

Top title in bold dark navy: "Claim Check Pattern — Handling Large Messages with S3". Bottom right: "Vineet Sharma".

Color scheme: White background, dark navy text, large file in red, S3 icon in orange, Kafka message small in green.
```

### 11. Stream-Table Duality Pattern

```markdown
Generate an AWS-style technical diagram for the "Stream-Table Duality" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. Left side: a stream of click events represented as flowing wave lines in teal with "10K/sec" label. Right side: a table of user profiles represented as grid icon in green, labeled "compacted topic". Center: a Kafka Streams or ksqlDB processor icon (dark blue) with a RocksDB state store icon (cylinder). Join operation symbol (overlap circle) shows stream enriched with table data. Output arrow to "enriched clicks" stream.

Text labels in dark navy: "Click Stream (10K/sec)", "User Profiles Table (compacted)", "Stream-Table Join", "RocksDB Local Cache", "Enriched Clicks Output".

Top title in bold dark navy: "Stream-Table Duality Pattern — Real-Time Enrichment". Bottom right: "Vineet Sharma".

Color scheme: White background, dark navy text, teal waves for stream, green grid for table, orange for join operation.
```

### 12. Saga (Choreography) Pattern

```markdown
Generate an AWS-style technical diagram for the "Saga (Choreography)" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A chain of service circles connected horizontally: Trip Service (dark blue) → Flight Service (dark blue) → Hotel Service (dark blue) → Car Service (dark blue). Events flow between them via Kafka topic icons (orange) as connectors. Success path shows green checkmarks on each step. Failure path shows a red X at Hotel, with dashed compensation arrows (red) going backward: Hotel cancels, Flight cancels.

Text labels in dark navy: "Start Saga", "FlightBooked →", "HotelBooked →", "CarBooked →", "Trip Complete", "Failure: HotelBookingFailed ←", "Compensate: Cancel Flight".

Top title in bold dark navy: "Saga Pattern — Distributed Transactions Without 2PC". Bottom right: "Vineet Sharma".

Color scheme: White background, dark navy text, green for success path, red for failure and compensation arrows, Kafka topics as orange connectors.
```

---

## 📋 Quick Reference: All Light Background Prompts Summary

```markdown
# GEMINI IMAGE PROMPTS INDEX — LIGHT BACKGROUND

## Common Elements Across All Light Background Images
- Clean white/off-white background (#FFFFFF)
- Subtle light gray grid pattern (#F0F0F0)
- Dark navy text and outlines (#0A1929)
- Accent colors: Teal (#00A8C6), Orange (#FF6B35), Green (#00A86B), Red (#FF4444)
- Clean sans-serif fonts (similar to AWS documentation)
- No realistic people — use icons and silhouettes
- "Vineet Sharma" at bottom right corner of every image
- Professional, clean, whiteboard-style documentation aesthetic
- AWS architecture diagram style with light background

## Series Cover
1. Master Cover Image — 11 Kafka Design Patterns (Light Background)

## Story Images (4)
2. Part 1 — Overview of All 11 Patterns (Light Background)
3. Part 2 — Reliability & Ordering Deep Dive (Light Background)
4. Part 3 — Data & State Deep Dive (Light Background)
5. Part 4 — Performance & Integration Deep Dive (Light Background)

## Individual Pattern Images (12)
6. Transactional Outbox (Light Background)
7. Idempotent Consumer (Light Background)
8. Partition Key / Ordering (Light Background)
9. Dead Letter Queue (DLQ) (Light Background)
10. Retry with Backoff (Light Background)
11. Event Sourcing (Light Background)
12. CQRS (Light Background)
13. Compacted Topic (Light Background)
14. Event Carried State Transfer (Light Background)
15. Claim Check (Light Background)
16. Stream-Table Duality (Light Background)
17. Saga (Choreography) (Light Background)
```

---

**Author:** Vineet Sharma

**Date:** 2026

**Usage:** Copy any prompt above into Google Gemini (or any image generation tool that supports detailed prompts) to generate consistent, professional AWS-style diagrams with **light backgrounds** for the Kafka Design Patterns series.