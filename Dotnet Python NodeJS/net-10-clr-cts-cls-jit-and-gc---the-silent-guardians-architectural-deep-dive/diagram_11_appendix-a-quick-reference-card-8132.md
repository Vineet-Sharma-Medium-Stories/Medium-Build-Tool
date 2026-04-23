# ## Appendix A: Quick Reference Card

```mermaid
---
config:
  theme: base
  layout: elk
---
mindmap
  root((.NET 10<br/>Runtime Core<br/>23 Years Evolution))
    CLR
      Manages execution
      Garbage Collection
        Gen0/1/2 + Background
        Pinned Object Heap NEW
        LOH Compaction NEW
      Exception handling
      Security & Transparency
      Diagnostics (EventPipe)
    CTS
      All types inherit from object
      Value vs Reference
      Primitives unified
      New types
        Half (16-bit float)
        Int128 / UInt128
        Vector512 (AVX-512)
      Generic math INumber<T>
    CLS
      Rules for cross-language libraries
      No unsigned publics
      No pointers in contracts
      Case-insensitive safe
      Generic variance FULL in .NET 10
      Default interface methods
    JIT
      Tier 0: Quick + instrumented (PGO)
      Tier 1: Optimizing (30+ calls)
      AVX-512 auto-vectorization
      ML-guided inlining
      Guarded devirtualization
      Range check elimination
      Loop unrolling (ML-predicted)
```
