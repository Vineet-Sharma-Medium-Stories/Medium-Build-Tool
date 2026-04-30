# Dev Setup: SignalR with .NET 10 API - Spotify Clone With Flutter And .NET 10

## Complete Development Environment Setup for .NET 10 Backend with Azure Deployment
[Flutter And .NET 10/images/Spotify-Clone-Flutter-NET-4](images/Spotify-Clone-Flutter-NET-4)
**Subtitle:** *Step-by-step guide to setting up your .NET 10 development environment, configuring SignalR, PostgreSQL, Redis, and deploying to Azure App Service with enterprise-grade features*

**Reference:** This setup guide works with the front-end environment described in **"Dev Setup: Real-time UI on Android + iOS with SignalR - Spotify Clone With Flutter And .NET 10"**. For complete Flutter setup including OAuth, SignalR client, and mobile deployment, please refer to the companion guide.

---

## Table of Contents (as paragraphs for flow)

This comprehensive backend development environment guide covers everything from installing .NET 10 SDK and configuring your development machine to deploying a production-ready SignalR-based API to Azure. You will learn how to set up PostgreSQL for analytics data storage, Redis for distributed caching and SignalR backplane, configure JWT authentication with Spotify OAuth, implement all 46 API endpoints with proper rate limiting using the new Token Bucket algorithm in .NET 10, set up background services for real-time polling, configure Docker containers for local development, and finally deploy to Azure App Service with Redis Cache, PostgreSQL Flexible Server, and Application Insights monitoring. The guide includes detailed troubleshooting sections for common issues like WebSocket connection failures, rate limiting misconfigurations, and SignalR scaling problems, as well as performance optimization checklists for NativeAOT compilation and Redis backplane configuration.

---

## Part 1: .NET 10 Development Environment Setup

### 1.1 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **OS** | Windows 10 64-bit / macOS 12 / Linux Ubuntu 22.04 | Windows 11 / macOS 14 / Ubuntu 24.04 |
| **RAM** | 8 GB | 16 GB or more |
| **Storage** | 20 GB free | 50 GB SSD |
| **CPU** | 4 cores | 8 cores |
| **Docker** | Docker Desktop 4.25+ | Docker Desktop with Kubernetes |

### 1.2 Installing .NET 10 SDK

**Windows Installation:**

```powershell
# Download .NET 10 SDK from official site
# https://dotnet.microsoft.com/en-us/download/dotnet/10.0

# Or use winget
winget install Microsoft.DotNet.SDK.10

# Verify installation
dotnet --version
dotnet --list-sdks
dotnet --list-runtimes

# Install additional workloads
dotnet workload install wasm-tools
dotnet workload install aspnet-core
```

**macOS Installation:**

```bash
# Using Homebrew
brew install --cask dotnet-sdk

# Or download from official site
wget https://download.visualstudio.microsoft.com/download/pr/xyz/dotnet-sdk-10.0.100-osx-x64.pkg
sudo installer -pkg dotnet-sdk-10.0.100-osx-x64.pkg -target /

# Verify
dotnet --info

# Install additional workloads
dotnet workload update
dotnet workload install microsoft-net-runtime-mono-tooling
```

**Linux Installation (Ubuntu/Debian):**

```bash
# Add Microsoft package repository
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb

# Install .NET 10 SDK
sudo apt-get update
sudo apt-get install -y dotnet-sdk-10.0

# Verify
dotnet --info

# Install EF Core tools
dotnet tool install --global dotnet-ef

# Install dev certificates for HTTPS
dotnet dev-certs https --trust
```

### 1.3 Installing Development Tools

**Visual Studio 2022 (Windows):**
```bash
# Install Visual Studio 2022 with workloads:
# - ASP.NET and web development
# - .NET desktop development
# - Azure development
# - Data storage and processing

# Or use VS Code with extensions
code --install-extension ms-dotnettools.csharp
code --install-extension ms-dotnettools.csdevkit
code --install-extension k--kato.docomment
```

**JetBrains Rider (Cross-platform):**
```bash
# Download from https://www.jetbrains.com/rider/
# Enable plugins:
# - .NET Core Debugger
# - Azure Toolkit
# - Database Tools and SQL
# - HTTP Client
```

### 1.4 Installing Docker Desktop

```bash
# Windows: Download from https://www.docker.com/products/docker-desktop
# Enable WSL2 backend for better performance

# macOS: brew install --cask docker

# Linux
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Verify installation
docker --version
docker-compose --version

# Pull required images
docker pull postgres:16-alpine
docker pull redis:7-alpine
docker pull seq:latest
docker pull mcr.microsoft.com/dotnet/sdk:10.0-preview
```

---

## Part 2: Project Initialization

### 2.1 Create New .NET 10 Project

```bash
# Create solution directory
mkdir SpotifyAPI
cd SpotifyAPI

# Create solution file
dotnet new sln -n SpotifyAPI

# Create Web API project
dotnet new webapi -n SpotifyAPI -f net10.0 --use-minimal-apis --no-https

# Add project to solution
dotnet sln add SpotifyAPI/SpotifyAPI.csproj

# Create class library for shared models
dotnet new classlib -n SpotifyAPI.Models -f net10.0
dotnet sln add SpotifyAPI.Models/SpotifyAPI.Models.csproj

# Create test project
dotnet new xunit -n SpotifyAPI.Tests -f net10.0
dotnet sln add SpotifyAPI.Tests/SpotifyAPI.Tests.csproj

# Add project references
dotnet add SpotifyAPI/SpotifyAPI.csproj reference SpotifyAPI.Models/SpotifyAPI.Models.csproj
dotnet add SpotifyAPI.Tests/SpotifyAPI.Tests.csproj reference SpotifyAPI/SpotifyAPI.csproj
```

