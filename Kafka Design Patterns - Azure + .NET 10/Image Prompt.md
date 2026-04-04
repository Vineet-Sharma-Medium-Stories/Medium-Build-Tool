## Main Prompt

Now create gemini image prompts for all 4 stories and 11 patterns in code block as readme. The images should be in AWS style with light background, infrastructure at background, technology and pattern logos with text. Include title and sub title, all 4 story title starts with "11 Kafka Design Patterns -". Place "Vineet Sharma" at bottom right.

Here is the complete README with **Gemini image prompts** for all 4 Azure stories and all 11 patterns in **Microsoft style with light background**.


# 🎨 Gemini Image Prompts for Kafka Design Patterns Series — Azure + .NET 10 Edition

## Series Title: **11 Kafka Design Patterns for Every Backend Engineer — Azure + .NET 10 Edition**

**Author:** Vineet Sharma (placed at bottom right of all images)

**Style:** Microsoft / Azure documentation style — clean white/light gray background, flat design, blue/purple/teal color palette (Microsoft Fluent Design), Azure service icons, clear text hierarchy, modern tech illustration aesthetic.



## 📸 Cover Image (Series Master Story)

```markdown
Generate a professional Microsoft Azure-style architectural hero image for a technical blog series titled "11 Kafka Design Patterns for Every Backend Engineer — Azure + .NET 10 Edition" with a LIGHT BACKGROUND.

Background: Clean white canvas with a subtle light gray grid pattern. Soft abstract Azure cloud infrastructure outlines in very light blue (#E3F2FD). Azure service icons in Microsoft Fluent Design style (Azure Event Hubs, Cosmos DB, Azure SQL, Blob Storage, Azure Functions, AKS, Durable Functions) in light gray with Microsoft blue (#0078D4) accents. Flowing data streams in Microsoft purple (#5E2B97) and teal (#00A1AB) connecting the services. A large Azure Event Hubs logo centered in the background with data flowing outward like a hub.

Foreground: 11 glowing pattern icons arranged in a circular or grid pattern around the center. Each icon represents a pattern with Microsoft Fluent Design style: Outbox (envelope with database), Idempotent Consumer (checkmark with duplicate symbol), Partition Key (key with ordered list), DLQ (skull with queue), Retry (recycling arrows), Event Sourcing (timeline with events), CQRS (split command/query arrows), Compacted Topic (compressed folder with key), Event Carried State Transfer (package with data), Claim Check (ticket with Blob Storage), Stream-Table (overlapping stream and table), Saga (chain of circles with checkmarks).

Top text in large bold Microsoft blue (#0078D4) font: "11 KAFKA DESIGN PATTERNS". Below in medium dark gray (#5C5C5C) font: "Azure + .NET 10 Edition — For Every Backend Engineer". Bottom right corner: "Vineet Sharma" in small dark gray text.

Overall style: Microsoft Learn / Azure documentation aesthetic, clean whiteboard style, Fluent Design icons, light background, crisp lines, no realistic people, professional diagrammatic look.
```

---

## 📖 Story 1: Overview (All 11 Patterns)

```markdown
Generate a Microsoft Azure-style technical illustration for a blog story titled "11 Kafka Design Patterns - Part 1: Overview of All 11 Patterns" with a LIGHT BACKGROUND.

Background: Clean white canvas with light gray grid. Azure cloud infrastructure diagram with Azure Event Hubs cluster in the center, surrounded by connection lines to other Azure services: Cosmos DB, Azure SQL Database, Blob Storage, Azure Functions, AKS, Application Insights, and Durable Functions. All service icons in Microsoft Fluent Design style (light gray with Microsoft blue outlines). Subtle data flow arrows in Microsoft purple (#5E2B97) and teal (#00A1AB).

Foreground: A large central hub representing Azure Event Hubs with 11 labeled pattern cards radiating outward in a semicircle or wheel arrangement. Each card has a small Fluent Design icon and pattern name on a white card with light gray border and soft shadow: Outbox, Idempotent Consumer, Partition Key, DLQ, Retry, Event Sourcing, CQRS, Compacted Topic, Event Carried State Transfer, Claim Check, Stream-Table Duality, Saga.

Top title text: "11 KAFKA DESIGN PATTERNS" in bold Microsoft blue (#0078D4). Subtitle: "Part 1 — Overview of All 11 Patterns on Azure" in dark gray (#323130). Bottom right corner: "Vineet Sharma" in small dark gray text.

Color scheme: White background (#FFFFFF), light gray grid (#F0F0F0), Microsoft blue (#0078D4), Microsoft purple (#5E2B97), teal (#00A1AB), dark gray text (#323130). Icons should be clean Fluent Design style, similar to Azure architecture diagram icons.
```

