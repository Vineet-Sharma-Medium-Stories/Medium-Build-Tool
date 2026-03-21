# Gemini Image Generation Prompts for All Three Parts

## Part 1: Foundations - Observatory, Async, and Exception Handling

```
Create a professional technical illustration for an architectural document titled "Architectural Remediation Framework: Eliminating the 12 Silent Killers in .NET 10 Web APIs - Part 1: Foundations".

Visual Composition:
- Background: Modern Microsoft-style gradient background in deep navy blue (#0A2E5C) fading to dark teal (#0A5C5C) with subtle geometric patterns reminiscent of Microsoft Fluent Design System
- Central Element: A massive circular shield divided into 6 segments, each representing a fixed anti-pattern:

Anti-Pattern Logos (arranged clockwise around shield):
1. "Fat Controllers" - A bloated controller icon with warning symbol, crossed out with red X, transforming into a sleek MediatR pipeline icon
2. "No Validation" - A broken shield icon with question mark, crossed out, transforming into FluentValidation checkmark shield
3. "Raw Exceptions" - An exploding bug icon with stack trace text, crossed out, transforming into clean RFC 7807 Problem Details document
4. "Blocking Async" - A padlock icon with thread blocking visualization, crossed out, transforming into flowing async arrows with await keyword
5. "No Cancellation" - A waste bin with clock icon, crossed out, transforming into graceful cancellation token flow
6. "No Observability" - A blindfolded eye icon, crossed out, transforming into OpenTelemetry circles with Serilog logs and Prometheus metrics

Technology Logos (floating around the shield):
- .NET 10 logo (prominent, top center)
- MediatR logo (left side)
- FluentValidation logo (right side)
- Serilog logo (bottom left)
- OpenTelemetry logo (bottom right)
- Redis logo (integrated with async flow)

Style Elements:
- Glowing blue connection lines between all components showing data flow
- Before/after visualization showing transformation from broken state to fixed state
- Subtle holographic effect on the shield
- Floating particles representing telemetry data flowing upward
- Clean sans-serif fonts in white and cyan (#00E5FF)
- Bottom right corner: "Vineet Sharma" in elegant white typography with subtle shadow

Mood: Technical, professional, hopeful transformation, Microsoft Fluent Design aesthetic
Resolution: 16:9 widescreen format, suitable for architectural documentation
```

---

## Part 2: Data Access - Pagination, Projections, and API Contracts

```
Create a professional technical illustration for an architectural document titled "Architectural Remediation Framework: Eliminating the 12 Silent Killers in .NET 10 Web APIs - Part 2: Data Access".

Visual Composition:
- Background: Modern Microsoft-style gradient background in forest green (#1E4D2E) fading to deep indigo (#2E2E5C) with circuit board pattern overlays
- Central Element: A massive database cylinder transformed into a layered cake structure with 4 distinct layers, each representing a fixed anti-pattern:

Anti-Pattern Logos (arranged as layers in the database structure):
1. "No Pagination" - An overflowing table icon with infinite scroll, crossed out, transforming into paginated pages with Skip/Take arrows and page numbers 1,2,3... with metadata headers
2. "Wrong HTTP Status Codes" - A confused robot icon with 200 OK stamp, crossed out, transforming into proper status code badges: 200✓, 201✓, 400✗, 404✗, 500✗, 429⚠ with RFC 7807 document
3. "Over-fetching Data" - A giant elephant icon (SELECT *) carrying too many columns, crossed out, transforming into lean SELECT projection with only 3 columns visible
4. "Returning EF Entities" - A tangled spaghetti icon with circular references, crossed out, transforming into clean DTO boxes with AutoMapper arrows

Technology Logos (positioned around the data architecture):
- .NET 10 logo (prominent, top)
- EF Core logo (left side, integrated with database)
- AutoMapper logo (right side, connecting entities to DTOs)
- SQL Server logo (bottom center, within database)
- Redis logo (floating, representing caching layer)
- REST API badges (floating, showing HTTP methods)

Style Elements:
- Data flow arrows showing optimized queries traveling from API to database
- Pagination control sliders showing page size adjustment
- SQL query optimization visualization showing reduced column count
- DTO transformation animation effect showing entity to DTO mapping
- Binary code rain in background (light green digital rain)
- Clean data visualization with bar charts showing 99.5% data reduction
- Bottom right corner: "Vineet Sharma" in elegant white typography with subtle glow

Mood: Efficient, optimized, clean, Microsoft Fluent Design with data visualization aesthetic
Resolution: 16:9 widescreen format, suitable for architectural documentation
```

---

## Part 3: Security & Resilience - Rate Limiting and Idempotency