### 2.2 Configure Project File for .NET 10

**SpotifyAPI/SpotifyAPI.csproj:**

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <InvariantGlobalization>false</InvariantGlobalization>
    
    <!-- NativeAOT Configuration -->
    <PublishAot>true</PublishAot>
    <PublishSingleFile>true</PublishSingleFile>
    <PublishTrimmed>true</PublishTrimmed>
    <TrimMode>partial</TrimMode>
    <SuppressTrimAnalysisWarnings>false</SuppressTrimAnalysisWarnings>
    
    <!-- Optimization -->
    <OptimizationPreference>Speed</OptimizationPreference>
    <StackTraceSupport>true</StackTraceSupport>
    
    <!-- Docker Support -->
    <DockerDefaultTargetOS>Linux</DockerDefaultTargetOS>
    <ContainerRuntimeIdentifier>linux-x64</ContainerRuntimeIdentifier>
    
    <!-- Versioning -->
    <Version>2.0.0</Version>
    <Authors>Your Company</Authors>
    <Description>Spotify Analytics API with SignalR</Description>
    
    <!-- Enable HTTP/3 -->
    <EnableHttp3>true</EnableHttp3>
  </PropertyGroup>
  
  <ItemGroup>
    <PackageReference Include="Microsoft.AspNetCore.Authentication.JwtBearer" Version="10.0.0-preview.3.*" />
    <PackageReference Include="Microsoft.AspNetCore.OpenApi" Version="10.0.0-preview.3.*" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.Design" Version="10.0.0-preview.3.*" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.Tools" Version="10.0.0-preview.3.*" />
    <PackageReference Include="Microsoft.Extensions.Caching.StackExchangeRedis" Version="10.0.0-preview.3.*" />
    <PackageReference Include="Microsoft.Extensions.Diagnostics.HealthChecks" Version="10.0.0-preview.3.*" />
    <PackageReference Include="Microsoft.Extensions.Http.Polly" Version="10.0.0-preview.3.*" />
    <PackageReference Include="Npgsql.EntityFrameworkCore.PostgreSQL" Version="10.0.0-preview.1.*" />
    <PackageReference Include="Polly" Version="8.4.1" />
    <PackageReference Include="Serilog.AspNetCore" Version="8.0.1" />
    <PackageReference Include="Serilog.Sinks.Seq" Version="7.0.1" />
    <PackageReference Include="Swashbuckle.AspNetCore" Version="6.6.2" />
    <PackageReference Include="Hellang.Middleware.ProblemDetails" Version="6.5.1" />
    <PackageReference Include="Microsoft.AspNetCore.SignalR.StackExchangeRedis" Version="10.0.0-preview.3.*" />
  </ItemGroup>
</Project>
```

### 2.3 Configure appsettings.json

**appsettings.json:**

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning",
      "Microsoft.AspNetCore.SignalR": "Debug",
      "Microsoft.AspNetCore.Http.Connections": "Debug"
    }
  },
  "Jwt": {
    "Key": "your-super-secret-key-minimum-32-characters-long!",
    "Issuer": "SpotifyAPI",
    "Audience": "SpotifyMobileApp",
    "ExpiryMinutes": 60
  },
  "Spotify": {
    "ClientId": "YOUR_SPOTIFY_CLIENT_ID",
    "ClientSecret": "YOUR_SPOTIFY_CLIENT_SECRET",
    "RedirectUri": "https://api.yourdomain.com/auth/callback"
  },
  "RateLimiting": {
    "Global": {
      "TokenLimit": 100,
      "ReplenishmentPeriod": "00:01:00",
      "TokensPerPeriod": 100
    },
    "SpotifyAPI": {
      "TokenLimit": 30,
      "QueueLimit": 5,
      "ReplenishmentPeriod": "00:01:00",
      "TokensPerPeriod": 30
    }
  },
  "SignalR": {
    "KeepAliveInterval": "00:00:15",
    "ClientTimeoutInterval": "00:00:30",
    "HandshakeTimeout": "00:00:15",
    "MaxReceiveMessageSize": 102400
  },
  "AllowedHosts": "*"
}
```

**appsettings.Development.json:**

```json
{
  "ConnectionStrings": {
    "PostgreSQL": "Host=localhost;Database=spotify_db;Username=postgres;Password=postgres",
    "Redis": "localhost:6379"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Debug",
      "Microsoft.AspNetCore": "Debug",
      "Microsoft.EntityFrameworkCore": "Debug"
    }
  },
  "Seq": {
    "ServerUrl": "http://localhost:5341"
  }
}
```

**appsettings.Production.json:**

```json
{
  "ConnectionStrings": {
    "PostgreSQL": "Host=spotify-db.postgres.database.azure.com;Database=spotify_db;Username=spotify@spotify-db;Password=${DB_PASSWORD}",
    "Redis": "spotify-cache.redis.cache.windows.net:6380,password=${REDIS_PASSWORD},ssl=True,abortConnect=False"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Warning",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "Seq": {
    "ServerUrl": "http://seq:5341"
  }
}
```

---

## Part 3: Docker-Compose for Local Development

**docker-compose.yml:**