---

## 📖 Story 2: Reliability & Ordering Patterns

```markdown
Generate a Microsoft Azure-style technical illustration for a blog story titled "11 Kafka Design Patterns - Part 2: Reliability & Ordering Deep Dive" with a LIGHT BACKGROUND.

Background: Clean white canvas with light gray grid. Azure infrastructure showing Azure Event Hubs, Cosmos DB (for idempotency), Azure SQL Database (for outbox table), Azure Service Bus (for DLQ), and Application Insights alerts. All icons in Microsoft Fluent Design style. Blue and orange connection lines.

Foreground: Five pattern icons prominently displayed in a horizontal or circular arrangement with Microsoft Fluent Design style:

1. Transactional Outbox — Envelope merging into a database cylinder (Azure SQL icon), with green checkmark.
2. Idempotent Consumer — Circular arrow with a checkmark inside, and a duplicate symbol crossed out in red. Cosmos DB icon nearby.
3. Partition Key — A key with ordered list items (1,2,3) flowing into Event Hubs partitions.
4. Dead Letter Queue — A skull icon inside a queue/message box (Service Bus icon), with an alert bell in orange.
5. Retry with Backoff — Clock with curved arrows showing increasing delays (1s, 2s, 4s). Durable Functions icon nearby.

Top title: "11 KAFKA DESIGN PATTERNS" in bold Microsoft blue (#0078D4). Subtitle: "Part 2 — Reliability & Ordering Deep Dive on Azure" in dark orange (#CC5500). Bottom right: "Vineet Sharma".

Color scheme: White background, Microsoft blue text, orange and teal accents for icons. Use green for success paths, red for warnings/duplicates. All icons in Fluent Design style.
```

---

## 📖 Story 3: Data & State Patterns

```markdown
Generate a Microsoft Azure-style technical illustration for a blog story titled "11 Kafka Design Patterns - Part 3: Data & State Deep Dive" with a LIGHT BACKGROUND.

Background: Clean white canvas with light gray grid. Azure infrastructure showing Azure Event Hubs with compacted topic visualization (stack of messages collapsing into one), Cosmos DB for snapshots and materialized views, Azure SQL Database, and Azure Schema Registry. Data lineage arrows in Microsoft purple showing events flowing from producers to storage to materialized views.

Foreground: Four pattern icons prominently displayed in Microsoft Fluent Design style:

1. Event Sourcing — A timeline with event dots leading to a database snapshot (Cosmos DB icon). Icons for "past", "present", "replay" in teal.
2. CQRS — Split design: left side "Command" (pencil/arrow in Microsoft blue), right side "Query" (magnifying glass in green). Connected by Event Hubs in center with purple arrow.
3. Compacted Topic — A folder or database icon with a key, showing only the latest version retained. Old versions fading to light gray.
4. Event Carried State Transfer — An event envelope that is "full" or "bulging" with data, with a "no fetch needed" symbol (crossed-out network icon in red).

Top title: "11 KAFKA DESIGN PATTERNS" in bold Microsoft blue (#0078D4). Subtitle: "Part 3 — Data & State Deep Dive on Azure" in dark teal (#008272). Bottom right: "Vineet Sharma".

Color scheme: White background, Microsoft blue text, teal and green accents. Icons in Fluent Design style with dark blue outlines.
```

---

## 📖 Story 4: Performance & Integration Patterns

