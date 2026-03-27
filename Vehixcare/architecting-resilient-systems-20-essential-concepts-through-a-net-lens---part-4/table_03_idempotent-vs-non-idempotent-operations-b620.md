# table_03_idempotent-vs-non-idempotent-operations-b620


| Operation | Idempotent? | Example |
|-----------|-------------|---------|
| GET | Yes | Retrieving vehicle details |
| PUT (full update) | Yes | Updating entire vehicle record |
| DELETE | Yes | Deleting a vehicle |
| POST (create) | No | Creating a new service booking |
| PATCH | Maybe | Partial updates |
