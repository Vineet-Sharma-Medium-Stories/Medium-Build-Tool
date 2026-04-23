# ### 4.2 .NET 10 JIT Pipeline — Complete Detailed D

```mermaid
---
config:
  theme: base
  layout: elk
---
flowchart TD
    IL[IL Code from Assembly<br/>(C#, F#, VB.NET compiled)] --> QUICK
    
    subgraph QUICK ["Tier 0: Quick JIT (.NET 10) - ~0.5-2ms compilation"]
        Q1["Step 1: Minimal optimization<br/>- No inlining (except trivial getters)<br/>- No loop optimizations<br/>- No vectorization"]
        Q2["Step 2: Generate instrumented trampoline for PGO<br/>- Insert call counters (per call site)<br/>- Insert branch probes<br/>- Insert type profile points"]
        Q3["Step 3: Emit unoptimized native code<br/>- One-to-one IL to instruction mapping<br/>- Preserve debug information<br/>- No register optimization"]
        Q4["Step 4: Cache generated code</br>- Store in code heap"]
    end
    
    QUICK --> EXEC0["Execute Instrumented Code<br/>(First N calls where N = 30 default)"]
    EXEC0 --> COLLECT["Collect PGO Data in Background:<br/>- Call site frequencies (which method called)<br/>- Branch prediction patterns (taken/not taken)<br/>- Type profile (for devirtualization)<br/>- Loop trip counts (average iterations)<br/>- Exception profile (exception frequency)"]
    
    COLLECT --> THRESHOLD{Call Count >= 30?<br/>Configurable via DOTNET_TieredPGO_CallCountThreshold}
    
    THRESHOLD -->|No| WAIT["Continue Tier 0 execution<br/>Update PGO samples continuously"]
    WAIT --> EXEC0
    
    THRESHOLD -->|Yes| PROMOTE["Promote to Tier 1 Queue<br/>(Background compilation thread - non-blocking)"]
    
    PROMOTE --> OPT
    
    subgraph OPT ["Tier 1: Optimizing JIT (.NET 10) - ~20-100ms compilation"]
        O1["Full optimizations (C2/JIT level)<br/>- Aggressive inlining decisions based on PGO"]
        O2["Inlining (depth up to 25, ML-predicted benefit analysis)<br/>- PGO data identifies hot calls first"]
        O3["Loop unrolling (ML-predicted factor: 2x, 4x, or 8x)<br/>- Based on average trip count from PGO"]
        O4["AVX-512 auto-vectorization<br/>with alignment detection and remainder handling"]
        O5["Devirtualization w/ guarded devirtualization (GDV)<br/>- Single-type check, then direct call"]
        O6["PGO-guided code reordering (hot/cold splitting)<br/>- Hot path contiguous in memory<br/>- Cold path moved to end"]
        O7["Constant propagation & folding<br/>- Compile-time evaluation where possible"]
        O8["Dead code elimination (DCE)<br/>- Remove unreachable branches"]
        O9["Range check elimination (RCE)<br/>- Remove array bounds checks in loops"]
        O10["Register allocation (linear scan with PGO hints)<br/>- Better spill decisions based on hotness"]
        O11["Loop invariant code motion (LICM)<br/>- Hoist loop-invariant computations"]
    end
    
    OPT --> NATIVE2["Highly optimized native code<br/>+ Caching in call site stub for future calls"]
    NATIVE2 --> CACHE["Promoted execution path<br/>Tier 0 code marked for garbage collection"]
    CACHE --> EXEC_OPT["Execute optimized code<br/>- No instrumentation overhead<br/>- Max performance"]
```