```markdown
Generate a Microsoft Azure-style technical illustration for a blog story titled "11 Kafka Design Patterns - Part 4: Performance & Integration Deep Dive" with a LIGHT BACKGROUND.

Background: Clean white canvas with light gray grid. Azure infrastructure showing Azure Event Hubs connected to Blob Storage (for Claim Check — large arrow to Blob Storage icon), AKS containers running Kafka Streams (light gray container icons), Durable Functions workflow for saga orchestration (connected circles), and Azure Stream Analytics for stream-table joins. High-speed data flow lines in Microsoft purple and teal.

Foreground: Three pattern icons prominently displayed in Microsoft Fluent Design style:

1. Claim Check — A ticket or claim stub with Azure Blob Storage icon. Visual of large file (red) going to Blob Storage, small reference (green) going to Event Hubs.
2. Stream-Table Duality — Overlapping icons: a flowing stream (blue wave lines) and a stable table (green grid). Azure Stream Analytics or AKS icon in center.
3. Saga (Choreography) — A chain of connected circles, each with a checkmark or cross. Durable Functions icon nearby. Compensating arrows looping back in red.

Top title: "11 KAFKA DESIGN PATTERNS" in bold Microsoft blue (#0078D4). Subtitle: "Part 4 — Performance & Integration Deep Dive on Azure" in dark orange (#CC5500). Bottom right: "Vineet Sharma".

Color scheme: White background, Microsoft blue text, bright cyan and orange accents. Icons in Fluent Design style with arrow flows in teal.
```

---

## 🎯 Individual Pattern Images (12 total) — Microsoft Style Light Background

### 1. Transactional Outbox Pattern

```markdown
Generate a Microsoft Azure-style technical diagram for the "Transactional Outbox" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. Left side shows an application service icon (Microsoft blue) writing to an Azure SQL Database cylinder (light gray with dark blue outline). Inside the database, two tables represented as grids: "Orders" and "Outbox" (Outbox highlighted in Microsoft purple). A transaction boundary (dashed Microsoft blue box) surrounds both writes. Right side shows an Azure Function icon reading from the Outbox and publishing to an Azure Event Hubs icon (dark blue). A consumer icon reads from Event Hubs.

Text labels in dark gray: "1. BEGIN TX", "2. INSERT Order", "3. INSERT Outbox", "4. COMMIT", "Azure Function Poller", "Publish to Event Hubs", "Consumer".

Top title in bold Microsoft blue: "Transactional Outbox Pattern — Exactly-Once Between DB and Kafka on Azure". Bottom right corner: "Vineet Sharma" in small dark gray text.

Color scheme: White background, dark gray text, Microsoft blue outlines, purple highlight on Outbox table, teal arrows. All icons in Microsoft Fluent Design style.
```

### 2. Idempotent Consumer Pattern

```markdown
Generate a Microsoft Azure-style technical diagram for the "Idempotent Consumer" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. Azure Event Hubs icon sending duplicate messages (visualized as two identical envelopes with same offset number, one in green, one in light gray) to a consumer icon (Microsoft blue). The consumer checks an Azure Cosmos DB icon (light gray with dark outline, labeled "Idempotency Store") with conditional write. First message writes marker (green check) and processes; second message sees existing marker and skips (red X).

Text labels in dark gray: "Duplicate Message", "Conditional PUT (attribute_not_exists)", "First → Process", "Duplicate → Skip", "Cosmos DB TTL 7 days".

Top title in bold Microsoft blue: "Idempotent Consumer Pattern — Making Duplicates Harmless on Azure". Bottom right: "Vineet Sharma".

Color scheme: White background, dark gray text, green for success path, red for duplicate skip. Cosmos DB icon in Fluent Design style.
```

### 3. Partition Key / Ordering Pattern

```markdown
Generate a Microsoft Azure-style technical diagram for the "Partition Key / Ordering" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A producer icon (Microsoft blue) sending three messages with the same key "order_123" (purple highlight on key). The key hashes to Partition 2 of an Azure Event Hubs topic with 4 partitions shown as horizontal bars. All three messages stack in order within Partition 2 (shown as 1,2,3). A consumer icon (Microsoft blue) reads from Partition 2, processing messages in sequence.

Text labels in dark gray: "Key: order_123", "Hash → Partition 2", "Partition 0", "Partition 1", "Partition 2 (ordered)", "Partition 3", "Consumer → Sequential Processing".

Top title in bold Microsoft blue: "Partition Key Pattern — Preserving Order Per Entity on Azure". Bottom right: "Vineet Sharma".

Color scheme: White background, dark gray text, Partition 2 highlighted in teal or Microsoft purple.
```