```yaml
version: '3.8'

services:
  api:
    image: mcr.microsoft.com/dotnet/sdk:10.0-preview
    container_name: spotify-api-dev
    ports:
      - "8080:8080"
      - "8081:8081"
    environment:
      - ASPNETCORE_ENVIRONMENT=Development
      - ASPNETCORE_URLS=http://+:8080;https://+:8081
      - ASPNETCORE_Kestrel__Certificates__Default__Path=/https/aspnetapp.pfx
      - ASPNETCORE_Kestrel__Certificates__Default__Password=password
    volumes:
      - .:/src
      - ~/.aspnet/https:/https:ro
      - ~/.microsoft/usersecrets:/root/.microsoft/usersecrets:ro
    working_dir: /src/SpotifyAPI
    command: dotnet watch run --no-launch-profile
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started
      seq:
        condition: service_started
    networks:
      - spotify-network

  postgres:
    image: postgres:16-alpine
    container_name: spotify-postgres-dev
    environment:
      - POSTGRES_DB=spotify_db
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-db.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - spotify-network

  redis:
    image: redis:7-alpine
    container_name: spotify-redis-dev
    command: redis-server --appendonly yes --requirepass redispass
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - spotify-network

  seq:
    image: datalust/seq:latest
    container_name: spotify-seq-dev
    environment:
      - ACCEPT_EULA=Y
    ports:
      - "5341:80"
    volumes:
      - seq_data:/data
    networks:
      - spotify-network

  pgadmin:
    image: dpage/pgadmin4:latest
    container_name: spotify-pgadmin-dev
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@admin.com
      - PGADMIN_DEFAULT_PASSWORD=admin
    ports:
      - "5050:80"
    depends_on:
      - postgres
    networks:
      - spotify-network

networks:
  spotify-network:
    driver: bridge

volumes:
  postgres_data:
  redis_data:
  seq_data:
```

**docker-compose.prod.yml:**

```yaml
version: '3.8'

services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    image: spotifyapi:latest
    ports:
      - "8080:8080"
    environment:
      - ASPNETCORE_ENVIRONMENT=Production
    restart: always
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      replicas: 3
      resources:
        limits:
          memory: 256M
          cpus: '0.5'
      update_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure

  nginx:
    image: nginx:alpine
    container_name: spotify-nginx-prod
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - api
    restart: always
```

---

## Part 4: Database Setup with Entity Framework

### 4.1 Create ApplicationDbContext

```csharp
// Data/ApplicationDbContext.cs
using Microsoft.EntityFrameworkCore;
using SpotifyAPI.Models;

namespace SpotifyAPI.Data;

public class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }
    
    public DbSet<UserProfile> UserProfiles { get; set; }
    public DbSet<ListeningHistoryEntry> ListeningHistory { get; set; }
    public DbSet<Friendship> Friendships { get; set; }
    public DbSet<UserAchievement> UserAchievements { get; set; }
    public DbSet<HourlyAnalytics> HourlyAnalytics { get; set; }
    public DbSet<DailyListeningStats> DailyListeningStats { get; set; }
    public DbSet<GenrePreference> GenrePreferences { get; set; }
    
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);
        
        // UserProfile configuration
        modelBuilder.Entity<UserProfile>(entity =>
        {
            entity.HasKey(e => e.Id);
            entity.HasIndex(e => e.Email).IsUnique();
            entity.Property(e => e.DisplayName).HasMaxLength(100);
            entity.Property(e => e.Email).HasMaxLength(200);
        });
        
        // ListeningHistory configuration
        modelBuilder.Entity<ListeningHistoryEntry>(entity =>
        {
            entity.HasKey(e => e.Id);
            entity.HasIndex(e => new { e.UserId, e.PlayedAt });
            entity.HasIndex(e => e.TrackId);
            entity.Property(e => e.TrackName).HasMaxLength(200);
            entity.Property(e => e.ArtistName).HasMaxLength(200);
        });
        
        // Friendship configuration
        modelBuilder.Entity<Friendship>(entity =>
        {
            entity.HasKey(e => e.Id);
            entity.HasIndex(e => new { e.UserId, e.FriendId }).IsUnique();
            entity.Property(e => e.Status).HasMaxLength(20);
        });
        
        // UserAchievement configuration
        modelBuilder.Entity<UserAchievement>(entity =>
        {
            entity.HasKey(e => e.Id);
            entity.HasIndex(e => new { e.UserId, e.AchievementType });
        });
        
        // HourlyAnalytics configuration
        modelBuilder.Entity<HourlyAnalytics>(entity =>
        {
            entity.HasKey(e => e.Id);
            entity.HasIndex(e => e.Hour);
        });
    }
}

public class ListeningHistoryEntry
{
    public long Id { get; set; }
    public string UserId { get; set; } = string.Empty;
    public string TrackId { get; set; } = string.Empty;
    public string TrackName { get; set; } = string.Empty;
    public string ArtistName { get; set; } = string.Empty;
    public DateTime PlayedAt { get; set; }
    public int DurationMs { get; set; }
    public bool IsSkipped { get; set; }
}

public class Friendship
{
    public long Id { get; set; }
    public string UserId { get; set; } = string.Empty;
    public string FriendId { get; set; } = string.Empty;
    public string Status { get; set; } = "pending"; // pending, accepted, blocked
    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    public DateTime? AcceptedAt { get; set; }
}

public class UserAchievement
{
    public long Id { get; set; }
    public string UserId { get; set; } = string.Empty;
    public string AchievementType { get; set; } = string.Empty;
    public int Progress { get; set; }
    public bool IsCompleted { get; set; }
    public DateTime EarnedAt { get; set; }
}

public class HourlyAnalytics
{
    public long Id { get; set; }
    public DateTime Hour { get; set; }
    public int TotalTracksPlayed { get; set; }
    public int UniqueUsers { get; set; }
    public double AverageDanceability { get; set; }
    public double AverageEnergy { get; set; }
    public double AverageValence { get; set; }
}

public class DailyListeningStats
{
    public long Id { get; set; }
    public string UserId { get; set; } = string.Empty;
    public DateTime Date { get; set; }
    public int TotalTracksPlayed { get; set; }
    public int TotalMinutesListened { get; set; }
    public int UniqueArtistsCount { get; set; }
    public string TopGenre { get; set; } = string.Empty;
    public string TopTrackId { get; set; } = string.Empty;
    public string TopArtistId { get; set; } = string.Empty;
}

public class GenrePreference
{
    public long Id { get; set; }
    public string UserId { get; set; } = string.Empty;
    public string Genre { get; set; } = string.Empty;
    public int PlayCount { get; set; }
    public DateTime LastPlayedAt { get; set; }
}
```

