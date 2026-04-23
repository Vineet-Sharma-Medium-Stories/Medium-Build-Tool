# ### 3.6 CLS Rule Reference — Complete ECMA-335 Tab

| Rule # | ECMA Reference | Description | Violation Warning |
|--------|----------------|-------------|-------------------|
| 1 | §7.1 | CLS rules apply only to public/protected members | N/A |
| 2 | §7.2 | No non-CLS types in public signatures | CS3001, CS3002 |
| 3 | §7.3 | No pointers in public signatures | CS3003 (using unsafe) |
| 4 | §7.4 | No return-type-only overloads | CS3006 |
| 5 | §7.5 | No ref/out/array-rank-only overloads | CS3007 |
| 6 | §7.6 | Base types must be CLS-compliant | CS3009 |
| 7 | §7.7 | Implemented interfaces must be CLS-compliant | CS3010 |
| 8 | §7.8 | Member visibility cannot hide inherited CLS member | CS3011 |
| 9 | §7.9 | Overridden methods must use CLS-compliant types | CS3012 |
| 10 | §7.10 | Generic variance must follow CLS rules | CS3013 |
| 11 | §7.11 | Operator overloads must be overloaded in pairs | CS3014 |
| 12 | §7.12 | Parameter arrays must be single-dimensional | CS3015 |
| 13 | §7.13 | Enums must have CLS-compliant underlying type | CS3016 |
| 14 | §7.14 | Non-CLS types can be used if marked | CS3017 |
| 15 | §7.15 | Visibility and accessibility rules | CS3018 |
| 16 | §7.16 | Required members must be present | CS3019 |