### 4. Dead Letter Queue (DLQ) Pattern

```markdown
Generate a Microsoft Azure-style technical diagram for the "Dead Letter Queue (DLQ)" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. An Azure Event Hubs icon (dark blue) with messages. A poison message (skull icon in red) enters the consumer icon. Consumer fails (red X), retries 3 times (counters shown), then sends to DLQ (Azure Service Bus icon in red). Main Event Hubs continues processing good messages (green checkmarks). Application Insights icon monitors DLQ with bell icon. An engineer silhouette (gray) reviews DLQ and replays fixed messages (green arrow).

Text labels in dark gray: "Event Hubs Main Topic", "Poison Message", "Retry 1,2,3", "Service Bus DLQ", "Application Insights Alarm", "Manual Replay".

Top title in bold Microsoft blue: "Dead Letter Queue Pattern — Isolating Poison Messages on Azure". Bottom right: "Vineet Sharma".

Color scheme: White background, red for poison message and DLQ, green for normal flow, dark gray text.
```

### 5. Retry with Backoff Pattern

```markdown
Generate a Microsoft Azure-style technical diagram for the "Retry with Backoff" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A consumer icon (Microsoft blue) fails to process a message (red X). The message routes to retry stages shown as three horizontal bars with Azure Durable Functions icon: "retry_1s" (1 second delay with small clock), then "retry_5s" (5 second delay with medium clock), then "retry_30s" (30 second delay with large clock). Exponential curve showing increasing delays. After max retries, message goes to Service Bus DLQ (red queue).

Text labels in dark gray: "Transient Failure", "Retry 1s", "Retry 5s", "Retry 30s", "Exponential Backoff + Jitter", "DLQ after 3 retries", "Durable Functions".

Top title in bold Microsoft blue: "Retry with Backoff Pattern — Handling Transient Failures on Azure". Bottom right: "Vineet Sharma".

Color scheme: White background, dark gray text, orange for retry stages, red for DLQ. Clock icons in Microsoft blue.
```

### 6. Event Sourcing Pattern

```markdown
Generate a Microsoft Azure-style technical diagram for the "Event Sourcing" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A horizontal timeline from left to right showing events as envelopes: "OrderCreated" (teal), "PaymentProcessed" (teal), "OrderShipped" (teal). Each event appended to an Azure Event Hubs icon (Microsoft blue). A "State Builder" Azure Function icon reads all events and applies them to build current state in a Cosmos DB cylinder. A "Snapshot" icon periodically saves state to Blob Storage (orange) for faster recovery.

Text labels in dark gray: "Immutable Event Log (Event Hubs)", "Replay from beginning", "Apply Event → New State", "Snapshot to Blob Storage", "Current State Cache (Cosmos DB)".

Top title in bold Microsoft blue: "Event Sourcing Pattern — Event Hubs as Source of Truth on Azure". Bottom right: "Vineet Sharma".

Color scheme: White background, dark gray text, teal events in order, orange Blob Storage icon for snapshots.
```

### 7. CQRS Pattern

```markdown
Generate a Microsoft Azure-style technical diagram for the "CQRS (Command Query Responsibility Segregation)" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. Split design with a vertical divider line. Left side labeled "Command Side" in Microsoft blue: API icon receives commands, validates (checkmark), publishes events to Azure Event Hubs center icon. Right side labeled "Query Side" in teal: Multiple read models as icons — Cosmos DB (mobile), Azure SQL Database (analytics), Azure Table Storage (admin). Events flow from Event Hubs center to each read model updater (Azure Functions, downward arrows).

Text labels in dark gray: "Command → Validate → Publish", "Event Bus (Event Hubs)", "Azure Functions Updaters", "Cosmos DB (Mobile)", "Azure SQL (Analytics)", "Table Storage (Admin)".

Top title in bold Microsoft blue: "CQRS Pattern — Separate Read and Write Models on Azure". Bottom right: "Vineet Sharma".

Color scheme: White background, dark gray text, Microsoft blue for command side, teal for query side, Event Hubs in center as purple bridge icon.
```