### 4.2 Configure Entity Framework

```bash
# Install EF Core tools (if not already)
dotnet tool install --global dotnet-ef

# Add migrations
dotnet ef migrations add InitialCreate --context ApplicationDbContext --output-dir Data/Migrations

# Create specific migrations
dotnet ef migrations add AddUserProfileFields --context ApplicationDbContext
dotnet ef migrations add AddAnalyticsTables --context ApplicationDbContext

# Apply migrations to database
dotnet ef database update --context ApplicationDbContext

# Generate SQL script for migrations
dotnet ef migrations script --context ApplicationDbContext -o migrations.sql

# Remove last migration (if needed)
dotnet ef migrations remove --context ApplicationDbContext
```

### 4.3 Seed Data Configuration

```csharp
// Data/SeedData.cs
using Microsoft.EntityFrameworkCore;
using SpotifyAPI.Models;

namespace SpotifyAPI.Data;

public static class SeedData
{
    public static async Task InitializeAsync(IServiceProvider serviceProvider)
    {
        using var scope = serviceProvider.CreateScope();
        var context = scope.ServiceProvider.GetRequiredService<ApplicationDbContext>();
        
        await context.Database.MigrateAsync();
        
        if (!await context.UserProfiles.AnyAsync())
        {
            // Seed initial data if needed
            await SeedUsers(context);
        }
        
        if (!await context.GenrePreferences.AnyAsync())
        {
            await SeedGenres(context);
        }
        
        await context.SaveChangesAsync();
    }
    
    private static async Task SeedUsers(ApplicationDbContext context)
    {
        // Seed admin user for testing
        var adminUser = new UserProfile
        {
            Id = "admin123",
            DisplayName = "Admin User",
            Email = "admin@spotifyanalytics.com",
            Product = "premium",
            Followers = 0,
            Country = "US"
        };
        
        await context.UserProfiles.AddAsync(adminUser);
    }
    
    private static async Task SeedGenres(ApplicationDbContext context)
    {
        var defaultGenres = new[]
        {
            "pop", "rock", "hip-hop", "electronic", "jazz", "classical",
            "indie", "folk", "metal", "reggae", "blues", "country",
            "r&b", "soul", "funk", "disco", "house", "techno",
            "trance", "dubstep", "drum-and-bass", "ambient"
        };
        
        foreach (var genre in defaultGenres)
        {
            await context.GenrePreferences.AddAsync(new GenrePreference
            {
                UserId = "system",
                Genre = genre,
                PlayCount = 0,
                LastPlayedAt = DateTime.UtcNow
            });
        }
    }
}
```

---

## Part 5: Running the Application

### 5.1 Run Locally with Docker Compose

```bash
# Start all services
docker-compose up -d

# Build and start
docker-compose up --build

# View logs
docker-compose logs -f api

# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### 5.2 Run with .NET CLI

```bash
# Set environment
export ASPNETCORE_ENVIRONMENT=Development

# Run the API
dotnet run --project SpotifyAPI/SpotifyAPI.csproj

# Watch for changes (hot reload)
dotnet watch run --project SpotifyAPI/SpotifyAPI.csproj

# Run with specific launch profile
dotnet run --launch-profile Development

# Run with environment variables
dotnet run --environment Development
```

### 5.3 Test API Endpoints

```bash
# Health check
curl https://localhost:8080/health

# Get API info
curl https://localhost:8080/

# Test SignalR hub with PowerShell (Windows)
$hubUrl = "https://localhost:8080/hubs/spotify"
Invoke-WebRequest -Uri $hubUrl -Method Get

# Test SignalR hub with curl (requires websocat)
websocat wss://localhost:8080/hubs/spotify -H "Authorization:Bearer YOUR_TOKEN"
```

### 5.4 Debugging with Visual Studio Code

**.vscode/launch.json:**

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": ".NET Core Launch (web)",
      "type": "coreclr",
      "request": "launch",
      "preLaunchTask": "build",
      "program": "${workspaceFolder}/SpotifyAPI/bin/Debug/net10.0/SpotifyAPI.dll",
      "args": [],
      "cwd": "${workspaceFolder}/SpotifyAPI",
      "stopAtEntry": false,
      "serverReadyAction": {
        "action": "openExternally",
        "pattern": "\\bNow listening on:\\s+(https?://\\S+)"
      },
      "env": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      },
      "sourceFileMap": {
        "/Views": "${workspaceFolder}/Views"
      }
    },
    {
      "name": ".NET Core Attach",
      "type": "coreclr",
      "request": "attach"
    }
  ]
}
```

