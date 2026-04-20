# **RAG performance on laptop (16GB RAM, 100,000 doc

| Operation | Time | Memory |
|-----------|------|--------|
| Chunk 1000 documents | 2 seconds | 100MB |
| Generate embeddings (10,000 chunks) | 1 minute | 500MB |
| Vector search (top 5) | 15ms | N/A |
| Augmented LLM call | 4 seconds | N/A |
| Total query latency | 4.5 seconds | ~2GB (ChromaDB) |
