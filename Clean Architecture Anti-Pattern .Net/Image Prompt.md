# Gemini Image Generation Prompts - Clean Architecture Anti-Pattern in .NET Series

## Series Overview

| Story | Title | Icon | Prompt Reference |
|-------|-------|------|------------------|
| **1** | A .NET Developer's Guide to Resilience - Part 1 | 🏛️ | [View Prompt](#story-1-prompt-net) |
| **2** | Domain Logic in Disguise - Part 2 | 🎭 | [View Prompt](#story-2-prompt-net) |
| **3** | Defining the Boundary - Part 3 | 🔍 | [View Prompt](#story-3-prompt-net) |
| **4** | Building the Result Pattern - Part 4 | ⚙️ | [View Prompt](#story-4-prompt-net) |
| **5** | Across Real-World Domains - Part 5 | 🏢 | [View Prompt](#story-5-prompt-net) |
| **6** | Infrastructure Resilience - Part 6 | 🛡️ | [View Prompt](#story-6-prompt-net) |
| **7** | Testing & Observability - Part 7 | 🧪 | [View Prompt](#story-7-prompt-net) |
| **8** | The Road Ahead - Part 8 | 🚀 | [View Prompt](#story-8-prompt-net) |

---

## Story 1 Prompt

```markdown
**Story 1: 🏛️ Clean Architecture Anti-Pattern in .NET - A .NET Developer's Guide to Resilience - Part 1**

Microsoft Fluent Design style, bright gradient background from white (#FFFFFF) to soft blue (#E8F0FA). 
Layered architecture diagram showing Clean Architecture layers stacked vertically: Presentation (top), Application, Domain, Infrastructure (bottom), using Microsoft Fluent card style with subtle shadows and rounded corners. 
Microsoft red (#D13438) warning symbol on Presentation layer with a dashed connector arrow pointing from Presentation to Domain layer, labeled "Violation - Domain Exception Coupling" in Microsoft red. 
Microsoft green (#6BB700) checkmark on right side with a separate diagram showing proper flow: Presentation → Application Interface → Domain → Result<T> return, with clean Fluent connectors. 
.NET 10 logo in Microsoft style with badge in top right corner. 
Tech elements: hexagonal shapes representing services, clean geometric connectors with arrows, subtle grid pattern overlay in light gray. 
Microsoft Fluent Design with clean lines, subtle shadows, rounded corners, white background with soft blue accents. 
Title: "Clean Architecture Anti-Pattern in .NET - A .NET Developer's Guide to Resilience" at top center in bold, Microsoft dark gray (#252525). 
Subtitle: "Part 1 - Foundational Principles & Architectural Violation" below title in smaller font, Microsoft medium gray (#6E6E6E). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right corner in small sans-serif font, medium gray (#6E6E6E).
```

---

## Story 2 Prompt

```markdown
**Story 2: 🎭 Clean Architecture Anti-Pattern in .NET - Domain Logic in Disguise - Part 2**

Microsoft Fluent Design style, bright gradient background from white (#FFFFFF) to soft blue (#E8F0FA). 
Two side-by-side comparison panels with a central divider line in light gray. 
Left panel: clock icon with stack trace visualization showing multiple frames, labeled "Exception-Based" with Microsoft red (#D13438) downward arrow, metric text "28x slower, 10x memory" in dark gray. 
Right panel: green checkmark with Result pattern badge, labeled "Result Pattern" with Microsoft green (#6BB700) upward arrow, metric text "Fast, Low Allocation" in dark gray. 
Bottom section showing GC pressure visualization: small memory blocks with light gray and white, Microsoft red accent on left side, Microsoft green accent on right side. 
Bar chart showing performance benchmark comparison: Microsoft red bar high, Microsoft green bar low, in Fluent style. 
.NET 10 logo in top corner with performance metrics badge. 
Microsoft Fluent Design with clean lines, subtle shadows, rounded corners. 
Title: "Clean Architecture Anti-Pattern in .NET - Domain Logic in Disguise" at top in Microsoft dark gray (#252525). 
Subtitle: "Part 2 - Performance Implications & Hidden Complexity" below in Microsoft medium gray (#6E6E6E). 
Colors: Microsoft red (#D13438), Microsoft green (#6BB700), Microsoft dark gray (#252525), Microsoft medium gray (#6E6E6E), white (#FFFFFF), soft blue (#E8F0FA). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right in medium gray.
```

---

## Story 3 Prompt

```markdown
**Story 3: 🔍 Clean Architecture Anti-Pattern in .NET - Defining the Boundary - Part 3**

Microsoft Fluent Design style, bright gradient background from white (#FFFFFF) to soft blue (#E8F0FA). 
Central decision tree diagram with branching paths using Microsoft Fluent card style. 
Top: "Failure Occurs" rounded card with subtle shadow. 
Left branch: "Infrastructure Exception" with sub-branches showing Database (SQL Server icon), HTTP (globe icon), Cache (Redis icon), Messaging (Azure Service Bus icon) in Microsoft Fluent card style. 
Right branch: "Domain Outcome" with sub-branches showing NotFound, Conflict, Validation, BusinessRule icons in light gray cards. 
Microsoft green checkmark on Domain side, Microsoft red warning on Infrastructure side. 
Decision matrix table below with columns: Source, Deterministic, Retryable, Examples, using Microsoft Fluent table style. 
.NET 10 logo integrated. 
Microsoft Fluent Design with clean lines, subtle shadows, rounded corners, light background. 
Title: "Clean Architecture Anti-Pattern in .NET - Defining the Boundary" at top in Microsoft dark gray (#252525). 
Subtitle: "Part 3 - Taxonomy & Classification Patterns" below in Microsoft medium gray (#6E6E6E). 
Colors: Microsoft red (#D13438), Microsoft green (#6BB700), Microsoft dark gray (#252525), light gray (#F3F3F3), white (#FFFFFF), soft blue (#E8F0FA). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right.
```

---

## Story 4 Prompt

```markdown
**Story 4: ⚙️ Clean Architecture Anti-Pattern in .NET - Building the Result Pattern - Part 4**

Microsoft Fluent Design style, bright gradient background from white (#FFFFFF) to soft blue (#E8F0FA). 
Central Result<T> container with two paths using Microsoft Fluent card style: left side showing "Success → T Value" with Microsoft green (#6BB700) checkmark, right side showing "Failure → DomainError" with Microsoft red (#D13438) warning icon. 
Code snippet style elements showing Result<T> class structure, Map, Bind, Match methods as functional blocks in light gray with Cascadia Code font. 
DomainError record with fields: Code, Message, Type, Metadata displayed as property list in Microsoft card style. 
.NET 10 feature badges: "Required Members", "Primary Constructors", "Enhanced Pattern Matching", "Collection Expressions" in light rounded tags. 
Functional composition arrows showing Map → Bind → Match pipeline with light gray connectors. 
Microsoft Fluent Design with clean lines, subtle shadows, rounded corners. 
Title: "Clean Architecture Anti-Pattern in .NET - Building the Result Pattern" at top in Microsoft dark gray (#252525). 
Subtitle: "Part 4 - Complete Implementation & .NET 10 Features" below in Microsoft medium gray (#6E6E6E). 
Colors: Microsoft red (#D13438), Microsoft green (#6BB700), Microsoft dark gray (#252525), Microsoft medium gray (#6E6E6E), white (#FFFFFF), soft blue (#E8F0FA). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right.
```

---

## Story 5 Prompt

```markdown
**Story 5: 🏢 Clean Architecture Anti-Pattern in .NET - Across Real-World Domains - Part 5**

Microsoft Fluent Design style, bright gradient background from white (#FFFFFF) to soft blue (#E8F0FA). 
Four quadrants arranged in a 2x2 grid using Microsoft Fluent card style with subtle shadows. 
Top Left: Payment Processing - credit card icon, gateway symbol, metrics showing "Insufficient Funds vs Gateway Timeout" in light gray. 
Top Right: Inventory Management - warehouse shelf icon, barcode symbol, metrics showing "Out of Stock vs Database Deadlock" in light gray. 
Bottom Left: Healthcare Scheduling - hospital icon, calendar symbol, metrics showing "Double-Booking vs EMR Integration Failure" in light gray. 
Bottom Right: Logistics Tracking - truck icon, GPS symbol, metrics showing "Delivery Window vs GPS Offline" in light gray. 
Central hub showing "Result Pattern" with clean connector lines to each quadrant. 
.NET 10 logo integrated with ASP.NET Core badge in Microsoft style. 
Microsoft Fluent Design with clean lines, subtle shadows, rounded corners, light background. 
Title: "Clean Architecture Anti-Pattern in .NET - Across Real-World Domains" at top in Microsoft dark gray (#252525). 
Subtitle: "Part 5 - Payment, Inventory, Healthcare, Logistics Case Studies" below in Microsoft medium gray (#6E6E6E). 
Colors: Microsoft red (#D13438), Microsoft green (#6BB700), Microsoft dark gray (#252525), light gray (#F3F3F3), white (#FFFFFF), soft blue (#E8F0FA). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right.
```

---

## Story 6 Prompt

```markdown
**Story 6: 🛡️ Clean Architecture Anti-Pattern in .NET - Infrastructure Resilience - Part 6**

Microsoft Fluent Design style, bright gradient background from white (#FFFFFF) to soft blue (#E8F0FA). 
Resilience pipeline diagram showing sequential blocks using Microsoft Fluent card style: "Timeout Policy" → "Retry Policy (Exponential Backoff)" → "Circuit Breaker" → "Bulkhead" → "Fallback". 
Microsoft green path showing success flow, Microsoft red path showing failure with circuit breaker state. 
Middleware stack visualization: Request → InfrastructureExceptionMiddleware → Handler Chain → Response, with exception type branching using light gray cards. 
Polly logo integration with retry attempt counters in Microsoft style. 
Health check icons: SQL Server, Redis, HTTP service with green checkmarks in Microsoft Fluent card style. 
.NET 10 badges with resilience features. 
Microsoft Fluent Design with clean lines, subtle shadows, rounded corners, light background. 
Title: "Clean Architecture Anti-Pattern in .NET - Infrastructure Resilience" at top in Microsoft dark gray (#252525). 
Subtitle: "Part 6 - Middleware, Polly Policies & Circuit Breakers" below in Microsoft medium gray (#6E6E6E). 
Colors: Microsoft red (#D13438), Microsoft green (#6BB700), Microsoft dark gray (#252525), light gray (#F3F3F3), white (#FFFFFF), soft blue (#E8F0FA). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right.
```

---

## Story 7 Prompt

```markdown
**Story 7: 🧪 Clean Architecture Anti-Pattern in .NET - Testing & Observability - Part 7**

Microsoft Fluent Design style, bright gradient background from white (#FFFFFF) to soft blue (#E8F0FA). 
Test pyramid diagram using Microsoft Fluent card style: wide base labeled "Unit Tests - Many, Fast" with Result assertion icon, middle labeled "Integration Tests - Infrastructure" with database icon, top labeled "E2E Tests - Few" with browser icon. 
Observability dashboard mockup showing metrics panels in Microsoft style: "Domain Operations" green line, "Domain Errors" info level, "Infrastructure Errors" red alerts. 
Structured log entries showing INFO level for Domain Error, ERROR level for Infrastructure Exception in light gray cards. 
OpenTelemetry trace visualization with spans, .NET Meters icon, Azure Monitor dashboard thumbnail in Microsoft style. 
xUnit logo with async test badges. 
Microsoft Fluent Design with clean lines, subtle shadows, rounded corners, light background. 
Title: "Clean Architecture Anti-Pattern in .NET - Testing & Observability" at top in Microsoft dark gray (#252525). 
Subtitle: "Part 7 - Unit Tests, Integration Tests, Metrics & Dashboards" below in Microsoft medium gray (#6E6E6E). 
Colors: Microsoft red (#D13438), Microsoft green (#6BB700), Microsoft dark gray (#252525), light gray (#F3F3F3), white (#FFFFFF), soft blue (#E8F0FA). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right.
```

---

## Story 8 Prompt

```markdown
**Story 8: 🚀 Clean Architecture Anti-Pattern in .NET - The Road Ahead - Part 8**

Microsoft Fluent Design style, bright gradient background from white (#FFFFFF) to soft blue (#E8F0FA). 
Phased migration diagram showing 4 sequential phases using Microsoft Fluent card style with subtle shadows: 
Phase 1: Foundation (card with Result and DomainError icons)
Phase 2: Internal Migration (arrow connecting code blocks)
Phase 3: API Migration (endpoint icons with version badges)
Phase 4: Optimization (rocket icon, Native AOT badge)
Roadmap timeline with checkmarks at each phase in Microsoft style. 
.NET 10 Native AOT logo with performance badges. 
Success metrics visualization showing reduction arrows: Exception Throws ↓90%, P99 Latency ↓60%, GC Collections ↓47% in Microsoft Fluent card style. 
Architecture Decision Record document icon with checkmark in Microsoft style. 
Microsoft Fluent Design with clean lines, subtle shadows, rounded corners, light background. 
Title: "Clean Architecture Anti-Pattern in .NET - The Road Ahead" at top in Microsoft dark gray (#252525). 
Subtitle: "Part 8 - Migration Strategy, Native AOT & Organizational Adoption" below in Microsoft medium gray (#6E6E6E). 
Colors: Microsoft red (#D13438), Microsoft green (#6BB700), Microsoft dark gray (#252525), light gray (#F3F3F3), white (#FFFFFF), soft blue (#E8F0FA). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right.
```

---

## Usage Instructions

1. Copy the prompt for the desired story
2. Paste into Gemini image generation tool
3. Set resolution to 1280x720
4. Generate image
5. Use as header image for the corresponding technical article

---

## Design Guidelines Applied

| Element | Specification |
|---------|---------------|
| **Style** | Microsoft Fluent Design / Clean / Professional |
| **Color Palette** | Microsoft Red (#D13438), Microsoft Green (#6BB700), Microsoft Dark Gray (#252525), Microsoft Medium Gray (#6E6E6E), Light Gray (#F3F3F3), White (#FFFFFF), Soft Blue (#E8F0FA) |
| **Typography** | Segoe UI for titles, Cascadia Code for code elements |
| **Resolution** | 1280x720 (16:9) |
| **Elements** | Microsoft Fluent cards, subtle shadows, rounded corners, clean connectors |
| **Author Credit** | "Vineet Sharma" at bottom right |
| **Background** | Light gradient from white to soft blue |
| **Mood** | Professional, technical, clean, Microsoft documentation style |

---

## Color Palette Reference

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| Microsoft Red | #D13438 | Warnings, errors, negative outcomes |
| Microsoft Green | #6BB700 | Success, positive outcomes |
| Microsoft Dark Gray | #252525 | Titles, primary text |
| Microsoft Medium Gray | #6E6E6E | Subtitles, secondary text |
| Light Gray | #F3F3F3 | Background cards, accents |
| White | #FFFFFF | Primary background |
| Soft Blue | #E8F0FA | Gradient background accent |

---