**.vscode/tasks.json:**

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build",
      "command": "dotnet",
      "type": "process",
      "args": [
        "build",
        "${workspaceFolder}/SpotifyAPI/SpotifyAPI.csproj",
        "/property:GenerateFullPaths=true",
        "/consoleloggerparameters:NoSummary"
      ],
      "problemMatcher": "$msCompile"
    },
    {
      "label": "publish",
      "command": "dotnet",
      "type": "process",
      "args": [
        "publish",
        "${workspaceFolder}/SpotifyAPI/SpotifyAPI.csproj",
        "-c",
        "Release",
        "-o",
        "${workspaceFolder}/publish"
      ],
      "problemMatcher": "$msCompile"
    },
    {
      "label": "watch",
      "command": "dotnet",
      "type": "process",
      "args": [
        "watch",
        "run",
        "--project",
        "${workspaceFolder}/SpotifyAPI/SpotifyAPI.csproj"
      ],
      "problemMatcher": "$msCompile"
    }
  ]
}
```

---

## Part 6: Azure Deployment

### 6.1 Create Azure Resources

```bash
# Login to Azure
az login

# Set subscription
az account set --subscription "Your Subscription Name"

# Create resource group
az group create \
  --name SpotifyAnalyticsRG \
  --location eastus \
  --tags Environment=Production Project=SpotifyAnalytics

# Create App Service Plan (Linux with NativeAOT support)
az appservice plan create \
  --name SpotifyPlan \
  --resource-group SpotifyAnalyticsRG \
  --sku P1V3 \
  --is-linux \
  --location eastus \
  --number-of-workers 3

# Create Web App for .NET 10
az webapp create \
  --name spotify-api-${RANDOM} \
  --resource-group SpotifyAnalyticsRG \
  --plan SpotifyPlan \
  --runtime "DOTNET:10.0"
```

### 6.2 Configure Azure PostgreSQL Flexible Server

```bash
# Create PostgreSQL server
az postgres flexible-server create \
  --name spotify-db-${RANDOM} \
  --resource-group SpotifyAnalyticsRG \
  --location eastus \
  --admin-user spotifyadmin \
  --admin-password $(openssl rand -base64 32) \
  --sku-name Standard_B2s \
  --tier Burstable \
  --version 16 \
  --storage-size 128 \
  --backup-retention 30 \
  --geo-redundant-backup Enabled \
  --high-availability Enabled \
  --zone 1 \
  --standby-zone 3

# Create database
az postgres flexible-server db create \
  --server-name spotify-db \
  --resource-group SpotifyAnalyticsRG \
  --database-name spotify_db

# Configure firewall rules
az postgres flexible-server firewall-rule create \
  --server-name spotify-db \
  --resource-group SpotifyAnalyticsRG \
  --name AllowAzureServices \
  --start-ip-address 0.0.0.0 \
  --end-ip-address 0.0.0.0

# Get connection string
az postgres flexible-server show-connection-string \
  --server-name spotify-db \
  --resource-group SpotifyAnalyticsRG \
  --admin-user spotifyadmin \
  --ssl true
```

### 6.3 Configure Azure Redis Cache

```bash
# Create Redis Cache (Premium for clustering)
az redis create \
  --name spotify-cache-${RANDOM} \
  --resource-group SpotifyAnalyticsRG \
  --location eastus \
  --sku Premium \
  --vm-size P1 \
  --enable-non-ssl-port false \
  --redis-configuration maxmemory-policy=allkeys-lru \
  --redis-configuration notify-keyspace-events=Ex \
  --shard-count 3

# Enable clustering
az redis update \
  --name spotify-cache \
  --resource-group SpotifyAnalyticsRG \
  --set enableNonSslPort=false

# Get Redis connection string
az redis list-keys \
  --name spotify-cache \
  --resource-group SpotifyAnalyticsRG \
  --query "{Primary:primaryKey, Secondary:secondaryKey}"
```

### 6.4 Configure Application Insights

```bash
# Create Application Insights
az monitor app-insights component create \
  --app spotify-analytics-insights \
  --resource-group SpotifyAnalyticsRG \
  --location eastus \
  --application-type web \
  --kind web

# Get instrumentation key
INSTRUMENTATION_KEY=$(az monitor app-insights component show \
  --app spotify-analytics-insights \
  --resource-group SpotifyAnalyticsRG \
  --query instrumentationKey \
  --output tsv)

echo "Instrumentation Key: $INSTRUMENTATION_KEY"

# Configure continuous export (optional)
az monitor app-insights component update \
  --app spotify-analytics-insights \
  --resource-group SpotifyAnalyticsRG \
  --set ingestionMode=LogAnalytics
```

### 6.5 Set Application Settings

```bash
# Generate JWT key
JWT_KEY=$(openssl rand -base64 32)
echo "JWT Key: $JWT_KEY"