### 8. Compacted Topic Pattern

```markdown
Generate a Microsoft Azure-style technical diagram for the "Compacted Topic" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. An Azure Event Hubs icon (Microsoft blue) with multiple messages for the same key "product_123". Messages shown as stacked rectangles: v1: price=19.99 (light gray), v2: price=24.99 (medium gray), v3: price=24.99 (dark teal, highlighted). After compaction (compression arrows), only v3 remains. A new consumer icon on AKS starts from end (green arrow) and immediately sees only the latest value. Multiple service icons (Order, Inventory, Pricing on AKS) read from the same compacted Event Hubs topic.

Text labels in dark gray: "Key: product_123", "v1, v2, v3 (only latest kept)", "Compaction", "Latest per key", "AKS Services get same current data".

Top title in bold Microsoft blue: "Compacted Topic Pattern — Distributed Key-Value Store on Azure". Bottom right: "Vineet Sharma".

Color scheme: White background, dark gray text, stack of messages collapsing into one highlighted in teal. AKS icons in Microsoft blue.
```

### 9. Event Carried State Transfer Pattern

```markdown
Generate a Microsoft Azure-style technical diagram for the "Event Carried State Transfer" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A producer icon (User Service in Microsoft blue) publishes an event. The event envelope is visibly "full" — containing user data fields (name, email, preferences) inside or next to it. Multiple consumer icons (Email, Notification, Analytics in teal) receive the same event via Azure Event Hubs (center icon). Each consumer processes using data from the event — no arrows back to User Service. A crossed-out network icon in red emphasizes "no fetching".

Text labels in dark gray: "UserUpdated Event (carries full profile)", "Email Service → uses email field", "Notification → uses preferences", "Analytics → uses all data", "NO FETCHING NEEDED".

Top title in bold Microsoft blue: "Event Carried State Transfer — Decouple Consumers from Source on Azure". Bottom right: "Vineet Sharma".

Color scheme: White background, dark gray text, full event envelope in Microsoft purple, consumers in teal, crossed-out fetch icon in red.
```

### 10. Claim Check Pattern

```markdown
Generate a Microsoft Azure-style technical diagram for the "Claim Check" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A producer icon (Microsoft blue) with a large file icon showing "100MB" in red. Large arrow points upward to Azure Blob Storage icon (orange). Producer sends small reference message (ticket icon in green) to Azure Event Hubs icon (Microsoft blue). Consumer icon (teal) receives small message, then downloads from Blob Storage using SAS URL (arrow from Blob Storage to consumer). Blob Storage lifecycle rule icon shows calendar with "Expire after 90 days".

Text labels in dark gray: "Large Payload (100MB)", "Upload to Blob Storage", "Claim Check (small reference)", "Event Hubs Message < 1KB", "Download from Blob Storage", "Process", "Lifecycle → Expire after 90 days".

Top title in bold Microsoft blue: "Claim Check Pattern — Handling Large Messages with Azure Blob Storage". Bottom right: "Vineet Sharma".

Color scheme: White background, dark gray text, large file in red, Blob Storage icon in orange, Event Hubs message in green.
```

### 11. Stream-Table Duality Pattern

```markdown
Generate a Microsoft Azure-style technical diagram for the "Stream-Table Duality" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. Left side: a stream of click events represented as flowing wave lines in teal with "10K/sec" label. Right side: a table of user profiles represented as grid icon in green, labeled "compacted topic". Center: Azure Stream Analytics icon or AKS icon (Microsoft blue) with a RocksDB or Redis cache icon (cylinder). Join operation symbol (overlap circle) shows stream enriched with table data. Output arrow to "enriched clicks" Event Hubs.

Text labels in dark gray: "Click Stream (10K/sec)", "User Profiles Table (compacted)", "Stream-Table Join", "Local Cache (RocksDB/Redis)", "Enriched Clicks Output".

Top title in bold Microsoft blue: "Stream-Table Duality Pattern — Real-Time Enrichment on Azure". Bottom right: "Vineet Sharma".

Color scheme: White background, dark gray text, teal waves for stream, green grid for table, Microsoft purple for join operation.
```