```
Create a professional technical illustration for an architectural document titled "Architectural Remediation Framework: Eliminating the 12 Silent Killers in .NET 10 Web APIs - Part 3: Security & Resilience".

Visual Composition:
- Background: Modern Microsoft-style gradient background in deep burgundy (#5C2E2E) fading to charcoal black (#2E2E2E) with subtle security grid patterns and lock icon motifs
- Central Element: A massive fortress wall divided into 2 powerful sections, each representing a fixed anti-pattern:

Anti-Pattern Logos (arranged as fortress defenses):
1. "No Rate Limiting" - Left side: Open floodgates with tsunami waves overwhelming servers, crossed out, transforming into sliding window rate limiter with token bucket visualization showing controlled flow, 429 responses with Retry-After headers, and graduated tiers (Free:20, Standard:100, Premium:500, Enterprise:2000)
2. "No Idempotency" - Right side: Duplicate cloning machine creating identical order copies with multiple credit card charges, crossed out, transforming into distributed Redis lock system with idempotency key flow showing single processing with cached responses for retries, RFC 7231 compliant header visualization

Technology Logos (arranged as fortress defenses):
- .NET 10 logo (prominent, top center, glowing)
- ASP.NET Core Rate Limiting shield logo (left tower)
- Redis logo with lock icon (right tower, central)
- Azure logo (background, representing cloud infrastructure)
- JWT/OAuth badges (floating, representing authentication)

Style Elements:
- DDoS attack visualization as red waves hitting the rate limiter shield
- Green successful requests flowing through the fortress gate
- Idempotency key flow as unique golden keys floating between client and server
- Redis cluster visualization as interconnected lock icons
- Duplicate prevention counter showing "0 duplicates" with checkmark
- Financial impact visualization: before ($$$$ double charges) to after ($ single charge)
- 429 response visualization with retry countdown timer
- Distributed lock mechanism showing "First request: Process | Retries: Cache hit"
- Background: Subtle network traffic visualization with throttling indicators
- Bottom right corner: "Vineet Sharma" in elegant white typography with security badge styling

Mood: Secure, resilient, protected, Microsoft Fluent Design with security and defense aesthetic
Resolution: 16:9 widescreen format, suitable for architectural documentation
```

---

## Bonus: Complete Architecture Overview (All 12 Anti-Patterns)

```
Create a professional technical illustration for an architectural document titled "Architectural Remediation Framework: Eliminating the 12 Silent Killers in .NET 10 Web APIs - Complete Architecture".

Visual Composition:
- Background: Epic Microsoft-style gradient background from deep navy blue (#0A2E5C) through forest green (#1E4D2E) to burgundy (#5C2E2E) representing the three parts, with Fluent Design geometry patterns
- Central Element: A massive architectural blueprint showing the complete .NET 10 API architecture with three concentric circles representing Parts 1, 2, and 3:

Inner Circle (Part 1 - Foundation - Blue Theme):
- MediatR pipeline icon
- FluentValidation shield
- Problem Details document
- Async flow arrows
- CancellationToken flow
- OpenTelemetry circles with Serilog logs

Middle Circle (Part 2 - Data Access - Green Theme):
- Database cylinder with pagination pages
- EF Core projection arrows
- DTO transformation boxes
- AutoMapper connections
- Proper HTTP status badges
- SQL optimization visualization

Outer Circle (Part 3 - Security & Resilience - Red/Burgundy Theme):
- Rate limiting fortress wall
- Token bucket visualization
- Redis cluster with idempotency keys
- Distributed lock mechanisms
- 429 response with Retry-After
- Duplicate prevention counter

All 12 Anti-Pattern Logos (arranged around the circles, each with before/after visualization):
1. Fat Controller → MediatR
2. No Validation → FluentValidation
3. Raw Exceptions → Problem Details
4. Blocking Async → Async/Await
5. No Cancellation → CancellationToken
6. No Pagination → Pagination
7. Wrong Status Codes → Proper HTTP
8. Over-fetching → Projections
9. EF Entities → DTOs
10. No Rate Limiting → Rate Limiting
11. No Observability → OpenTelemetry
12. No Idempotency → Redis Idempotency

Technology Logos (positioned around the architecture):
- .NET 10 logo (largest, top center, radiating)
- Microsoft Azure logo (background cloud)
- SQL Server logo (integrated with data layer)
- Redis logo (connected to idempotency)
- OpenTelemetry logo (observability layer)
- Serilog logo (logging layer)
- MediatR logo (application layer)
- AutoMapper logo (mapping layer)

Style Elements:
- Flowing connection lines showing request lifecycle from client through all three layers
- Performance improvement metrics: 86% faster | 99.5% less data | 100% duplicate elimination
- Transformation visualization from broken (red X) to fixed (green checkmark)
- Holo