# Set all app settings
az webapp config appsettings set \
  --name spotify-api-prod \
  --resource-group SpotifyAnalyticsRG \
  --settings \
    ASPNETCORE_ENVIRONMENT=Production \
    ASPNETCORE_HTTP_PORTS=8080 \
    Jwt__Key="$JWT_KEY" \
    Jwt__Issuer="SpotifyAPI" \
    Jwt__Audience="SpotifyMobileApp" \
    ConnectionStrings__PostgreSQL="Host=spotify-db.postgres.database.azure.com;Database=spotify_db;Username=spotifyadmin;Password=${DB_PASSWORD};Ssl Mode=Require;Trust Server Certificate=false" \
    ConnectionStrings__Redis="spotify-cache.redis.cache.windows.net:6380,password=${REDIS_PASSWORD},ssl=True,abortConnect=False" \
    APPLICATIONINSIGHTS_CONNECTION_STRING="InstrumentationKey=${INSTRUMENTATION_KEY};IngestionEndpoint=https://eastus-1.in.applicationinsights.azure.com/" \
    Serilog__WriteTo__Seq__ServerUrl="http://seq:5341" \
    SignalR__KeepAliveInterval="00:00:15" \
    SignalR__ClientTimeoutInterval="00:00:30" \
    ENABLE_NATIVE_AOT="true" \
    WEBSITE_RUN_FROM_PACKAGE="1"
```

### 6.6 Configure Auto-Scaling

```bash
# Create auto-scale settings
az monitor autoscale create \
  --resource-group SpotifyAnalyticsRG \
  --resource spotify-api-prod \
  --resource-type Microsoft.Web/sites \
  --name spotify-auto-scale \
  --min-count 2 \
  --max-count 10 \
  --count 2

# Add scale rules
az monitor autoscale rule create \
  --resource-group SpotifyAnalyticsRG \
  --autoscale-name spotify-auto-scale \
  --scale out \
  --condition "Percentage CPU > 75 for 5 minutes" \
  --cooldown 5 \
  --type ChangeCount \
  --value 1

az monitor autoscale rule create \
  --resource-group SpotifyAnalyticsRG \
  --autoscale-name spotify-auto-scale \
  --scale in \
  --condition "Percentage CPU < 30 for 10 minutes" \
  --cooldown 10 \
  --type ChangeCount \
  --value 1

# Add memory-based scaling
az monitor autoscale rule create \
  --resource-group SpotifyAnalyticsRG \
  --autoscale-name spotify-auto-scale \
  --scale out \
  --condition "Memory Percentage > 80 for 5 minutes" \
  --cooldown 5 \
  --type ChangeCount \
  --value 1
```

### 6.7 Configure Custom Domain and SSL

```bash
# Add custom domain
az webapp config hostname add \
  --webapp-name spotify-api-prod \
  --resource-group SpotifyAnalyticsRG \
  --hostname api.yourdomain.com

# Upload SSL certificate
az webapp config ssl upload \
  --name spotify-api-prod \
  --resource-group SpotifyAnalyticsRG \
  --certificate-file certificate.pfx \
  --certificate-password "your-password"

# Bind SSL certificate to domain
az webapp config ssl bind \
  --certificate-thumbprint "your-thumbprint" \
  --ssl-type SNI \
  --name spotify-api-prod \
  --resource-group SpotifyAnalyticsRG

# Enable HTTPS only
az webapp update \
  --name spotify-api-prod \
  --resource-group SpotifyAnalyticsRG \
  --set httpsOnly=true

# Enable TLS 1.2 and TLS 1.3 only
az webapp config set \
  --name spotify-api-prod \
  --resource-group SpotifyAnalyticsRG \
  --min-tls-version 1.2
```

### 6.8 Configure Azure DevOps CI/CD Pipeline

**azure-pipelines.yml:**

```yaml
trigger:
  branches:
    include:
    - main
    - develop
  paths:
    include:
    - SpotifyAPI/*
    - docker-compose.yml

pool:
  vmImage: 'ubuntu-latest'

variables:
  buildConfiguration: 'Release'
  dotnetVersion: '10.0.x'
  azureSubscription: 'Azure-Service-Connection'
  appName: 'spotify-api-prod'
  resourceGroup: 'SpotifyAnalyticsRG'

stages:
  - stage: Build
    displayName: 'Build Stage'
    jobs:
      - job: Build
        displayName: 'Build and Test'
        steps:
          - task: UseDotNet@2
            inputs:
              version: '$(dotnetVersion)'
              
          - task: DotNetCoreCLI@2
            displayName: 'Restore packages'
            inputs:
              command: 'restore'
              projects: '**/*.csproj'
              
          - task: DotNetCoreCLI@2
            displayName: 'Build solution'
            inputs:
              command: 'build'
              projects: '**/*.csproj'
              arguments: '--configuration $(buildConfiguration) --no-restore'
              
          - task: DotNetCoreCLI@2
            displayName: 'Run unit tests'
            inputs:
              command: 'test'
              projects: '**/*.Tests.csproj'
              arguments: '--configuration $(buildConfiguration) --collect:"XPlat Code Coverage"'
              
          - task: DotNetCoreCLI@2
            displayName: 'Publish with NativeAOT'
            inputs:
              command: 'publish'
              publishWebProjects: true
              arguments: '--configuration $(buildConfiguration) --self-contained true -p:PublishSingleFile=true -p:PublishTrimmed=true -o $(Build.ArtifactStagingDirectory)'
              zipAfterPublish: true
              
          - task: PublishBuildArtifacts@1
            displayName: 'Publish artifacts'
            inputs:
              PathtoPublish: '$(Build.ArtifactStagingDirectory)'
              ArtifactName: 'drop'

  - stage: Deploy
    displayName: 'Deploy Stage'
    dependsOn: Build
    condition: succeeded()
    jobs:
      - deployment: DeployToAzure
        displayName: 'Deploy to Azure'
        environment: 'production'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebApp@1
                  displayName: 'Deploy to Azure App Service'
                  inputs:
                    azureSubscription: '$(azureSubscription)'
                    appType: 'webAppLinux'
                    appName: '$(appName)'
                    package: '$(Pipeline.Workspace)/drop/*.zip'
                    runtimeStack: 'DOTNET|10.0'
                    
                - task: AzureAppServiceManage@0
                  displayName: 'Restart App Service'
                  inputs:
                    azureSubscription: '$(azureSubscription)'
                    Action: 'Restart'
                    WebAppName: '$(appName)'
                    
                - task: AzureCLI@2
                  displayName: 'Run database migrations'
                  inputs:
                    azureSubscription: '$(azureSubscription)'
                    scriptType: 'bash'
                    scriptLocation: 'inlineScript'
                    inlineScript: |
                      az webapp ssh --name $(appName) --resource-group $(resourceGroup) --command "dotnet ef database update"