### 12. Saga (Choreography) Pattern

```markdown
Generate a Microsoft Azure-style technical diagram for the "Saga (Choreography)" pattern with a LIGHT BACKGROUND.

Visual composition: Clean white background with light gray grid. A chain of service circles connected horizontally: Trip Service (Microsoft blue) → Flight Service (Microsoft blue) → Hotel Service (Microsoft blue) → Car Service (Microsoft blue). Events flow between them via Azure Event Hubs icons (purple) as connectors. Success path shows green checkmarks on each step. Failure path shows a red X at Hotel, with dashed compensation arrows (red) going backward: Hotel cancels, Flight cancels. Azure Durable Functions icon in the background for orchestration option.

Text labels in dark gray: "Start Saga", "FlightBooked →", "HotelBooked →", "CarBooked →", "Trip Complete", "Failure: HotelBookingFailed ←", "Compensate: Cancel Flight", "Durable Functions".

Top title in bold Microsoft blue: "Saga Pattern — Distributed Transactions Without 2PC on Azure". Bottom right: "Vineet Sharma".

Color scheme: White background, dark gray text, green for success path, red for failure and compensation arrows, Event Hubs as purple connectors.
```

---

## 📋 Quick Reference: All Light Background Prompts Summary (Azure Edition)

```markdown
# GEMINI IMAGE PROMPTS INDEX — MICROSOFT AZURE STYLE (LIGHT BACKGROUND)

## Common Elements Across All Light Background Images (Azure Edition)
- Clean white/off-white background (#FFFFFF)
- Subtle light gray grid pattern (#F0F0F0)
- Microsoft blue text and outlines (#0078D4)
- Accent colors: Microsoft Purple (#5E2B97), Teal (#00A1AB), Green (#00A86B), Red (#FF4444), Orange (#FF8C00)
- Microsoft Fluent Design style icons
- Clean sans-serif fonts (Azure documentation style, Segoe UI or similar)
- No realistic people — use icons and silhouettes
- "Vineet Sharma" at bottom right corner of every image
- Professional, clean, whiteboard-style documentation aesthetic
- Microsoft Learn / Azure documentation style

## Series Cover
1. Master Cover Image — 11 Kafka Design Patterns — Azure + .NET 10 Edition (Light Background)

## Story Images (4)
2. Part 1 — Overview of All 11 Patterns on Azure (Light Background)
3. Part 2 — Reliability & Ordering Deep Dive on Azure (Light Background)
4. Part 3 — Data & State Deep Dive on Azure (Light Background)
5. Part 4 — Performance & Integration Deep Dive on Azure (Light Background)

## Individual Pattern Images (12)
6. Transactional Outbox (Azure + .NET 10)
7. Idempotent Consumer (Azure + .NET 10)
8. Partition Key / Ordering (Azure + .NET 10)
9. Dead Letter Queue (DLQ) (Azure + .NET 10)
10. Retry with Backoff (Azure + .NET 10)
11. Event Sourcing (Azure + .NET 10)
12. CQRS (Azure + .NET 10)
13. Compacted Topic (Azure + .NET 10)
14. Event Carried State Transfer (Azure + .NET 10)
15. Claim Check (Azure + .NET 10)
16. Stream-Table Duality (Azure + .NET 10)
17. Saga (Choreography) (Azure + .NET 10)

## Azure Service Icons Reference
- Azure Event Hubs — Purple/Dark Blue
- Azure Cosmos DB — Green/Dark Blue
- Azure SQL Database — Blue/Teal
- Azure Blob Storage — Orange/Blue
- Azure Functions — Purple/Blue
- Azure Durable Functions — Purple/Orange
- Azure Stream Analytics — Blue/Teal
- Azure Service Bus — Blue/Yellow
- Application Insights — Blue/Green
- Azure Kubernetes Service (AKS) — Blue/Cyan
- Azure Redis Cache — Red/Orange
```

---

**Author:** Vineet Sharma

**Date:** 2026

**Usage:** Copy any prompt above into Google Gemini (or any image generation tool that supports detailed prompts) to generate consistent, professional Microsoft Azure-style diagrams with **light backgrounds** for the Kafka Design Patterns series — Azure + .NET 10 Edition.