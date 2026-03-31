# Gemini Image Generation Prompts - Clean Architecture Anti-Pattern in Python Series

## Series Overview

| Story | Title | Icon | Prompt Reference |
|-------|-------|------|------------------|
| **1** | A Developer's Guide to Resilience - Part 1 | 🏛️ | [View Prompt](#story-1-prompt) |
| **2** | Domain Logic in Disguise - Part 2 | 🎭 | [View Prompt](#story-2-prompt) |
| **3** | Defining the Boundary - Part 3 | 🔍 | [View Prompt](#story-3-prompt) |
| **4** | Building the Result Pattern - Part 4 | ⚙️ | [View Prompt](#story-4-prompt) |
| **5** | Across Real-World Domains - Part 5 | 🏢 | [View Prompt](#story-5-prompt) |
| **6** | Infrastructure Resilience - Part 6 | 🛡️ | [View Prompt](#story-6-prompt) |
| **7** | Testing & Observability - Part 7 | 🧪 | [View Prompt](#story-7-prompt) |
| **8** | The Road Ahead - Part 8 | 🚀 | [View Prompt](#story-8-prompt) |

---

## Story 1 Prompt

```markdown
**Story 1: 🏛️ Clean Architecture Anti-Pattern in Python - A Developer's Guide to Resilience - Part 1**

AWS cloud style illustration, clean light gradient background from white (#FFFFFF) to soft gray (#F8F9FA). 
Layered architecture diagram showing Clean Architecture layers stacked vertically: Presentation (top), Application, Domain, Infrastructure (bottom), using AWS service card style with soft shadows and rounded corners. 
Orange (#FF9900) warning symbol on Presentation layer with a dotted connector arrow pointing from Presentation to Domain layer, labeled "Violation - Domain Exception Coupling" in soft orange. 
Green (#27AE60) checkmark on right side with a separate diagram showing proper flow: Presentation → Application Interface → Domain → Result[T] return, with clean AWS-style connectors. 
Python logo in AWS style with 3.12+ badge in top right corner. 
Tech elements: hexagonal shapes representing services, clean geometric connectors with arrows, subtle grid pattern overlay in light gray. 
AWS style flat design with soft shadows, clean lines, rounded corners, white background with light gray accents. 
Title: "Clean Architecture Anti-Pattern in Python - A Developer's Guide to Resilience" at top center in bold, dark gray (#1F2A3E). 
Subtitle: "Part 1 - Foundational Principles & Architectural Violation" below title in smaller font, medium gray (#5A6C7E). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right corner in small sans-serif font, medium gray (#6C7A89).
```

---

## Story 2 Prompt

```markdown
**Story 2: 🎭 Clean Architecture Anti-Pattern in Python - Domain Logic in Disguise - Part 2**

AWS cloud style illustration, clean light gradient background from white (#FFFFFF) to soft gray (#F8F9FA). 
Two side-by-side comparison panels with a central divider line in light gray. 
Left panel: clock icon with stack trace visualization showing multiple frames, labeled "Exception-Based" with orange (#FF9900) downward arrow, metric text "23x slower, 12x memory" in dark gray. 
Right panel: green checkmark with Result pattern badge, labeled "Result Pattern" with green (#27AE60) upward arrow, metric text "Fast, Low Allocation" in dark gray. 
Bottom section showing resource usage visualization: small memory blocks with light gray and white, orange warning accent on left side, green calm accent on right side. 
Bar chart showing performance benchmark comparison: orange bar medium height, green bar low height, in AWS style. 
Python logo in top corner with performance metrics badge. 
AWS style flat design with soft shadows, clean lines, rounded corners. 
Title: "Clean Architecture Anti-Pattern in Python - Domain Logic in Disguise" at top in dark gray (#1F2A3E). 
Subtitle: "Part 2 - Performance Implications & Hidden Complexity" below in medium gray (#5A6C7E). 
Colors: AWS orange (#FF9900), AWS green (#27AE60), dark gray (#1F2A3E), medium gray (#5A6C7E), white (#FFFFFF). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right in medium gray.
```

---

## Story 3 Prompt

```markdown
**Story 3: 🔍 Clean Architecture Anti-Pattern in Python - Defining the Boundary - Part 3**

AWS cloud style illustration, clean light gradient background from white (#FFFFFF) to soft gray (#F8F9FA). 
Central decision tree diagram with branching paths using AWS service card style. 
Top: "Failure Occurs" rounded card with soft shadow. 
Left branch: "Infrastructure Exception" with sub-branches showing Database (PostgreSQL icon), HTTP (globe icon), Cache (Redis icon), Messaging (SQS icon) in AWS service card style. 
Right branch: "Domain Outcome" with sub-branches showing NotFound, Conflict, Validation, BusinessRule icons in light gray cards. 
Green checkmark on Domain side, orange warning on Infrastructure side. 
Decision matrix table below with columns: Source, Deterministic, Retryable, Examples, using AWS table style. 
Python logo integrated. 
AWS style flat design with soft shadows, clean lines, rounded corners, light background. 
Title: "Clean Architecture Anti-Pattern in Python - Defining the Boundary" at top in dark gray (#1F2A3E). 
Subtitle: "Part 3 - Taxonomy & Classification Patterns" below in medium gray (#5A6C7E). 
Colors: AWS orange (#FF9900), AWS green (#27AE60), dark gray (#1F2A3E), light gray (#F8F9FA), white (#FFFFFF). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right.
```

---

## Story 4 Prompt

```markdown
**Story 4: ⚙️ Clean Architecture Anti-Pattern in Python - Building the Result Pattern - Part 4**

AWS cloud style illustration, clean light gradient background from white (#FFFFFF) to soft gray (#F8F9FA). 
Central Result[T] container with two paths using AWS service card style: left side showing "Success → T Value" with green (#27AE60) checkmark, right side showing "Failure → DomainError" with orange (#FF9900) warning icon. 
Code snippet style elements showing Result[T] class structure, map, bind, match methods as functional blocks in light gray with monospace font. 
DomainError record with fields: Code, Message, Type, Metadata displayed as property list in AWS card style. 
Python 3.12+ feature badges: "match statement", "dataclass", "Generic", "async/await" in light rounded tags. 
Functional composition arrows showing map → bind → match pipeline with light gray connectors. 
AWS style flat design with soft shadows, clean lines, rounded corners. 
Title: "Clean Architecture Anti-Pattern in Python - Building the Result Pattern" at top in dark gray (#1F2A3E). 
Subtitle: "Part 4 - Complete Implementation & Python 3.12+ Features" below in medium gray (#5A6C7E). 
Colors: AWS orange (#FF9900), AWS green (#27AE60), dark gray (#1F2A3E), medium gray (#5A6C7E), white (#FFFFFF). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right.
```

---

## Story 5 Prompt

```markdown
**Story 5: 🏢 Clean Architecture Anti-Pattern in Python - Across Real-World Domains - Part 5**

AWS cloud style illustration, clean light gradient background from white (#FFFFFF) to soft gray (#F8F9FA). 
Four quadrants arranged in a 2x2 grid using AWS service card style with soft shadows. 
Top Left: Payment Processing - credit card icon, gateway symbol, metrics showing "Insufficient Funds vs Gateway Timeout" in light gray. 
Top Right: Inventory Management - warehouse shelf icon, barcode symbol, metrics showing "Out of Stock vs Database Deadlock" in light gray. 
Bottom Left: Healthcare Scheduling - hospital icon, calendar symbol, metrics showing "Double-Booking vs EMR Integration Failure" in light gray. 
Bottom Right: Logistics Tracking - truck icon, GPS symbol, metrics showing "Delivery Window vs GPS Offline" in light gray. 
Central hub showing "Result Pattern" with clean connector lines to each quadrant. 
Python logo integrated with FastAPI badge in AWS style. 
AWS style flat design with soft shadows, clean lines, rounded corners, light background. 
Title: "Clean Architecture Anti-Pattern in Python - Across Real-World Domains" at top in dark gray (#1F2A3E). 
Subtitle: "Part 5 - Payment, Inventory, Healthcare, Logistics Case Studies" below in medium gray (#5A6C7E). 
Colors: AWS orange (#FF9900), AWS green (#27AE60), dark gray (#1F2A3E), light gray (#F8F9FA), white (#FFFFFF). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right.
```

---

## Story 6 Prompt

```markdown
**Story 6: 🛡️ Clean Architecture Anti-Pattern in Python - Infrastructure Resilience - Part 6**

AWS cloud style illustration, clean light gradient background from white (#FFFFFF) to soft gray (#F8F9FA). 
Resilience pipeline diagram showing sequential blocks using AWS service card style: "Timeout Policy" → "Retry Policy" → "Circuit Breaker" → "Bulkhead" → "Fallback". 
Green path showing success flow, orange path showing failure with circuit breaker state. 
Middleware stack visualization: Request → InfrastructureExceptionMiddleware → Handler Chain → Response, with exception type branching using light gray cards. 
Tenacity logo integration with retry attempt counters in AWS style. 
Health check icons: PostgreSQL, Redis, HTTP service with green checkmarks in AWS card style. 
Python async/await badges. 
AWS style flat design with soft shadows, clean lines, rounded corners, light background. 
Title: "Clean Architecture Anti-Pattern in Python - Infrastructure Resilience" at top in dark gray (#1F2A3E). 
Subtitle: "Part 6 - Middleware, Tenacity Policies & Circuit Breakers" below in medium gray (#5A6C7E). 
Colors: AWS orange (#FF9900), AWS green (#27AE60), dark gray (#1F2A3E), light gray (#F8F9FA), white (#FFFFFF). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right.
```

---

## Story 7 Prompt

```markdown
**Story 7: 🧪 Clean Architecture Anti-Pattern in Python - Testing & Observability - Part 7**

AWS cloud style illustration, clean light gradient background from white (#FFFFFF) to soft gray (#F8F9FA). 
Test pyramid diagram using AWS card style: wide base labeled "Unit Tests - Many, Fast" with Result assertion icon, middle labeled "Integration Tests - Infrastructure" with database icon, top labeled "E2E Tests - Few" with browser icon. 
Observability dashboard mockup showing metrics panels in AWS style: "Domain Operations" green line, "Domain Errors" info level, "Infrastructure Errors" orange alerts. 
Structured log entries showing INFO level for Domain Error, ERROR level for Infrastructure Exception in light gray cards. 
OpenTelemetry trace visualization with spans, Prometheus metrics meter icon, Grafana dashboard thumbnail in AWS style. 
Pytest logo with async test badges. 
AWS style flat design with soft shadows, clean lines, rounded corners, light background. 
Title: "Clean Architecture Anti-Pattern in Python - Testing & Observability" at top in dark gray (#1F2A3E). 
Subtitle: "Part 7 - Unit Tests, Integration Tests, Metrics & Dashboards" below in medium gray (#5A6C7E). 
Colors: AWS orange (#FF9900), AWS green (#27AE60), dark gray (#1F2A3E), light gray (#F8F9FA), white (#FFFFFF). 
Resolution: 1280x720. 
Author credit "Vineet Sharma" at bottom right.
```

---

## Story 8 Prompt

```markdown
**Story 8: 🚀 Clean Architecture Anti-Pattern in Python - The Road Ahead - Part 8**

AWS cloud style illustration, clean light gradient background from white (#FFFFFF) to soft gray (#F8F9FA). 
Phased migration diagram showing 4 sequential phases using AWS service card style with soft shadows: 
Phase 1: Foundation (card with Result and DomainError icons)
Phase 2: Internal Migration (arrow connecting code blocks)
Phase 3: API Migration (endpoint icons with version badges)
Phase 4: Optimization (rocket icon, Python 3.12+ badge)
Roadmap timeline with checkmarks at each phase in AWS style. 
Python 3.12+ logo with performance badges. 
Success metrics visualization showing reduction arrows: Exception Raises ↓98%, P99 Latency ↓60%, GC Collections ↓47% in AWS card style. 
Architecture Decision Record document icon with checkmark in AWS style. 
AWS style flat design with soft shadows, clean lines, rounded corners, light background. 
Title: "Clean Architecture Anti-Pattern in Python - The Road Ahead" at top in dark gray (#1F2A3E). 
Subtitle: "Part 8 - Migration Strategy, Python 3.12+ & Organizational Adoption" below in medium gray (#5A6C7E). 
Colors: AWS orange (#FF9900), AWS green (#27AE60), dark gray (#1F2A3E), light gray (#F8F9FA), white (#FFFFFF). 
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
| **Style** | AWS Cloud Style / Clean / Professional |
| **Color Palette** | AWS Orange (#FF9900), AWS Green (#27AE60), Dark Gray (#1F2A3E), Light Gray (#F8F9FA), White (#FFFFFF) |
| **Typography** | Clean sans-serif fonts, monospace for code |
| **Resolution** | 1280x720 (16:9) |
| **Elements** | AWS service cards, soft shadows, rounded corners, clean connectors |
| **Author Credit** | "Vineet Sharma" at bottom right |
| **Background** | Light gradient from white to soft gray |
| **Mood** | Professional, technical, clean, AWS documentation style |

---

## Color Palette Reference

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| AWS Orange | #FF9900 | Warnings, accents, primary highlight |
| AWS Green | #27AE60 | Success, positive outcomes |
| Dark Gray | #1F2A3E | Titles, primary text |
| Medium Gray | #5A6C7E | Subtitles, secondary text |
| Light Gray | #F8F9FA | Background, cards |
| White | #FFFFFF | Primary background |

---