```

### 6.9 Configure Azure Monitoring and Alerts

```bash
# Create CPU alert
az monitor metrics alert create \
  --name "API-High-CPU" \
  --resource-group SpotifyAnalyticsRG \
  --scopes "/subscriptions/$(az account show --query id -o tsv)/resourceGroups/SpotifyAnalyticsRG/providers/Microsoft.Web/sites/spotify-api-prod" \
  --condition "avg Percentage CPU > 80" \
  --description "Alert when CPU usage exceeds 80%" \
  --evaluation-frequency 5m \
  --window-size 15m \
  --severity 2 \
  --action-group $(az monitor action-group create --name SpotifyAlertGroup --resource-group SpotifyAnalyticsRG --short-name SpotifyAlerts --query id -o tsv)

# Create memory alert
az monitor metrics alert create \
  --name "API-High-Memory" \
  --resource-group SpotifyAnalyticsRG \
  --scopes "/subscriptions/$(az account show --query id -o tsv)/resourceGroups/SpotifyAnalyticsRG/providers/Microsoft.Web/sites/spotify-api-prod" \
  --condition "avg Memory Percentage > 85" \
  --description "Alert when memory usage exceeds 85%" \
  --evaluation-frequency 5m \
  --window-size 15m \
  --severity 2

# Create error rate alert
az monitor metrics alert create \
  --name "API-High-Error-Rate" \
  --resource-group SpotifyAnalyticsRG \
  --scopes "/subscriptions/$(az account show --query id -o tsv)/resourceGroups/SpotifyAnalyticsRG/providers/Microsoft.Web/sites/spotify-api-prod" \
  --condition "count Http5xx > 10" \
  --description "Alert when 5xx errors exceed 10 in 5 minutes" \
  --evaluation-frequency 5m \
  --window-size 5m \
  --severity 1

# Create SignalR connection alert
az monitor metrics alert create \
  --name "SignalR-Connection-Drop" \
  --resource-group SpotifyAnalyticsRG \
  --scopes "/subscriptions/$(az account show --query id -o tsv)/resourceGroups/SpotifyAnalyticsRG/providers/Microsoft.Web/sites/spotify-api-prod" \
  --condition "count ConnectionsClosed > 100" \
  --description "Alert when SignalR connections drop significantly" \
  --evaluation-frequency 5m \
  --window-size 10m \
  --severity 2
```

---

## Part 7: Load Testing

### 7.1 k6 Load Test Script

**load-test.js:**

```javascript
import http from 'k6/http';
import { sleep, check } from 'k6';
import ws from 'k6/ws';

export const options = {
  stages: [
    { duration: '2m', target: 100 },  // Ramp up to 100 users
    { duration: '5m', target: 100 },  // Stay at 100 users
    { duration: '2m', target: 500 },  // Ramp up to 500 users
    { duration: '5m', target: 500 },  // Stay at 500 users
    { duration: '2m', target: 0 },    // Ramp down to 0
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],  // 95% of requests < 500ms
    http_req_failed: ['rate<0.01'],    // Less than 1% error rate
  },
};

const BASE_URL = 'https://api.yourdomain.com';
const TOKEN = 'your-test-token';

export default function () {
  // Test 1: Get current track
  const trackResponse = http.get(`${BASE_URL}/api/player/currently-playing`, {
    headers: {
      'Authorization': `Bearer ${TOKEN}`,
    },
  });
  
  check(trackResponse, {
    'current track status is 200': (r) => r.status === 200,
    'track response time < 200ms': (r) => r.timings.duration < 200,
  });
  
  // Test 2: Get recent tracks
  const recentResponse = http.get(`${BASE_URL}/api/player/recently-played?limit=20`, {
    headers: {
      'Authorization': `Bearer ${TOKEN}`,
    },
  });
  
  check(recentResponse, {
    'recent tracks status is 200': (r) => r.status === 200,
  });
  
  // Test 3: SignalR WebSocket connection
  const wsUrl = `${BASE_URL.replace('https', 'wss')}/hubs/spotify?access_token=${TOKEN}`;
  const wsResponse = ws.connect(wsUrl, {}, (socket) => {
    socket.on('open', () => {
      socket.send(JSON.stringify({
        protocol: 'json',
        version: 1,
      }));
      socket.setTimeout(() => {
        socket.close();
      }, 10000);
    });
    
    socket.on('message', (data) => {
      console.log('WebSocket message received');
    });
  });
  
  sleep(1);
}

// Run with: k6 run --vus 100 --duration 30s load-test.js
```

### 7.2 Run Load Test

```bash
# Install k6
# Windows: choco install k6
# macOS: brew install k6
# Linux: sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69 && echo "deb https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list && sudo apt-get update && sudo apt-get install k6

# Run basic test
k6 run load-test.js

# Run with environment variables
k6 run -e BASE_URL=https://api.yourdomain.com load-test.js

# Run with output to InfluxDB
k6 run --out influxdb=http://localhost:8086/k6 load-test.js

# Run with Cloud execution
k6 cloud load-test.js
```

---

## Part 8: Troubleshooting Guide

### 8.1 Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| **SignalR connections dropping** | Check WebSocket settings: `az webapp config set --web-sockets-enabled true` |
| **Redis connection failed** | Verify firewall rules and connection string: `az redis show --name spotify-cache` |
| **Database connection timeout** | Increase connection pool size in connection string: `Pooling=true;MaxPoolSize=100` |
| **NativeAOT compilation error** | Add missing annotations: `[DynamicDependency(DynamicallyAccessedMemberTypes.All, typeof(Type))]` |
| **Rate limiting too aggressive** | Adjust token bucket settings in appsettings.json |
| **Memory leak** | Check for unmanaged resources and use `using` statements |

### 8.2 Debugging Commands

```bash
# Check App Service logs
az webapp log tail --name spotify-api-prod --resource-group SpotifyAnalyticsRG

# Check SignalR status
curl -X GET https://api.yourdomain.com/health/signalr

# Check Redis cache stats
az redis show --name spotify-cache --resource-group SpotifyAnalyticsRG --query "redisVersion"

# Check database connections
az postgres flexible-server show --name spotify-db --resource-group SpotifyAnalyticsRG --query "storageProfile"

# Monitor metrics
az monitor metrics list --resource "spotify-api-prod" --resource-group SpotifyAnalyticsRG --resource-type Microsoft.Web/sites --metric "CpuPercentage"

# Check Application Insights
az monitor app-insights query --app spotify-analytics-insights --analytics-query "requests | summarize count() by resultCode"
```

### 8.3 Performance Optimization Commands

```bash
# Enable HTTP/2 and HTTP/3
az webapp config set --http20-enabled true --http20-proxy-enabled true

# Enable Always On
az webapp config set --always-on true

# Configure ARR affinity (required for SignalR)
az webapp config set --client-affinity-enabled true

# Increase instance count
az appservice plan update --name SpotifyPlan --resource-group SpotifyAnalyticsRG --number-of-workers 5

# Configure auto-healing rules
az webapp config set --auto-heal-enabled true --auto-heal-rules @auto-heal.json

# Enable WebSocket compression
az webapp config set --web-sockets-enabled true --web-sockets-compression-enabled true
```

---

## Part 9: Production Readiness Checklist

- [ ] All environment variables configured in Azure App Settings
- [ ] SSL/TLS certificates installed and configured
- [ ] Custom domain added with proper CNAME/DNS records
- [ ] CDN configured for static assets
- [ ] Redis Cache Premium tier with clustering enabled
- [ ] PostgreSQL High Availability configured
- [ ] Application Insights monitoring active with alerts
- [ ] Auto-scaling rules configured with proper metrics
- [ ] Load testing completed with acceptable thresholds
- [ ] Security scanning passed (OWASP ZAP)
- [ ] GDPR compliance verified (data deletion, export)
- [ ] Backup strategy implemented (daily backups)
- [ ] Disaster recovery plan documented
- [ ] API versioning strategy defined
- [ ] Rate limiting tuned for production workloads
- [ ] SignalR connection limits configured
- [ ] Log retention policy set in Application Insights
- [ ] CI/CD pipeline automated and tested
- [ ] Blue-green deployment configured
- [ ] Feature flags implemented for gradual rollouts

---

## Next Steps

This backend development environment setup works with the Flutter front-end described in **"Dev Setup: Real-time UI on Android + iOS with SignalR - Spotify Clone With Flutter And .NET 10"**. For complete Flutter setup including OAuth, SignalR client implementation, and mobile deployment, continue to the companion guide.

**Quick Reference:**

| Command | Purpose |
|---------|---------|
| `docker-compose up -d` | Start local development environment |
| `dotnet watch run` | Run with hot reload |
| `dotnet ef database update` | Apply migrations |
| `az webapp deploy` | Deploy to Azure |
| `k6 run load-test.js` | Run load tests |

**Useful Azure CLI Commands:**
```bash
# List all resources
az resource list --resource-group SpotifyAnalyticsRG

# Get deployment logs
az webapp log deployment show --name spotify-api-prod --resource-group SpotifyAnalyticsRG

# Scale app service plan
az appservice plan update --name SpotifyPlan --resource-group SpotifyAnalyticsRG --number-of-workers 5

# Swap deployment slots
az webapp deployment slot swap --name spotify-api-prod --resource-group SpotifyAnalyticsRG --slot staging --target-slot production
```

**Support Resources:**
- .NET Documentation: https://learn.microsoft.com/en-us/dotnet/
- SignalR Documentation: https://learn.microsoft.com/en-us/aspnet/core/signalr/
- Azure SDK for .NET: https://azure.github.io/azure-sdk-for-net/

---

*Both development environment setup guides are now complete. The front-end and back-end work together to deliver a production-ready real-time Spotify analytics platform on Azure.*