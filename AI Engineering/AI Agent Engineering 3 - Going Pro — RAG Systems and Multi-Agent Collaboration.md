# AI Agent Engineering 3 - Going Pro — RAG Systems and Multi-Agent Collaboration


## From Single Agents to Intelligent Teams

Welcome back to our AI Agent Engineering series! In [Part 2](link-to-part-2), we built our first real agent — complete with tools, memory, and the ability to handle multi-step tasks like booking flights. Your WhatsApp travel agent can now remember user preferences, use multiple tools, and maintain context across conversations.

But what happens when your agent needs to answer questions from a 500-page policy manual? Or when one agent isn't enough to handle complex customer service scenarios? That's where we're going today.

By the end of this story, you'll have built:
- A RAG system that can answer questions from any document collection
- A multi-agent team with specialized roles working together
- A customer support system with supervisor, specialists, and escalation paths

---

## 🔄 What We Covered in Part 2

Before we dive into new territory, let's quickly recap what you learned in the previous story:

### Agent Core Architecture
- The think-act-observe autonomous loop
- Planning vs reacting strategies
- LangChain and LangGraph frameworks

### Tool & Function Calling
- Building reusable tools with JSON schemas
- Tool registry and orchestration
- Error handling with retries and circuit breakers
- Real tools: Weather, Flights, Hotels, Web Search

### Memory Systems
- Short-term memory for conversation context
- Long-term Redis-based persistent memory
- Semantic memory with embeddings
- Working memory for task state

### Complete WhatsApp Travel Agent
- Multi-step booking flows
- User preference tracking
- Context maintenance across days
- Production-ready FastAPI integration

Your agent from Part 2 is already impressive — it can remember users, use tools, and handle complex bookings. But it has limitations:

**Limitations of your current agent:**
- Knowledge is limited to what's in the LLM's training data
- Can't access your company's internal documents or policies
- Single agent must handle everything (jack of all trades, master of none)
- No way to parallelize complex research tasks

Today, we fix all of that.

---

## 🎯 What We'll Cover in Part 3

1. **RAG Systems Fundamentals** — Connecting agents to knowledge bases
2. **Chunking Strategies** — How to split documents for optimal retrieval
3. **Vector Databases Deep Dive** — Pinecone, Weaviate, Milvus, Chroma, Qdrant
4. **RAG Frameworks** — LlamaIndex, LangChain Retrieval, Haystack
5. **Multi-Agent Patterns** — Planner-executor, supervisor, debate, swarm
6. **Multi-Agent Frameworks** — AutoGen, CrewAI, LangGraph, Semantic Kernel

---

# Part 3.1: RAG Systems — Giving Your Agent Knowledge

*"An agent without knowledge is just a confident storyteller."*

RAG (Retrieval-Augmented Generation) is how you connect your agent to vast knowledge bases — company policies, product documentation, research papers, customer support history, anything.

## Why RAG Matters

LLMs have knowledge cutoffs. They don't know:
- Your company's internal policies and procedures
- Your products' latest features and prices
- Your customers' previous support tickets
- Real-time inventory or availability
- Proprietary research or data

RAG solves this by retrieving relevant information in real-time and feeding it to the LLM as context.

```
User Question 
    ↓
[Retrieve relevant documents from knowledge base]
    ↓
Question + Retrieved Documents 
    ↓
[LLM generates answer based on actual data]
    ↓
Response with citations
```

## The RAG Pipeline

```python
class RAGPipeline:
    """
    Complete RAG pipeline from document to answer
    """
    
    def __init__(self):
        self.documents = []
        self.chunks = []
        self.embeddings = []
        self.vector_store = None
        self.llm = None
        
    def load_documents(self, paths: List[str]) -> List[Document]:
        """
        Load documents from files
        """
        documents = []
        for path in paths:
            if path.endswith('.pdf'):
                documents.extend(self._load_pdf(path))
            elif path.endswith('.txt'):
                documents.extend(self._load_text(path))
            elif path.endswith('.md'):
                documents.extend(self._load_markdown(path))
        return documents
    
    def chunk_documents(self, documents: List[Document], strategy: str = "semantic") -> List[Chunk]:
        """
        Split documents into retrievable chunks
        """
        if strategy == "fixed":
            return self._fixed_size_chunking(documents)
        elif strategy == "semantic":
            return self._semantic_chunking(documents)
        elif strategy == "recursive":
            return self._recursive_chunking(documents)
        else:
            raise ValueError(f"Unknown strategy: {strategy}")
    
    def create_embeddings(self, chunks: List[Chunk]) -> List[List[float]]:
        """
        Create embeddings for all chunks
        """
        texts = [chunk.text for chunk in chunks]
        return self._embedding_model.encode(texts)
    
    def index_vectors(self, chunks: List[Chunk], embeddings: List[List[float]]):
        """
        Store chunks and embeddings in vector database
        """
        # Store in vector DB (implementation varies by DB)
        pass
    
    def retrieve(self, query: str, top_k: int = 3) -> List[Chunk]:
        """
        Retrieve relevant chunks for a query
        """
        # Create query embedding
        query_embedding = self._embedding_model.encode([query])[0]
        
        # Search vector DB
        results = self.vector_store.search(query_embedding, top_k)
        
        return results
    
    def generate(self, query: str, context: List[Chunk]) -> str:
        """
        Generate answer using retrieved context
        """
        context_text = "\n\n".join([c.text for c in context])
        
        prompt = f"""
Answer the question based on the provided context.

Context:
{context_text}

Question: {query}

Answer:
"""
        return self.llm.generate(prompt)
    
    def query(self, query: str) -> Dict:
        """
        Complete RAG query
        """
        # Retrieve relevant chunks
        chunks = self.retrieve(query)
        
        # Generate answer
        answer = self.generate(query, chunks)
        
        return {
            "query": query,
            "answer": answer,
            "sources": [{"text": c.text[:200], "source": c.source} for c in chunks]
        }
```

---

## Chunking Strategies: The Art of Splitting Documents

The way you split documents into chunks dramatically affects retrieval quality. Get it wrong, and your agent will miss critical information or retrieve irrelevant context.

### Strategy 1: Fixed-Size Chunking

Simplest approach: split every N characters or tokens.

```python
class FixedSizeChunker:
    """
    Split text into fixed-size chunks with overlap
    """
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.encoder = tiktoken.get_encoding("cl100k_base")
        
    def chunk(self, text: str, metadata: Dict = None) -> List[Dict]:
        """
        Split text into fixed-size chunks
        """
        tokens = self.encoder.encode(text)
        chunks = []
        
        for i in range(0, len(tokens), self.chunk_size - self.chunk_overlap):
            chunk_tokens = tokens[i:i + self.chunk_size]
            chunk_text = self.encoder.decode(chunk_tokens)
            
            chunks.append({
                "text": chunk_text,
                "tokens": len(chunk_tokens),
                "start_idx": i,
                "end_idx": i + len(chunk_tokens),
                "metadata": metadata or {}
            })
            
            if i + self.chunk_size >= len(tokens):
                break
        
        return chunks

# Example
chunker = FixedSizeChunker(chunk_size=500, chunk_overlap=50)
chunks = chunker.chunk(long_document)

# Pros: Simple, predictable, works for any text
# Cons: May cut sentences in half, lose semantic boundaries
```

### Strategy 2: Semantic Chunking

Split at natural boundaries like paragraphs or sentences.

```python
class SemanticChunker:
    """
    Split text at semantic boundaries (paragraphs, sections)
    """
    
    def __init__(self, max_tokens: int = 1000):
        self.max_tokens = max_tokens
        self.encoder = tiktoken.get_encoding("cl100k_base")
        
    def chunk(self, text: str, metadata: Dict = None) -> List[Dict]:
        """
        Split text by paragraphs, then combine until token limit
        """
        # Split by double newlines (paragraphs)
        paragraphs = re.split(r'\n\s*\n', text)
        
        chunks = []
        current_chunk = []
        current_tokens = 0
        
        for para in paragraphs:
            para_tokens = len(self.encoder.encode(para))
            
            # If adding this paragraph exceeds limit, start new chunk
            if current_tokens + para_tokens > self.max_tokens and current_chunk:
                chunk_text = '\n\n'.join(current_chunk)
                chunks.append({
                    "text": chunk_text,
                    "tokens": current_tokens,
                    "metadata": metadata or {}
                })
                current_chunk = [para]
                current_tokens = para_tokens
            else:
                current_chunk.append(para)
                current_tokens += para_tokens
        
        # Add last chunk
        if current_chunk:
            chunk_text = '\n\n'.join(current_chunk)
            chunks.append({
                "text": chunk_text,
                "tokens": current_tokens,
                "metadata": metadata or {}
            })
        
        return chunks

# Pros: Preserves semantic units, better for retrieval
# Cons: Variable chunk sizes, may still be too large
```

### Strategy 3: Recursive Chunking

Try multiple separators recursively to maintain structure.

```python
class RecursiveChunker:
    """
    Recursively split using multiple separators
    """
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = ["\n\n", "\n", ".", "!", "?", ",", " ", ""]
        
    def chunk(self, text: str, metadata: Dict = None) -> List[Dict]:
        """
        Recursively split using separators
        """
        return self._split_text(text, self.separators, metadata)
    
    def _split_text(self, text: str, separators: List[str], metadata: Dict) -> List[Dict]:
        """
        Internal recursive splitting
        """
        final_chunks = []
        
        # Get current separator
        separator = separators[-1] if separators else ""
        new_separators = separators[:-1]
        
        # Split by current separator
        if separator:
            splits = text.split(separator)
        else:
            splits = list(text)
        
        good_splits = []
        for s in splits:
            if self._count_tokens(s) < self.chunk_size:
                good_splits.append(s)
            else:
                if good_splits:
                    merged_text = separator.join(good_splits)
                    if merged_text:
                        final_chunks.append({
                            "text": merged_text,
                            "metadata": metadata
                        })
                    good_splits = []
                
                if not new_separators:
                    final_chunks.append({
                        "text": s,
                        "metadata": metadata
                    })
                else:
                    other_chunks = self._split_text(s, new_separators, metadata)
                    final_chunks.extend(other_chunks)
        
        if good_splits:
            merged_text = separator.join(good_splits)
            if merged_text:
                final_chunks.append({
                    "text": merged_text,
                    "metadata": metadata
                })
        
        return final_chunks
    
    def _count_tokens(self, text: str) -> int:
        """Count tokens in text"""
        encoder = tiktoken.get_encoding("cl100k_base")
        return len(encoder.encode(text))

# Pros: Best balance, maintains structure as much as possible
# Cons: More complex, slower
```

### Strategy 4: Document Structure Chunking

Use document structure (headings, sections) to create chunks.

```python
class StructureChunker:
    """
    Split documents based on their structure (headings, sections)
    """
    
    def __init__(self):
        self.heading_patterns = [
            r'^# (.+)$',  # Markdown h1
            r'^## (.+)$',  # Markdown h2
            r'^### (.+)$',  # Markdown h3
            r'^[A-Z][^a-z\n]+$',  # ALL CAPS HEADINGS
            r'^\d+\.\s+(.+)$',  # Numbered sections
        ]
        
    def chunk(self, text: str, metadata: Dict = None) -> List[Dict]:
        """
        Split by document headings
        """
        lines = text.split('\n')
        chunks = []
        current_section = []
        current_heading = "Introduction"
        
        for line in lines:
            # Check if line is a heading
            heading = self._is_heading(line)
            if heading:
                # Save previous section
                if current_section:
                    chunks.append({
                        "text": '\n'.join(current_section),
                        "heading": current_heading,
                        "metadata": {**(metadata or {}), "heading": current_heading}
                    })
                # Start new section
                current_heading = heading
                current_section = [line]
            else:
                current_section.append(line)
        
        # Add last section
        if current_section:
            chunks.append({
                "text": '\n'.join(current_section),
                "heading": current_heading,
                "metadata": {**(metadata or {}), "heading": current_heading}
            })
        
        return chunks
    
    def _is_heading(self, line: str) -> Optional[str]:
        """Check if line is a heading and return heading text"""
        line = line.strip()
        if not line:
            return None
        
        for pattern in self.heading_patterns:
            match = re.match(pattern, line)
            if match:
                return match.group(1).strip()
        
        return None

# Pros: Perfect for structured documents, preserves document organization
# Cons: Only works for documents with clear structure
```

## Choosing the Right Chunking Strategy

| Document Type | Best Strategy | Why |
|--------------|---------------|-----|
| Web articles | Semantic | Natural paragraph boundaries |
| Legal contracts | Document structure | Section-based retrieval critical |
| Research papers | Recursive | Mix of sections and paragraphs |
| Chat logs | Fixed-size | No natural boundaries |
| Product docs | Document structure | Follows user manual organization |
| Mixed content | Recursive | Handles everything well |

---

## Embeddings: The Magic Behind Semantic Search

Embeddings convert text into vectors (lists of numbers) that capture meaning. Similar texts have similar vectors.

```python
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class EmbeddingService:
    """
    Create and manage embeddings for semantic search
    """
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.dimension = self.model.get_sentence_embedding_dimension()
        
    def embed(self, texts: List[str]) -> np.ndarray:
        """
        Create embeddings for a list of texts
        """
        return self.model.encode(texts, show_progress_bar=True)
    
    def embed_single(self, text: str) -> np.ndarray:
        """
        Create embedding for a single text
        """
        return self.model.encode([text])[0]
    
    def similarity(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        """
        Calculate cosine similarity between two embeddings
        """
        return cosine_similarity([embedding1], [embedding2])[0][0]
    
    def search(self, query: str, documents: List[str], top_k: int = 5) -> List[Dict]:
        """
        Search for documents similar to query
        """
        # Embed query and documents
        query_emb = self.embed_single(query)
        doc_embs = self.embed(documents)
        
        # Calculate similarities
        similarities = cosine_similarity([query_emb], doc_embs)[0]
        
        # Get top k indices
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Format results
        results = []
        for idx in top_indices:
            results.append({
                "text": documents[idx],
                "similarity": float(similarities[idx]),
                "index": int(idx)
            })
        
        return results
    
    def visualize_embedding(self, text: str) -> Dict:
        """
        Visualize embedding properties (for debugging)
        """
        emb = self.embed_single(text)
        return {
            "text": text,
            "dimension": len(emb),
            "mean": float(np.mean(emb)),
            "std": float(np.std(emb)),
            "min": float(np.min(emb)),
            "max": float(np.max(emb)),
            "sample": emb[:10].tolist()  # First 10 values
        }

# Usage
embeddings = EmbeddingService()

# Create embeddings
texts = [
    "The weather in Tokyo is sunny today",
    "Paris is famous for its cuisine",
    "New York has many skyscrapers",
    "London weather is often rainy"
]
doc_embeddings = embeddings.embed(texts)

# Search
results = embeddings.search("What's the weather like?", texts)
for r in results:
    print(f"Score: {r['similarity']:.3f} - {r['text']}")
```

**Output:**
```
Score: 0.89 - The weather in Tokyo is sunny today
Score: 0.76 - London weather is often rainy
Score: 0.45 - Paris is famous for its cuisine
Score: 0.32 - New York has many skyscrapers
```

---

# Part 3.2: Vector Databases — Storing and Searching at Scale

When you have millions of documents, you need specialized databases for vector search.

## Pinecone — Fully Managed at Scale

```python
import pinecone
from pinecone import Pinecone, ServerlessSpec
import time

class PineconeVectorStore:
    """
    Vector store using Pinecone (fully managed)
    """
    
    def __init__(self, api_key: str, environment: str, index_name: str):
        # Initialize Pinecone
        pc = Pinecone(api_key=api_key)
        
        self.index_name = index_name
        self.dimension = 384  # all-MiniLM-L6-v2 dimension
        
        # Create index if doesn't exist
        if index_name not in pc.list_indexes().names():
            pc.create_index(
                name=index_name,
                dimension=self.dimension,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-west-2"
                )
            )
            # Wait for index to be ready
            while not pc.describe_index(index_name).status['ready']:
                time.sleep(1)
        
        self.index = pc.Index(index_name)
        self.embedding_service = EmbeddingService()
        
    def upsert(self, texts: List[str], metadatas: List[Dict] = None, ids: List[str] = None):
        """
        Insert or update vectors
        """
        # Create embeddings
        embeddings = self.embedding_service.embed(texts)
        
        # Prepare vectors
        vectors = []
        for i, (text, embedding) in enumerate(zip(texts, embeddings)):
            vector_id = ids[i] if ids else f"vec_{int(time.time())}_{i}"
            metadata = metadatas[i] if metadatas else {}
            metadata["text"] = text  # Store text in metadata
            
            vectors.append({
                "id": vector_id,
                "values": embedding.tolist(),
                "metadata": metadata
            })
        
        # Upsert in batches
        batch_size = 100
        for i in range(0, len(vectors), batch_size):
            batch = vectors[i:i + batch_size]
            self.index.upsert(vectors=batch)
            
        return len(vectors)
    
    def query(self, query_text: str, top_k: int = 5, filter: Dict = None) -> List[Dict]:
        """
        Query for similar vectors
        """
        # Create query embedding
        query_emb = self.embedding_service.embed_single(query_text)
        
        # Query Pinecone
        results = self.index.query(
            vector=query_emb.tolist(),
            top_k=top_k,
            include_metadata=True,
            filter=filter
        )
        
        return [{
            "id": match["id"],
            "score": match["score"],
            "text": match["metadata"].get("text", ""),
            "metadata": match["metadata"]
        } for match in results["matches"]]
    
    def delete(self, ids: List[str]):
        """
        Delete vectors by ID
        """
        self.index.delete(ids=ids)
    
    def update_metadata(self, id: str, metadata: Dict):
        """
        Update metadata for a vector
        """
        self.index.update(id=id, set_metadata=metadata)
    
    def describe_stats(self) -> Dict:
        """
        Get index statistics
        """
        return self.index.describe_index_stats()

# Usage
pinecone_store = PineconeVectorStore(
    api_key="your-api-key",
    environment="gcp-starter",
    index_name="knowledge-base"
)

# Add documents
texts = [
    "Our refund policy allows returns within 30 days",
    "Premium plan costs $49.99 per month",
    "Customer support is available 24/7 via chat"
]
pinecone_store.upsert(texts)

# Query
results = pinecone_store.query("What's your refund policy?")
for r in results:
    print(f"Score: {r['score']:.3f} - {r['text']}")
```

## Weaviate — Open Source with Hybrid Search

```python
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.query import HybridVector

class WeaviateVectorStore:
    """
    Vector store using Weaviate (open source, hybrid search)
    """
    
    def __init__(self, url: str = "http://localhost:8080"):
        # Connect to Weaviate
        self.client = weaviate.connect_to_local()
        
        self.collection_name = "Documents"
        self.embedding_service = EmbeddingService()
        
        self._create_collection()
        
    def _create_collection(self):
        """
        Create collection if doesn't exist
        """
        if not self.client.collections.exists(self.collection_name):
            self.client.collections.create(
                name=self.collection_name,
                properties=[
                    Property(name="text", data_type=DataType.TEXT),
                    Property(name="source", data_type=DataType.TEXT),
                    Property(name="category", data_type=DataType.TEXT),
                    Property(name="timestamp", data_type=DataType.DATE),
                ],
                # Enable hybrid search
                vectorizer_config=weaviate.classes.config.Configure.Vectorizer.none()
            )
    
    def add_documents(self, texts: List[str], metadatas: List[Dict] = None):
        """
        Add documents to Weaviate
        """
        collection = self.client.collections.get(self.collection_name)
        
        # Create embeddings
        embeddings = self.embedding_service.embed(texts)
        
        with collection.batch.fixed_size(batch_size=100) as batch:
            for i, (text, embedding) in enumerate(zip(texts, embeddings)):
                metadata = metadatas[i] if metadatas else {}
                
                batch.add_object(
                    properties={
                        "text": text,
                        **metadata
                    },
                    vector=embedding.tolist()
                )
    
    def hybrid_search(self, query: str, alpha: float = 0.5, limit: int = 5) -> List[Dict]:
        """
        Hybrid search combining vector and keyword
        alpha=0.5 means equal weight to vector and keyword
        """
        collection = self.client.collections.get(self.collection_name)
        
        # Create query embedding
        query_emb = self.embedding_service.embed_single(query)
        
        # Hybrid search
        response = collection.query.hybrid(
            query=query,
            vector=query_emb.tolist(),
            alpha=alpha,  # Balance between vector and keyword
            limit=limit
        )
        
        return [{
            "text": obj.properties["text"],
            "score": obj.metadata.score,
            "metadata": {k:v for k,v in obj.properties.items() if k != "text"}
        } for obj in response.objects]
    
    def vector_search(self, query: str, limit: int = 5) -> List[Dict]:
        """
        Pure vector search
        """
        collection = self.client.collections.get(self.collection_name)
        query_emb = self.embedding_service.embed_single(query)
        
        response = collection.query.near_vector(
            near_vector=query_emb.tolist(),
            limit=limit
        )
        
        return [{
            "text": obj.properties["text"],
            "metadata": {k:v for k,v in obj.properties.items() if k != "text"}
        } for obj in response.objects]
    
    def keyword_search(self, query: str, limit: int = 5) -> List[Dict]:
        """
        Pure keyword search (BM25)
        """
        collection = self.client.collections.get(self.collection_name)
        
        response = collection.query.bm25(
            query=query,
            limit=limit
        )
        
        return [{
            "text": obj.properties["text"],
            "score": obj.metadata.score,
            "metadata": {k:v for k,v in obj.properties.items() if k != "text"}
        } for obj in response.objects]

# Usage
weaviate_store = WeaviateVectorStore()

# Add documents
weaviate_store.add_documents(
    texts=[
        "Our refund policy allows returns within 30 days",
        "Premium plan costs $49.99 per month",
        "Customer support is available 24/7 via chat"
    ],
    metadatas=[
        {"source": "policy.pdf", "category": "policy"},
        {"source": "pricing.md", "category": "pricing"},
        {"source": "faq.txt", "category": "support"}
    ]
)

# Hybrid search (best of both worlds)
results = weaviate_store.hybrid_search("refund", alpha=0.5)
for r in results:
    print(f"Score: {r['score']:.3f} - {r['text']}")
```

## Chroma — Lightweight and Embedded

```python
import chromadb
from chromadb.config import Settings
import uuid

class ChromaVectorStore:
    """
    Vector store using Chroma (lightweight, embedded)
    """
    
    def __init__(self, persist_directory: str = "./chroma_db"):
        # Initialize Chroma
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=persist_directory
        ))
        
        self.embedding_service = EmbeddingService()
        
        # Create or get collection
        self.collection = self.client.get_or_create_collection(
            name="knowledge_base",
            metadata={"hnsw:space": "cosine"}
        )
        
    def add_documents(self, texts: List[str], metadatas: List[Dict] = None, ids: List[str] = None):
        """
        Add documents to Chroma
        """
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in texts]
        
        # Create embeddings
        embeddings = self.embedding_service.embed(texts)
        
        # Add to collection
        self.collection.add(
            documents=texts,
            embeddings=embeddings.tolist(),
            metadatas=metadatas or [{} for _ in texts],
            ids=ids
        )
        
        # Persist to disk
        self.client.persist()
        
        return ids
    
    def query(self, query_text: str, n_results: int = 5, filter_dict: Dict = None) -> List[Dict]:
        """
        Query for similar documents
        """
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results,
            where=filter_dict
        )
        
        formatted = []
        for i in range(len(results['ids'][0])):
            formatted.append({
                "id": results['ids'][0][i],
                "text": results['documents'][0][i],
                "metadata": results['metadatas'][0][i],
                "distance": results['distances'][0][i] if 'distances' in results else None
            })
        
        return formatted
    
    def get_by_ids(self, ids: List[str]) -> List[Dict]:
        """
        Get documents by IDs
        """
        results = self.collection.get(ids=ids)
        
        formatted = []
        for i in range(len(results['ids'])):
            formatted.append({
                "id": results['ids'][i],
                "text": results['documents'][i],
                "metadata": results['metadatas'][i]
            })
        
        return formatted
    
    def delete(self, ids: List[str]):
        """
        Delete documents by IDs
        """
        self.collection.delete(ids=ids)
        self.client.persist()
    
    def update(self, id: str, text: str = None, metadata: Dict = None):
        """
        Update a document
        """
        update_kwargs = {"ids": [id]}
        if text:
            update_kwargs["documents"] = [text]
            # Update embedding
            embedding = self.embedding_service.embed_single(text)
            update_kwargs["embeddings"] = [embedding.tolist()]
        if metadata:
            update_kwargs["metadatas"] = [metadata]
        
        self.collection.update(**update_kwargs)
        self.client.persist()
    
    def count(self) -> int:
        """
        Get number of documents
        """
        return self.collection.count()

# Usage
chroma_store = ChromaVectorStore()

# Add documents
chroma_store.add_documents(
    texts=[
        "The Eiffel Tower is in Paris",
        "London has the Big Ben",
        "Tokyo Tower is in Japan"
    ],
    metadatas=[
        {"country": "France", "type": "landmark"},
        {"country": "UK", "type": "landmark"},
        {"country": "Japan", "type": "landmark"}
    ]
)

# Query
results = chroma_store.query("Famous landmarks in Europe")
for r in results:
    print(f"Distance: {r['distance']:.3f} - {r['text']}")
```

## Qdrant — Rust-Powered Performance

```python
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import Distance, VectorParams
import uuid

class QdrantVectorStore:
    """
    Vector store using Qdrant (high performance, Rust)
    """
    
    def __init__(self, host: str = "localhost", port: int = 6333):
        # Connect to Qdrant
        self.client = QdrantClient(host=host, port=port)
        
        self.collection_name = "knowledge_base"
        self.vector_size = 384  # all-MiniLM-L6-v2 dimension
        self.embedding_service = EmbeddingService()
        
        self._create_collection()
        
    def _create_collection(self):
        """
        Create collection if doesn't exist
        """
        collections = self.client.get_collections().collections
        collection_names = [c.name for c in collections]
        
        if self.collection_name not in collection_names:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=self.vector_size,
                    distance=Distance.COSINE
                ),
                optimizers_config=models.OptimizersConfigDiff(
                    indexing_threshold=10000  # Start indexing after 10k points
                )
            )
            
            # Create payload indexes for faster filtering
            self.client.create_payload_index(
                collection_name=self.collection_name,
                field_name="source",
                field_schema=models.PayloadSchemaType.KEYWORD
            )
            self.client.create_payload_index(
                collection_name=self.collection_name,
                field_name="category",
                field_schema=models.PayloadSchemaType.KEYWORD
            )
    
    def upsert(self, texts: List[str], metadatas: List[Dict] = None) -> List[str]:
        """
        Insert or update vectors
        """
        # Create embeddings
        embeddings = self.embedding_service.embed(texts)
        
        # Prepare points
        points = []
        ids = []
        
        for i, (text, embedding) in enumerate(zip(texts, embeddings)):
            point_id = str(uuid.uuid4())
            ids.append(point_id)
            
            payload = metadatas[i] if metadatas else {}
            payload["text"] = text
            
            points.append(
                models.PointStruct(
                    id=point_id,
                    vector=embedding.tolist(),
                    payload=payload
                )
            )
        
        # Upsert in batches
        batch_size = 100
        for i in range(0, len(points), batch_size):
            batch = points[i:i + batch_size]
            self.client.upsert(
                collection_name=self.collection_name,
                points=batch
            )
        
        return ids
    
    def search(self, query_text: str, filter_conditions: Dict = None, limit: int = 5) -> List[Dict]:
        """
        Search with filtering
        """
        # Create query embedding
        query_emb = self.embedding_service.embed_single(query_text)
        
        # Build filter
        qdrant_filter = None
        if filter_conditions:
            must_conditions = []
            for key, value in filter_conditions.items():
                must_conditions.append(
                    models.FieldCondition(
                        key=key,
                        match=models.MatchValue(value=value)
                    )
                )
            qdrant_filter = models.Filter(must=must_conditions)
        
        # Execute search
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_emb.tolist(),
            query_filter=qdrant_filter,
            limit=limit,
            with_payload=True
        )
        
        return [{
            "id": r.id,
            "score": r.score,
            "text": r.payload.get("text", ""),
            "metadata": {k:v for k,v in r.payload.items() if k != "text"}
        } for r in results]
    
    def scroll(self, filter_conditions: Dict = None, limit: int = 100) -> List[Dict]:
        """
        Scroll through points (without vector search)
        """
        qdrant_filter = None
        if filter_conditions:
            must_conditions = []
            for key, value in filter_conditions.items():
                must_conditions.append(
                    models.FieldCondition(
                        key=key,
                        match=models.MatchValue(value=value)
                    )
                )
            qdrant_filter = models.Filter(must=must_conditions)
        
        results = self.client.scroll(
            collection_name=self.collection_name,
            scroll_filter=qdrant_filter,
            limit=limit,
            with_payload=True
        )[0]
        
        return [{
            "id": r.id,
            "text": r.payload.get("text", ""),
            "metadata": {k:v for k,v in r.payload.items() if k != "text"}
        } for r in results]
    
    def recommend(self, positive_ids: List[str], negative_ids: List[str] = None, limit: int = 5) -> List[Dict]:
        """
        Recommend similar items based on examples
        """
        results = self.client.recommend(
            collection_name=self.collection_name,
            positive=positive_ids,
            negative=negative_ids or [],
            limit=limit,
            with_payload=True
        )
        
        return [{
            "id": r.id,
            "score": r.score,
            "text": r.payload.get("text", ""),
            "metadata": {k:v for k,v in r.payload.items() if k != "text"}
        } for r in results]
    
    def delete(self, ids: List[str]):
        """
        Delete points by ID
        """
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=models.PointIdsList(
                points=ids
            )
        )
    
    def count(self) -> int:
        """
        Get collection size
        """
        return self.client.count(
            collection_name=self.collection_name
        ).count

# Usage
qdrant_store = QdrantVectorStore()

# Add documents
ids = qdrant_store.upsert(
    texts=[
        "Our refund policy allows returns within 30 days",
        "Premium plan costs $49.99 per month",
        "Customer support is available 24/7 via chat"
    ],
    metadatas=[
        {"source": "policy.pdf", "category": "policy"},
        {"source": "pricing.md", "category": "pricing"},
        {"source": "faq.txt", "category": "support"}
    ]
)

# Search with filter
results = qdrant_store.search(
    "refund",
    filter_conditions={"category": "policy"},
    limit=5
)
```

## Vector Database Comparison

| Feature | Pinecone | Weaviate | Milvus | Chroma | Qdrant |
|---------|----------|----------|--------|--------|--------|
| **Hosting** | Fully managed | Self/Cloud | Self/Cloud | Embedded | Self/Cloud |
| **Performance** | Excellent | Good | Excellent | Good | Excellent |
| **Filtering** | Good | Excellent | Good | Basic | Excellent |
| **Hybrid search** | No | Yes | Yes | No | Yes |
| **Setup complexity** | Low | Medium | High | Very low | Medium |
| **Best for** | Production | Enterprise | Billion scale | Dev/Prototyping | High perf |
| **Language** | Python | Go | C++/Go | Python | Rust |

---

# Part 3.3: RAG Frameworks

## LlamaIndex — Specialized for RAG

```python
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
    DocumentSummaryIndex,
    KeywordTableIndex,
    KnowledgeGraphIndex
)
from llama_index.core.node_parser import SentenceSplitter, SemanticSplitterNodeParser
from llama_index.core.retrievers import VectorIndexRetriever, RouterRetriever
from llama_index.core.query_engine import RetrieverQueryEngine, RouterQueryEngine
from llama_index.core.indices.query.query_transform import HyDEQueryTransform
from llama_index.core.postprocessor import SimilarityPostprocessor, MetadataReplacementPostProcessor
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
import os

class LlamaIndexRAG:
    """
    RAG system using LlamaIndex
    """
    
    def __init__(self, persist_dir: str = "./storage"):
        self.persist_dir = persist_dir
        self.embed_model = OpenAIEmbedding()
        self.llm = OpenAI(model="gpt-4", temperature=0)
        self.index = None
        self.query_engine = None
        
    def load_documents(self, directory_path: str):
        """
        Load documents from directory
        """
        reader = SimpleDirectoryReader(directory_path)
        documents = reader.load_data()
        print(f"📚 Loaded {len(documents)} documents")
        return documents
    
    def create_index(self, documents, chunk_size: int = 512, chunk_overlap: int = 50):
        """
        Create vector index from documents
        """
        # Configure parser
        parser = SentenceSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
        nodes = parser.get_nodes_from_documents(documents)
        print(f"📝 Created {len(nodes)} chunks")
        
        # Create index
        self.index = VectorStoreIndex(
            nodes,
            embed_model=self.embed_model,
            show_progress=True
        )
        
        # Persist index
        self.index.storage_context.persist(persist_dir=self.persist_dir)
        
        return self.index
    
    def create_semantic_index(self, documents):
        """
        Create index with semantic chunking
        """
        parser = SemanticSplitterNodeParser(
            embed_model=self.embed_model,
            chunk_size=512,
            chunk_overlap=50
        )
        
        nodes = parser.get_nodes_from_documents(documents)
        
        self.index = VectorStoreIndex(
            nodes,
            embed_model=self.embed_model
        )
        
        return self.index
    
    def load_index(self):
        """
        Load persisted index
        """
        storage_context = StorageContext.from_defaults(persist_dir=self.persist_dir)
        self.index = load_index_from_storage(storage_context)
        print(f"✅ Loaded index from {self.persist_dir}")
        return self.index
    
    def create_query_engine(self, similarity_top_k: int = 3, rerank: bool = True):
        """
        Create query engine with advanced options
        """
        # Base retriever
        retriever = VectorIndexRetriever(
            index=self.index,
            similarity_top_k=similarity_top_k
        )
        
        # Post-processors
        postprocessors = [
            SimilarityPostprocessor(similarity_cutoff=0.7)
        ]
        
        if rerank:
            from llama_index.core.postprocessor import LLMRerank
            postprocessors.append(
                LLMRerank(
                    llm=self.llm,
                    top_n=2
                )
            )
        
        # Query engine
        self.query_engine = RetrieverQueryEngine(
            retriever=retriever,
            node_postprocessors=postprocessors
        )
        
        return self.query_engine
    
    def create_hyde_engine(self):
        """
        Create engine with HyDE (Hypothetical Document Embeddings)
        Improves retrieval by generating hypothetical answer first
        """
        from llama_index.core.query_engine import TransformQueryEngine
        
        hyde = HyDEQueryTransform(llm=self.llm, include_original=True)
        
        base_engine = self.create_query_engine()
        
        self.query_engine = TransformQueryEngine(
            base_engine,
            hyde
        )
        
        return self.query_engine
    
    def create_router_engine(self):
        """
        Create engine that routes to different retrievers
        """
        from llama_index.core.tools import QueryEngineTool, ToolMetadata
        
        # Create different indices
        vector_tool = QueryEngineTool(
            query_engine=self.create_query_engine(),
            metadata=ToolMetadata(
                name="vector_search",
                description="Use for general questions and similarity search"
            )
        )
        
        # Keyword index for exact matching
        keyword_index = KeywordTableIndex.from_documents(
            self.index.docstore.docs.values()
        )
        keyword_tool = QueryEngineTool(
            query_engine=keyword_index.as_query_engine(),
            metadata=ToolMetadata(
                name="keyword_search",
                description="Use for exact keyword matching"
            )
        )
        
        # Router
        from llama_index.core.query_engine import RouterQueryEngine
        from llama_index.core.selectors import LLMSingleSelector
        
        self.query_engine = RouterQueryEngine(
            selector=LLMSingleSelector.from_defaults(llm=self.llm),
            query_engine_tools=[vector_tool, keyword_tool]
        )
        
        return self.query_engine
    
    async def query(self, question: str) -> Dict:
        """
        Query the RAG system
        """
        if not self.query_engine:
            self.create_query_engine()
        
        response = self.query_engine.query(question)
        
        # Format sources
        sources = []
        for node in response.source_nodes:
            sources.append({
                "text": node.node.text[:200] + "...",
                "score": node.score,
                "source": node.node.metadata.get("file_name", "Unknown")
            })
        
        return {
            "question": question,
            "answer": str(response),
            "sources": sources
        }
    
    def advanced_indexing_strategies(self, documents):
        """
        Demonstrate different indexing strategies
        """
        strategies = {}
        
        # 1. Summary index - good for summarization
        strategies["summary"] = DocumentSummaryIndex.from_documents(documents)
        
        # 2. Keyword table index - good for keyword lookup
        strategies["keyword"] = KeywordTableIndex.from_documents(documents)
        
        # 3. Knowledge graph index - for relationship extraction
        strategies["knowledge_graph"] = KnowledgeGraphIndex.from_documents(
            documents,
            llm=self.llm,
            max_triplets_per_chunk=5
        )
        
        # 4. Composable graph - combine multiple indices
        from llama_index.core.indices.composability import ComposableGraph
        
        strategies["composable"] = ComposableGraph.from_indices(
            VectorStoreIndex,
            [strategies["summary"], strategies["keyword"]],
            llm=self.llm
        )
        
        return strategies

# Usage
rag = LlamaIndexRAG()

# Load and index documents
docs = rag.load_documents("./knowledge_base")
rag.create_index(docs, chunk_size=512)

# Query
result = await rag.query("What is our refund policy?")
print(f"Answer: {result['answer']}")
print("Sources:")
for s in result['sources']:
    print(f"- {s['source']} (score: {s['score']:.3f})")
```

## LangChain Retrieval — Integrated with Agents

```python
from langchain.retrievers import (
    ContextualCompressionRetriever,
    EnsembleRetriever,
    MultiQueryRetriever,
    ParentDocumentRetriever
)
from langchain.retrievers.document_compressors import LLMChainExtractor, LLMChainFilter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader, TextLoader, PDFLoader
from langchain.storage import InMemoryStore
from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
import uuid

class LangChainRAG:
    """
    RAG system using LangChain
    """
    
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.llm = OpenAI(temperature=0)
        self.vectorstore = None
        self.retriever = None
        self.qa_chain = None
        
    def load_documents(self, directory: str):
        """
        Load documents from directory
        """
        # Load text files
        text_loader = DirectoryLoader(
            directory,
            glob="**/*.txt",
            loader_cls=TextLoader
        )
        text_docs = text_loader.load()
        
        # Load PDFs
        pdf_loader = DirectoryLoader(
            directory,
            glob="**/*.pdf",
            loader_cls=PDFLoader
        )
        pdf_docs = pdf_loader.load()
        
        all_docs = text_docs + pdf_docs
        print(f"📚 Loaded {len(all_docs)} documents")
        return all_docs
    
    def create_vectorstore(self, documents):
        """
        Create vector store from documents
        """
        # Split documents
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n\n", "\n", " ", ""]
        )
        splits = text_splitter.split_documents(documents)
        print(f"📝 Created {len(splits)} chunks")
        
        # Create vectorstore
        self.vectorstore = Chroma.from_documents(
            documents=splits,
            embedding=self.embeddings,
            persist_directory="./chroma_db"
        )
        
        return self.vectorstore
    
    def create_basic_retriever(self, k: int = 4):
        """
        Create basic similarity retriever
        """
        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": k}
        )
        return self.retriever
    
    def create_multi_query_retriever(self):
        """
        Generate multiple queries from original to improve recall
        """
        self.retriever = MultiQueryRetriever.from_llm(
            retriever=self.vectorstore.as_retriever(),
            llm=self.llm
        )
        return self.retriever
    
    def create_compression_retriever(self):
        """
        Compress retrieved documents to extract only relevant parts
        """
        # Base retriever
        base_retriever = self.vectorstore.as_retriever(search_kwargs={"k": 5})
        
        # Compressor that extracts relevant sentences
        compressor = LLMChainExtractor.from_llm(self.llm)
        
        self.retriever = ContextualCompressionRetriever(
            base_compressor=compressor,
            base_retriever=base_retriever
        )
        
        return self.retriever
    
    def create_ensemble_retriever(self, documents):
        """
        Combine multiple retrieval strategies
        """
        # Vector retriever
        vector_retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 3}
        )
        
        # BM25 retriever (keyword-based)
        from langchain.retrievers import BM25Retriever
        bm25_retriever = BM25Retriever.from_documents(documents)
        bm25_retriever.k = 3
        
        # Ensemble
        self.retriever = EnsembleRetriever(
            retrievers=[vector_retriever, bm25_retriever],
            weights=[0.5, 0.5]
        )
        
        return self.retriever
    
    def create_parent_retriever(self, documents):
        """
        Parent Document Retriever - retrieves small chunks but returns full parent
        """
        # Create stores
        vectorstore = Chroma(
            collection_name="chunks",
            embedding_function=self.embeddings
        )
        store = InMemoryStore()
        
        # Create retriever
        self.retriever = ParentDocumentRetriever(
            vectorstore=vectorstore,
            docstore=store,
            child_splitter=RecursiveCharacterTextSplitter(chunk_size=400),
            parent_splitter=RecursiveCharacterTextSplitter(chunk_size=2000)
        )
        
        # Add documents
        self.retriever.add_documents(documents)
        
        return self.retriever
    
    def create_qa_chain(self):
        """
        Create QA chain with retriever
        """
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",  # "stuff", "map_reduce", "refine", "map_rerank"
            retriever=self.retriever,
            return_source_documents=True,
            verbose=True
        )
        
        return self.qa_chain
    
    async def query(self, question: str) -> Dict:
        """
        Query the RAG system
        """
        if not self.qa_chain:
            self.create_qa_chain()
        
        result = self.qa_chain.invoke({"query": question})
        
        return {
            "question": question,
            "answer": result["result"],
            "sources": [
                {
                    "content": doc.page_content[:200] + "...",
                    "metadata": doc.metadata
                }
                for doc in result["source_documents"]
            ]
        }
    
    def create_custom_chain(self):
        """
        Create custom retrieval chain with prompt
        """
        from langchain.chains import RetrievalQA
        from langchain.prompts import PromptTemplate
        
        prompt_template = """Use the following pieces of context to answer the question at the end. 
        If you don't know the answer, just say you don't know. Don't try to make up an answer.
        
        Context:
        {context}
        
        Question: {question}
        
        Answer the question in a helpful, detailed way. If the answer comes from specific sources, mention them.
        
        Answer:"""
        
        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            chain_type_kwargs={"prompt": PROMPT},
            return_source_documents=True
        )
        
        return self.qa_chain

# Usage
rag = LangChainRAG()

# Load and index
docs = rag.load_documents("./knowledge_base")
rag.create_vectorstore(docs)

# Use advanced retriever
rag.create_compression_retriever()

# Query
result = await rag.query("What's our refund policy for international flights?")
print(f"Answer: {result['answer']}")
```

## Haystack — Production Pipelines

```python
from haystack import Pipeline, Document
from haystack.document_stores import InMemoryDocumentStore, ElasticsearchDocumentStore
from haystack.nodes import (
    TextConverter,
    PDFToTextConverter,
    PreProcessor,
    EmbeddingRetriever,
    BM25Retriever,
    PromptNode,
    AnswerParser,
    JoinDocuments,
    SentenceTransformersRanker,
    FARMReader
)
from haystack.pipelines import ExtractiveQAPipeline, Pipeline
from haystack.utils import print_answers
import os

class HaystackRAG:
    """
    RAG system using Haystack
    """
    
    def __init__(self):
        # Initialize document store
        self.document_store = InMemoryDocumentStore(
            embedding_dim=384,
            similarity="cosine"
        )
        
        self.retriever = None
        self.pipeline = None
        
    def index_documents(self, file_paths: List[str]):
        """
        Index documents into document store
        """
        # Conversion nodes
        text_converter = TextConverter()
        pdf_converter = PDFToTextConverter()
        
        # Preprocessing
        preprocessor = PreProcessor(
            clean_empty_lines=True,
            clean_whitespace=True,
            clean_header_footer=True,
            split_by="word",
            split_length=200,
            split_overlap=20,
            split_respect_sentence_boundary=True
        )
        
        # Process each file
        all_docs = []
        for file_path in file_paths:
            print(f"📄 Processing: {file_path}")
            
            # Choose converter based on file type
            if file_path.endswith('.pdf'):
                converter = pdf_converter
            else:
                converter = text_converter
            
            # Convert to text
            docs = converter.convert(file_path=file_path)
            
            # Preprocess
            docs = preprocessor.process(docs)
            
            all_docs.extend(docs)
        
        # Write to document store
        self.document_store.write_documents(all_docs)
        print(f"📚 Indexed {len(all_docs)} documents")
        
        # Create embeddings
        self.retriever = EmbeddingRetriever(
            document_store=self.document_store,
            embedding_model="sentence-transformers/all-MiniLM-L6-v2",
            model_format="sentence_transformers"
        )
        
        self.document_store.update_embeddings(self.retriever)
        
        return len(all_docs)
    
    def create_rag_pipeline(self):
        """
        Create a RAG pipeline
        """
        pipeline = Pipeline()
        
        # Add retriever
        pipeline.add_node(
            component=self.retriever,
            name="Retriever",
            inputs=["Query"]
        )
        
        # Add prompt node for generation
        prompt_node = PromptNode(
            model_name_or_path="gpt-4",
            default_prompt_template="""Answer the question based on the provided documents.
            
Documents:
{join(documents)}
            
Question: {query}
            
Answer the question in a helpful way. If you're unsure, say so. Always base your answer on the documents provided.
Answer:""",
            output_variable="answers",
            api_key=os.getenv("OPENAI_API_KEY"),
            max_length=500
        )
        
        pipeline.add_node(
            component=prompt_node,
            name="PromptNode",
            inputs=["Retriever"]
        )
        
        self.pipeline = pipeline
        return pipeline
    
    def create_extractive_pipeline(self):
        """
        Create extractive QA pipeline (finds exact answer spans)
        """
        # Add reader for extractive QA
        reader = FARMReader(
            model_name_or_path="deepset/roberta-base-squad2",
            use_gpu=False
        )
        
        pipeline = ExtractiveQAPipeline(
            reader=reader,
            retriever=self.retriever
        )
        
        self.pipeline = pipeline
        return pipeline
    
    def create_hybrid_pipeline(self):
        """
        Create hybrid search pipeline (keyword + vector)
        """
        pipeline = Pipeline()
        
        # Sparse retriever (BM25)
        sparse_retriever = BM25Retriever(document_store=self.document_store)
        
        # Dense retriever (embeddings)
        dense_retriever = EmbeddingRetriever(
            document_store=self.document_store,
            embedding_model="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        pipeline.add_node(
            component=sparse_retriever,
            name="SparseRetriever",
            inputs=["Query"]
        )
        
        pipeline.add_node(
            component=dense_retriever,
            name="DenseRetriever",
            inputs=["Query"]
        )
        
        # Join results
        join_node = JoinDocuments(join_mode="concatenate")
        pipeline.add_node(
            component=join_node,
            name="Join",
            inputs=["SparseRetriever", "DenseRetriever"]
        )
        
        # Add ranker
        ranker = SentenceTransformersRanker(
            model_name_or_path="cross-encoder/ms-marco-MiniLM-L-6-v2"
        )
        pipeline.add_node(
            component=ranker,
            name="Ranker",
            inputs=["Join"]
        )
        
        self.pipeline = pipeline
        return pipeline
    
    async def query(self, question: str, top_k: int = 3) -> Dict:
        """
        Query the pipeline
        """
        if not self.pipeline:
            self.create_rag_pipeline()
        
        result = self.pipeline.run(
            query=question,
            params={"Retriever": {"top_k": top_k}}
        )
        
        # Format response
        answers = []
        if "answers" in result:
            for answer in result["answers"]:
                answers.append({
                    "answer": answer.answer,
                    "score": answer.score,
                    "context": answer.context
                })
        
        documents = []
        if "documents" in result:
            for doc in result["documents"]:
                documents.append({
                    "content": doc.content[:200] + "...",
                    "score": doc.score,
                    "meta": doc.meta
                })
        
        return {
            "question": question,
            "answers": answers,
            "documents": documents
        }
    
    def evaluate(self, eval_questions: List[str], eval_answers: List[str]) -> Dict:
        """
        Evaluate RAG performance
        """
        from haystack.eval import EvaluationResult
        
        results = []
        correct = 0
        
        for q, expected in zip(eval_questions, eval_answers):
            result = self.query(q)
            
            # Simple evaluation (in production, use proper metrics)
            if result["answers"]:
                actual = result["answers"][0]["answer"]
                if expected.lower() in actual.lower():
                    correct += 1
            
            results.append({
                "question": q,
                "expected": expected,
                "actual": result["answers"][0]["answer"] if result["answers"] else None
            })
        
        accuracy = correct / len(eval_questions)
        
        return {
            "accuracy": accuracy,
            "correct": correct,
            "total": len(eval_questions),
            "results": results
        }

# Usage
rag = HaystackRAG()

# Index documents
rag.index_documents([
    "./knowledge_base/policies.pdf",
    "./knowledge_base/faqs.txt",
    "./knowledge_base/product_docs.pdf"
])

# Create hybrid pipeline
rag.create_hybrid_pipeline()

# Query
result = await rag.query("How do I change my flight booking?")
for ans in result["answers"]:
    print(f"Answer: {ans['answer']} (score: {ans['score']:.3f})")
```

---

# Part 3.4: Multi-Agent Systems — When One Agent Isn't Enough

*"Complex problems need specialized teams, not generalists."*

## Why Multi-Agent Systems?

| Single Agent | Multi-Agent System |
|--------------|-------------------|
| Jack of all trades, master of none | Specialized experts |
| Single perspective | Multiple viewpoints |
| Sequential thinking | Parallel processing |
| Single point of failure | Distributed responsibility |
| Hard to scale | Easy to add new agents |
| Limited by context window | Shared memory across agents |

**Real-world analogy:** A startup founder (single agent) tries to do everything — product, sales, marketing, support. A company (multi-agent) has specialists: CEO, CTO, sales lead, marketing manager, support team. The company scales; the founder burns out.

---

## Pattern 1: Planner-Executor

One agent creates a plan, multiple executors carry it out.

```python
from typing import List, Dict, Any
from enum import Enum
import asyncio

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class Task:
    def __init__(self, id: str, description: str, assigned_to: str, dependencies: List[str] = None):
        self.id = id
        self.description = description
        self.assigned_to = assigned_to
        self.dependencies = dependencies or []
        self.status = TaskStatus.PENDING
        self.result = None

class ExecutorAgent:
    """Base class for executor agents"""
    
    def __init__(self, name: str, capabilities: List[str], llm):
        self.name = name
        self.capabilities = capabilities
        self.llm = llm
        
    async def execute(self, task: Task) -> Any:
        """Execute a specific task"""
        print(f"🔧 Executor {self.name} working on: {task.description}")
        
        # In real implementation, this would use tools/APIs
        await asyncio.sleep(1)  # Simulate work
        
        return f"Result from {self.name}: {task.description} completed"

class VenueExecutor(ExecutorAgent):
    """Specialized in venue booking"""
    
    async def execute(self, task: Task) -> Any:
        print(f"🏨 Venue expert: {task.description}")
        # Search venue APIs, check availability, compare prices
        return {
            "venue": "Grand Hotel",
            "capacity": 200,
            "price": 15000,
            "available_dates": ["2024-06-15", "2024-06-22"]
        }

class CateringExecutor(ExecutorAgent):
    """Specialized in catering"""
    
    async def execute(self, task: Task) -> Any:
        print(f"🍽️ Catering expert: {task.description}")
        return {
            "menu": ["appetizers", "main course", "dessert"],
            "dietary_options": ["vegetarian", "vegan", "gluten-free"],
            "price_per_person": 85
        }

class PlannerAgent:
    """Creates plans and coordinates executors"""
    
    def __init__(self, llm):
        self.llm = llm
        self.executors = {}
        self.tasks = []
        self.results = {}
        
    def register_executor(self, executor: ExecutorAgent):
        """Register an executor agent"""
        self.executors[executor.name] = executor
        print(f"✅ Registered executor: {executor.name}")
        
    async def create_plan(self, user_request: str) -> List[Task]:
        """
        Break down request into tasks with dependencies
        """
        # Get executor capabilities
        capabilities = {}
        for name, executor in self.executors.items():
            capabilities[name] = executor.capabilities
        
        prompt = f"""
User request: "{user_request}"

Available executors and their capabilities:
{json.dumps(capabilities, indent=2)}

Break this request into specific tasks that can be executed independently.
For each task, provide:
- id: Unique identifier (e.g., "task1", "task2")
- description: Clear description of what needs to be done
- assigned_to: Which executor should handle this
- dependencies: List of task IDs that must be completed first

Consider task dependencies carefully. For example:
- Venue must be booked before catering can be planned
- Budget must be set before any bookings

Return as JSON array.
"""
        response = await self.llm(prompt)
        
        try:
            tasks_data = json.loads(response)
            for task_data in tasks_data:
                task = Task(
                    id=task_data['id'],
                    description=task_data['description'],
                    assigned_to=task_data['assigned_to'],
                    dependencies=task_data.get('dependencies', [])
                )
                self.tasks.append(task)
        except Exception as e:
            print(f"Error parsing plan: {e}")
            # Fallback plan
            self.tasks = [
                Task(id="task1", description="Set budget", assigned_to="budget", dependencies=[]),
                Task(id="task2", description="Find venue", assigned_to="venue", dependencies=["task1"]),
                Task(id="task3",description="Plan catering", assigned_to="catering", dependencies=["task2"])
            ]
        
        print(f"📋 Created plan with {len(self.tasks)} tasks")
        return self.tasks
    
    async def execute_plan(self) -> Dict[str, Any]:
        """
        Execute tasks respecting dependencies
        """
        task_map = {task.id: task for task in self.tasks}
        completed = set()
        in_progress = set()
        
        while len(completed) < len(self.tasks):
            # Find tasks ready to execute
            ready_tasks = []
            for task in self.tasks:
                if task.id in completed or task.id in in_progress:
                    continue
                    
                # Check dependencies
                deps_satisfied = all(dep in completed for dep in task.dependencies)
                if deps_satisfied:
                    ready_tasks.append(task)
            
            if not ready_tasks:
                print("⚠️ Deadlock detected!")
                break
            
            print(f"\n🚀 Executing {len(ready_tasks)} tasks in parallel:")
            for task in ready_tasks:
                print(f"  • {task.id}: {task.description} → {task.assigned_to}")
                task.status = TaskStatus.IN_PROGRESS
                in_progress.add(task.id)
            
            # Run tasks concurrently
            tasks_to_run = []
            for task in ready_tasks:
                executor = self.executors.get(task.assigned_to)
                if executor:
                    tasks_to_run.append(self._execute_task(task, executor))
                else:
                    print(f"⚠️ No executor for {task.assigned_to}")
                    task.status = TaskStatus.FAILED
                    completed.add(task.id)
            
            if tasks_to_run:
                results = await asyncio.gather(*tasks_to_run, return_exceptions=True)
                
                for task, result in zip(ready_tasks, results):
                    if isinstance(result, Exception):
                        print(f"❌ Task {task.id} failed: {result}")
                        task.status = TaskStatus.FAILED
                    else:
                        task.status = TaskStatus.COMPLETED
                        task.result = result
                        self.results[task.id] = result
                    
                    completed.add(task.id)
                    in_progress.remove(task.id)
        
        return self.results
    
    async def _execute_task(self, task: Task, executor: ExecutorAgent) -> Any:
        """Execute a single task"""
        return await executor.execute(task)
    
    async def synthesize_results(self) -> str:
        """Combine all results into a coherent response"""
        context = "Task results:\n"
        for task_id, result in self.results.items():
            task = next(t for t in self.tasks if t.id == task_id)
            context += f"\n{task.description}:\n{json.dumps(result, indent=2)}\n"
        
        prompt = f"""
Based on the following task results, create a comprehensive response:

{context}

Synthesize the information into a clear, helpful response.
Include all key details and recommendations.
"""
        return await self.llm(prompt)

# Wedding planner example
class WeddingPlannerSystem:
    def __init__(self):
        self.llm = OpenAI(temperature=0.7)
        self.planner = PlannerAgent(self.llm)
        
        # Register executors
        self.planner.register_executor(VenueExecutor("venue", ["venue", "location"], self.llm))
        self.planner.register_executor(CateringExecutor("catering", ["food", "catering"], self.llm))
        self.planner.register_executor(ExecutorAgent("budget", ["budget", "cost"], self.llm))
        self.planner.register_executor(ExecutorAgent("photography", ["photo", "video"], self.llm))
        self.planner.register_executor(ExecutorAgent("music", ["music", "dj"], self.llm))
        
    async def plan_wedding(self, request: str) -> str:
        print(f"💍 Wedding planning request: {request}")
        
        # Create plan
        tasks = await self.planner.create_plan(request)
        
        # Execute plan
        results = await self.planner.execute_plan()
        
        # Synthesize response
        response = await self.planner.synthesize_results()
        
        return response

# Usage
wedding_planner = WeddingPlannerSystem()
response = await wedding_planner.plan_wedding(
    "Plan a wedding for 150 people in June with $50,000 budget"
)
print(response)
```

## Pattern 2: Supervisor Agent

A supervisor coordinates specialists, maintaining conversation flow.

```python
from enum import Enum

class AgentSpecialty(Enum):
    SALES = "sales"
    SUPPORT = "support"
    BILLING = "billing"
    TECHNICAL = "technical"
    GENERAL = "general"

class SpecializedAgent:
    """Specialized agent for a domain"""
    
    def __init__(self, name: str, specialty: AgentSpecialty, llm):
        self.name = name
        self.specialty = specialty
        self.llm = llm
        self.conversation_history = []
        
    async def handle(self, user_message: str, context: dict) -> str:
        """Handle message within specialty"""
        self.conversation_history.append({"role": "user", "content": user_message})
        
        # Specialty prompts
        prompts = {
            AgentSpecialty.SALES: "You are a sales expert. Focus on product benefits and closing deals.",
            AgentSpecialty.SUPPORT: "You are a support specialist. Be patient and solve problems.",
            AgentSpecialty.BILLING: "You are a billing expert. Handle payments and invoices accurately.",
            AgentSpecialty.TECHNICAL: "You are a technical expert. Provide detailed solutions.",
            AgentSpecialty.GENERAL: "You are a helpful assistant."
        }
        
        prompt = f"""
{prompts[self.specialty]}

Context: {json.dumps(context, indent=2)}

Conversation:
{self._format_history()}

User: {user_message}

Respond:
"""
        response = await self.llm(prompt)
        self.conversation_history.append({"role": "assistant", "content": response})
        return response
    
    def _format_history(self) -> str:
        return "\n".join([
            f"{m['role']}: {m['content']}"
            for m in self.conversation_history[-5:]
        ])

class SupervisorAgent:
    """Coordinates specialized agents"""
    
    def __init__(self, llm):
        self.llm = llm
        self.specialists = {}
        self.current_specialist = None
        self.context = {
            "user_id": None,
            "topic": None,
            "sentiment": "neutral",
            "escalation_count": 0
        }
        
    def register_specialist(self, agent: SpecializedAgent):
        """Register a specialist agent"""
        self.specialists[agent.specialty] = agent
        
    async def route_query(self, message: str) -> AgentSpecialty:
        """Determine which specialist should handle this"""
        available = [s.value for s in self.specialists.keys()]
        
        prompt = f"""
User: "{message}"

Available: {available}

Which specialist should handle this? Consider:
- Sales: buying, pricing, products
- Support: problems, how-to, troubleshooting
- Billing: payments, invoices, refunds
- Technical: technical issues, code
- General: anything else

Respond with just the specialty name:
"""
        response = await self.llm(prompt)
        specialty_str = response.strip().lower()
        
        for specialty in AgentSpecialty:
            if specialty.value == specialty_str:
                return specialty
        
        return AgentSpecialty.GENERAL
    
    async def detect_sentiment(self, message: str) -> str:
        """Detect user sentiment"""
        prompt = f"Message: '{message}'\nSentiment (positive/negative/neutral):"
        response = await self.llm(prompt)
        return response.strip().lower()
    
    async def should_escalate(self, message: str, response: str) -> bool:
        """Check if escalation needed"""
        prompt = f"""
User: {message}
Agent: {response}

Should this be escalated to a different specialist? (yes/no)
"""
        result = await self.llm(prompt)
        return result.strip().lower() == "yes"
    
    async def process(self, user_id: str, message: str) -> str:
        """Main message processing"""
        
        # Update context
        self.context["user_id"] = user_id
        self.context["sentiment"] = await self.detect_sentiment(message)
        
        # Route to specialist
        specialty = await self.route_query(message)
        
        if self.current_specialist is None or self.current_specialist.specialty != specialty:
            print(f"🔄 Switching to {specialty.value} specialist")
            self.current_specialist = self.specialists[specialty]
            self.context["topic"] = specialty.value
        
        # Get response
        response = await self.current_specialist.handle(message, self.context)
        
        # Check escalation
        if await self.should_escalate(message, response):
            self.context["escalation_count"] += 1
            
            if self.context["escalation_count"] > 2:
                return "Let me connect you with a human agent who can better assist you."
            
            # Try another specialist
            other = [s for s in self.specialists.keys() if s != specialty]
            if other:
                print(f"⚠️ Escalating to {other[0].value}")
                self.current_specialist = self.specialists[other[0]]
                response = await self.current_specialist.handle(
                    message, 
                    {**self.context, "escalated_from": specialty.value}
                )
        
        return response

# Customer service system
class CustomerServiceSystem:
    def __init__(self):
        self.llm = OpenAI(temperature=0.3)
        self.supervisor = SupervisorAgent(self.llm)
        
        # Register specialists
        self.supervisor.register_specialist(
            SpecializedAgent("sales", AgentSpecialty.SALES, self.llm)
        )
        self.supervisor.register_specialist(
            SpecializedAgent("support", AgentSpecialty.SUPPORT, self.llm)
        )
        self.supervisor.register_specialist(
            SpecializedAgent("billing", AgentSpecialty.BILLING, self.llm)
        )
        self.supervisor.register_specialist(
            SpecializedAgent("technical", AgentSpecialty.TECHNICAL, self.llm)
        )
        
    async def chat(self, user_id: str, message: str) -> str:
        return await self.supervisor.process(user_id, message)

# Example conversation
async def demo_customer_service():
    cs = CustomerServiceSystem()
    
    messages = [
        ("How much does premium cost?"),
        ("Actually, I'm having trouble with my current plan"),
        ("I was charged twice this month"),
        ("This is really frustrating!")
    ]
    
    for msg in messages:
        print(f"\n📱 User: {msg}")
        response = await cs.chat("user123", msg)
        print(f"💬 Agent: {response}")
```

## Pattern 3: Debate Agents

Multiple agents argue different positions to reach better conclusions.

```python
class DebateAgent:
    """Agent that takes a specific stance in a debate"""
    
    def __init__(self, name: str, stance: str, llm):
        self.name = name
        self.stance = stance
        self.llm = llm
        self.arguments = []
        
    async def present_argument(self, topic: str, context: str = "") -> str:
        """Present initial argument"""
        prompt = f"""
You are {self.name}, taking the {self.stance} stance on this topic.

Topic: {topic}
Context: {context}

Present your strongest argument for the {self.stance} position.
Be persuasive, use evidence and logic.
"""
        argument = await self.llm(prompt)
        self.arguments.append({"round": len(self.arguments), "argument": argument})
        return argument
    
    async def rebuttal(self, topic: str, opposing_arguments: List[str]) -> str:
        """Respond to opposing arguments"""
        prompt = f"""
You are {self.name}, taking the {self.stance} stance.

Topic: {topic}

Opposing arguments:
{chr(10).join([f'- {arg}' for arg in opposing_arguments])}

Provide a rebuttal. Address each opposing point, defend your position,
and strengthen your original argument.
"""
        rebuttal = await self.llm(prompt)
        self.arguments.append({"round": len(self.arguments), "rebuttal": rebuttal})
        return rebuttal

class DebateModerator:
    """Moderates debate and synthesizes conclusions"""
    
    def __init__(self, llm):
        self.llm = llm
        self.agents = []
        self.history = []
        
    def add_agent(self, agent: DebateAgent):
        self.agents.append(agent)
        
    async def conduct_debate(self, topic: str, rounds: int = 2) -> Dict:
        """Conduct multi-round debate"""
        
        print(f"\n🎯 Debate Topic: {topic}\n")
        
        # Round 1: Opening statements
        print("📢 Round 1 - Opening Statements")
        round1_args = []
        for agent in self.agents:
            arg = await agent.present_argument(topic)
            print(f"\n{agent.name} ({agent.stance}):\n{arg[:200]}...\n")
            round1_args.append(arg)
            self.history.append({
                "round": 1,
                "agent": agent.name,
                "stance": agent.stance,
                "content": arg
            })
        
        # Subsequent rounds: Rebuttals
        for round_num in range(2, rounds + 1):
            print(f"⚔️ Round {round_num} - Rebuttals")
            round_args = []
            
            for agent in self.agents:
                opposing = [
                    h["content"] for h in self.history 
                    if h["round"] == round_num - 1 and h["agent"] != agent.name
                ]
                
                rebuttal = await agent.rebuttal(topic, opposing)
                print(f"\n{agent.name}:\n{rebuttal[:200]}...\n")
                round_args.append(rebuttal)
                self.history.append({
                    "round": round_num,
                    "agent": agent.name,
                    "stance": agent.stance,
                    "content": rebuttal
                })
        
        # Synthesis
        synthesis = await self.synthesize(topic)
        
        return {
            "topic": topic,
            "history": self.history,
            "synthesis": synthesis
        }
    
    async def synthesize(self, topic: str) -> str:
        """Synthesize all perspectives"""
        summary = "\n".join([
            f"Round {h['round']} - {h['agent']} ({h['stance']}): {h['content'][:100]}..."
            for h in self.history
        ])
        
        prompt = f"""
Debate Topic: {topic}

Debate Summary:
{summary}

Synthesize this debate into a balanced, insightful conclusion that:
1. Summarizes key arguments from each perspective
2. Identifies areas of agreement
3. Highlights strongest points from each side
4. Provides practical recommendations

The synthesis should be neutral and helpful.
"""
        return await self.llm(prompt)

# Investment advisor with debate
class InvestmentAdvisor:
    def __init__(self):
        self.llm = OpenAI(temperature=0.7)
        self.moderator = DebateModerator(self.llm)
        
        # Create agents with different perspectives
        self.moderator.add_agent(DebateAgent("Bull", "aggressive growth", self.llm))
        self.moderator.add_agent(DebateAgent("Bear", "conservative defensive", self.llm))
        self.moderator.add_agent(DebateAgent("Value", "undervalued assets", self.llm))
        self.moderator.add_agent(DebateAgent("Technical", "market trends", self.llm))
        
    async def advise(self, query: str) -> str:
        """Get investment advice through debate"""
        
        result = await self.moderator.conduct_debate(query, rounds=2)
        
        return f"""
📊 **Investment Analysis: {query}**

{result['synthesis']}

**Key Perspectives:**
• Bull: {self._extract_point(result['history'], 'Bull')}
• Bear: {self._extract_point(result['history'], 'Bear')}
• Value: {self._extract_point(result['history'], 'Value')}
• Technical: {self._extract_point(result['history'], 'Technical')}

*This is for informational purposes only. Not financial advice.*
"""
    
    def _extract_point(self, history, agent_name):
        for h in reversed(history):
            if h['agent'] == agent_name:
                return h['content'][:150] + "..."
        return "No data"

# Usage
advisor = InvestmentAdvisor()
advice = await advisor.advise("Should I invest in AI stocks right now?")
print(advice)
```

## Pattern 4: Swarm Model

Decentralized agents work in parallel, sharing results.

```python
import asyncio
from dataclasses import dataclass
from typing import List, Any
import uuid
import time

@dataclass
class Message:
    """Message in swarm communication"""
    id: str
    sender: str
    content: Any
    msg_type: str  # "query", "result", "update"
    timestamp: float

class Blackboard:
    """Shared memory for swarm agents"""
    
    def __init__(self):
        self.messages = []
        self.results = {}
        self.tasks = []
        self.lock = asyncio.Lock()
        
    async def post(self, message: Message):
        """Post message to blackboard"""
        async with self.lock:
            self.messages.append(message)
            if message.msg_type == "result":
                self.results[message.sender] = message.content
                
    async def get_messages(self, since: float = 0) -> List[Message]:
        """Get messages since timestamp"""
        async with self.lock:
            return [m for m in self.messages if m.timestamp > since]
    
    async def add_task(self, task: dict):
        """Add task for agents"""
        async with self.lock:
            self.tasks.append(task)
    
    async def get_tasks(self, agent_type: str = None) -> List[dict]:
        """Get tasks for agent type"""
        async with self.lock:
            if agent_type:
                return [t for t in self.tasks if t.get('type') == agent_type]
            return self.tasks

class SwarmAgent:
    """Individual agent in the swarm"""
    
    def __init__(self, agent_id: str, agent_type: str, capabilities: List[str], llm):
        self.id = agent_id
        self.type = agent_type
        self.capabilities = capabilities
        self.llm = llm
        self.blackboard = None
        self.knowledge = {}
        self.last_check = 0
        
    def connect(self, blackboard: Blackboard):
        """Connect to blackboard"""
        self.blackboard = blackboard
        
    async def run(self):
        """Main agent loop"""
        while True:
            # Check for new messages
            messages = await self.blackboard.get_messages(self.last_check)
            self.last_check = time.time()
            
            for msg in messages:
                await self._handle_message(msg)
            
            # Check for tasks
            tasks = await self.blackboard.get_tasks(self.type)
            for task in tasks:
                await self._execute_task(task)
            
            # Proactively contribute
            await self._contribute()
            
            await asyncio.sleep(1)
    
    async def _handle_message(self, message: Message):
        """Handle incoming message"""
        if message.msg_type == "query" and self._can_answer(message.content):
            answer = await self._answer_question(message.content)
            await self.blackboard.post(Message(
                id=str(uuid.uuid4()),
                sender=self.id,
                content=answer,
                msg_type="result",
                timestamp=time.time()
            ))
        elif message.msg_type == "result":
            self.knowledge[message.sender] = message.content
    
    async def _execute_task(self, task: dict):
        """Execute assigned task"""
        print(f"🐝 {self.id} executing: {task['description']}")
        
        # Simulate work
        await asyncio.sleep(2)
        
        # Generate result
        result = await self.llm(f"Task: {task['description']}\nGenerate findings:")
        
        await self.blackboard.post(Message(
            id=str(uuid.uuid4()),
            sender=self.id,
            content={
                "task_id": task.get('id'),
                "result": result,
                "findings": self._extract_findings(result)
            },
            msg_type="result",
            timestamp=time.time()
        ))
    
    async def _contribute(self):
        """Proactively contribute findings"""
        if self.knowledge and random.random() < 0.3:  # 30% chance
            synthesis = await self.llm(f"Synthesize: {json.dumps(self.knowledge)}")
            await self.blackboard.post(Message(
                id=str(uuid.uuid4()),
                sender=self.id,
                content=synthesis,
                msg_type="update",
                timestamp=time.time()
            ))
    
    def _can_answer(self, query: str) -> bool:
        """Check if agent can answer query"""
        query_lower = query.lower()
        return any(cap.lower() in query_lower for cap in self.capabilities)
    
    async def _answer_question(self, query: str) -> str:
        """Answer a question"""
        context = f"Knowledge: {json.dumps(self.knowledge)}"
        return await self.llm(f"{context}\n\nQuestion: {query}\nAnswer:")
    
    def _extract_findings(self, text: str) -> List[str]:
        """Extract key findings"""
        # Simplified
        return [text[:100]]

class SwarmCoordinator:
    """Coordinates the swarm"""
    
    def __init__(self, llm):
        self.llm = llm
        self.blackboard = Blackboard()
        self.agents = []
        
    def add_agent(self, agent: SwarmAgent):
        agent.connect(self.blackboard)
        self.agents.append(agent)
        
    async def start(self):
        """Start all swarm agents"""
        tasks = [agent.run() for agent in self.agents]
        await asyncio.gather(*tasks)
        
    async def assign_task(self, task_description: str) -> Dict:
        """Assign a task to the swarm"""
        
        # Break into subtasks
        subtasks = await self._decompose_task(task_description)
        
        for subtask in subtasks:
            await self.blackboard.add_task(subtask)
        
        # Wait for results
        await asyncio.sleep(5)
        
        # Collect results
        results = list(self.blackboard.results.values())
        
        # Synthesize
        final = await self._synthesize_results(task_description, results)
        
        return final
    
    async def _decompose_task(self, task: str) -> List[dict]:
        """Break task into subtasks"""
        agent_types = list(set([a.type for a in self.agents]))
        
        prompt = f"""
Task: {task}

Available agent types: {agent_types}

Break this task into smaller subtasks that can be worked on in parallel.
For each subtask, specify:
- id: unique identifier
- description: what to do
- type: which agent type should handle it

Return as JSON array.
"""
        response = await self.llm(prompt)
        return json.loads(response)
    
    async def _synthesize_results(self, original_task: str, results: List[dict]) -> str:
        """Synthesize all results"""
        context = f"Task: {original_task}\n\nResults:\n"
        for r in results:
            context += json.dumps(r, indent=2) + "\n"
        
        return await self.llm(f"{context}\nSynthesize into comprehensive answer:")

# Market research swarm
class MarketResearchSwarm:
    def __init__(self):
        self.llm = OpenAI(temperature=0.5)
        self.coordinator = SwarmCoordinator(self.llm)
        
        # Create specialized agents
        agent_types = [
            ("competitor", ["competitor", "market share", "pricing"]),
            ("customer", ["customer", "feedback", "satisfaction"]),
            ("trend", ["trend", "innovation", "future"]),
            ("financial", ["revenue", "profit", "valuation"]),
            ("product", ["product", "features", "quality"]),
        ]
        
        for i, (atype, caps) in enumerate(agent_types):
            agent = SwarmAgent(
                agent_id=f"agent_{i}",
                agent_type=atype,
                capabilities=caps,
                llm=self.llm
            )
            self.coordinator.add_agent(agent)
    
    async def research(self, query: str) -> str:
        """Conduct market research"""
        print(f"🔍 Starting market research: {query}")
        print("🐝 Releasing swarm agents...")
        
        # Start swarm in background
        asyncio.create_task(self.coordinator.start())
        
        # Assign task
        result = await self.coordinator.assign_task(query)
        
        return result

# Usage
swarm = MarketResearchSwarm()
result = await swarm.research(
    "Analyze the competitive landscape for AI writing assistants"
)
print(result)
```

---

# Part 3.5: Multi-Agent Frameworks

## AutoGen — Conversational Multi-Agent

```python
import autogen
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

class AutoGenPlanner:
    """Multi-agent travel planner using AutoGen"""
    
    def __init__(self):
        # Configuration
        config_list = [
            {
                'model': 'gpt-4',
                'api_key': os.getenv("OPENAI_API_KEY"),
            }
        ]
        
        llm_config = {
            "config_list": config_list,
            "temperature": 0.7,
            "timeout": 120
        }
        
        # Create specialized agents
        self.flight_agent = AssistantAgent(
            name="FlightExpert",
            system_message="""You are a flight booking expert. You help find and book flights.
            You have access to flight search APIs. Always provide specific options with prices.
            When you have flight options, say "FLIGHTS_READY" and list them.""",
            llm_config=llm_config
        )
        
        self.hotel_agent = AssistantAgent(
            name="HotelExpert",
            system_message="""You are a hotel booking specialist. Provide detailed hotel recommendations
            with prices and locations. When you have hotel options, say "HOTELS_READY".""",
            llm_config=llm_config
        )
        
        self.activity_agent = AssistantAgent(
            name="ActivityExpert",
            system_message="""You are a local activities expert. Suggest attractions, restaurants,
            and things to do. When you have suggestions, say "ACTIVITIES_READY".""",
            llm_config=llm_config
        )
        
        self.coordinator = AssistantAgent(
            name="Coordinator",
            system_message="""You are the travel coordinator. Gather information from the user,
            delegate to specialists, and synthesize their recommendations into a complete itinerary.
            Wait for all specialists to report "READY" before presenting the final plan.""",
            llm_config=llm_config
        )
        
        self.user_proxy = UserProxyAgent(
            name="User",
            human_input_mode="NEVER",
            code_execution_config=False,
            max_consecutive_auto_reply=10
        )
        
    async def plan_trip(self, user_request: str) -> str:
        """Plan a trip using multi-agent collaboration"""
        
        groupchat = GroupChat(
            agents=[self.user_proxy, self.coordinator, self.flight_agent, 
                    self.hotel_agent, self.activity_agent],
            messages=[],
            max_round=20
        )
        
        manager = GroupChatManager(
            groupchat=groupchat,
            llm_config={"config_list": [{"model": "gpt-4", "api_key": os.getenv("OPENAI_API_KEY")}]}
        )
        
        self.user_proxy.initiate_chat(
            manager,
            message=f"I need help planning a trip: {user_request}"
        )
        
        return groupchat.messages[-1]['content']

# Usage
planner = AutoGenPlanner()
response = await planner.plan_trip(
    "I want to visit Tokyo for 5 days next month with a budget of $3000"
)
print(response)
```

## CrewAI — Role-Based Teams

```python
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

class ContentCreationCrew:
    """Content creation team with specialized roles"""
    
    def __init__(self):
        self.search_tool = SerperDevTool()
        self.scrape_tool = ScrapeWebsiteTool()
        
    def create_agents(self):
        """Create specialized agents"""
        
        researcher = Agent(
            role='Senior Research Analyst',
            goal='Uncover comprehensive information on the topic',
            backstory="""You are an experienced research analyst with a knack for finding 
            the most relevant and up-to-date information.""",
            tools=[self.search_tool, self.scrape_tool],
            verbose=True,
            allow_delegation=False
        )
        
        writer = Agent(
            role='Content Writer',
            goal='Create engaging, well-structured content',
            backstory="""You are a talented writer who transforms research into 
            compelling narratives.""",
            verbose=True,
            allow_delegation=True
        )
        
        editor = Agent(
            role='Senior Editor',
            goal='Ensure content meets quality standards',
            backstory="""You are a meticulous editor with an eye for detail.""",
            verbose=True,
            allow_delegation=False
        )
        
        seo = Agent(
            role='SEO Specialist',
            goal='Optimize content for search engines',
            backstory="""You are an SEO expert who balances keywords with readability.""",
            tools=[self.search_tool],
            verbose=True,
            allow_delegation=False
        )
        
        return {
            'researcher': researcher,
            'writer': writer,
            'editor': editor,
            'seo': seo
        }
    
    def create_tasks(self, agents, topic: str):
        """Create tasks for each agent"""
        
        research_task = Task(
            description=f"""
            Research the topic: '{topic}'
            
            Find:
            1. Key statistics and data points
            2. Expert opinions and quotes
            3. Current trends and developments
            4. Competitor analysis
            
            Compile into a detailed research brief.
            """,
            agent=agents['researcher'],
            expected_output="A comprehensive research brief"
        )
        
        write_task = Task(
            description=f"""
            Using the research brief, write a comprehensive article about '{topic}'.
            
            Requirements:
            - Engaging headline
            - Well-structured with subheadings
            - 1500-2000 words
            - Include key statistics and quotes
            """,
            agent=agents['writer'],
            expected_output="A complete first draft"
        )
        
        seo_task = Task(
            description=f"""
            Optimize the article for SEO:
            1. Identify primary and secondary keywords
            2. Optimize headline and subheadings
            3. Add meta description
            4. Suggest internal linking opportunities
            
            Provide SEO recommendations.
            """,
            agent=agents['seo'],
            expected_output="SEO optimization report"
        )
        
        edit_task = Task(
            description=f"""
            Review and edit the article:
            1. Check for grammar and spelling errors
            2. Ensure consistent tone
            3. Verify all facts
            4. Apply SEO recommendations
            
            Provide the final polished version.
            """,
            agent=agents['editor'],
            expected_output="Final edited article"
        )
        
        return [research_task, write_task, seo_task, edit_task]
    
    async def create_content(self, topic: str) -> str:
        """Run the content creation crew"""
        
        agents = self.create_agents()
        tasks = self.create_tasks(agents, topic)
        
        crew = Crew(
            agents=list(agents.values()),
            tasks=tasks,
            verbose=2,
            process=Process.sequential
        )
        
        result = crew.kickoff()
        return result

# Usage
crew = ContentCreationCrew()
article = await crew.create_content("The Future of AI in Healthcare")
print(article)
```

## LangGraph — Graph-Based Workflows

```python
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
from langgraph.checkpoint import MemorySaver
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
import operator

# Define state
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    user_id: str
    intent: str
    sentiment: float
    escalation_level: int
    resolved: bool

# Define nodes (agents)
async def triage_agent(state: AgentState) -> AgentState:
    """Determine user intent"""
    llm = ChatOpenAI(model="gpt-4")
    
    last_message = state["messages"][-1].content
    
    prompt = f"""
Analyze this user message and determine intent:
"{last_message}"

Categories:
- technical: Technical issues, bugs
- billing: Payments, invoices, refunds
- account: Login, profile, settings
- feature: How-to, capabilities
- complaint: Negative feedback
- other: Anything else

Return just the category.
"""
    intent = await llm.ainvoke(prompt)
    state["intent"] = intent.content.strip()
    
    return state

async def technical_support(state: AgentState) -> AgentState:
    """Handle technical issues"""
    llm = ChatOpenAI(model="gpt-4")
    
    response = await llm.ainvoke([
        {"role": "system", "content": "You are a technical support specialist."},
        *state["messages"]
    ])
    
    state["messages"].append(AIMessage(content=response.content))
    return state

async def billing_support(state: AgentState) -> AgentState:
    """Handle billing issues"""
    llm = ChatOpenAI(model="gpt-4")
    
    response = await llm.ainvoke([
        {"role": "system", "content": "You are a billing specialist."},
        *state["messages"]
    ])
    
    state["messages"].append(AIMessage(content=response.content))
    return state

async def account_support(state: AgentState) -> AgentState:
    """Handle account issues"""
    llm = ChatOpenAI(model="gpt-4")
    
    response = await llm.ainvoke([
        {"role": "system", "content": "You are an account specialist."},
        *state["messages"]
    ])
    
    state["messages"].append(AIMessage(content=response.content))
    return state

async def complaint_handler(state: AgentState) -> AgentState:
    """Handle complaints"""
    llm = ChatOpenAI(model="gpt-4")
    
    response = await llm.ainvoke([
        {"role": "system", "content": "You handle complaints with empathy."},
        *state["messages"]
    ])
    
    state["messages"].append(AIMessage(content=response.content))
    return state

async def human_escalation(state: AgentState) -> AgentState:
    """Escalate to human"""
    state["messages"].append(AIMessage(
        content="Connecting you with a human agent..."
    ))
    return state

def build_support_graph():
    """Build the support workflow graph"""
    
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("triage", triage_agent)
    workflow.add_node("technical", technical_support)
    workflow.add_node("billing", billing_support)
    workflow.add_node("account", account_support)
    workflow.add_node("complaint", complaint_handler)
    workflow.add_node("human", human_escalation)
    
    # Set entry point
    workflow.set_entry_point("triage")
    
    # Conditional edges from triage
    workflow.add_conditional_edges(
        "triage",
        lambda state: state["intent"],
        {
            "technical": "technical",
            "billing": "billing",
            "account": "account",
            "complaint": "complaint",
            "other": "technical"  # Default
        }
    )
    
    # All support nodes go to human for now (simplified)
    for node in ["technical", "billing", "account", "complaint"]:
        workflow.add_edge(node, "human")
    
    workflow.add_edge("human", END)
    
    return workflow.compile()

class LangGraphSupport:
    """Customer support using LangGraph"""
    
    def __init__(self):
        self.graph = build_support_graph()
        self.threads = {}
        
    async def process_message(self, user_id: str, message: str) -> str:
        """Process message through graph"""
        
        if user_id not in self.threads:
            self.threads[user_id] = {
                "config": {"configurable": {"thread_id": user_id}},
                "state": {
                    "messages": [],
                    "user_id": user_id,
                    "intent": "",
                    "sentiment": 0.0,
                    "escalation_level": 0,
                    "resolved": False
                }
            }
        
        thread = self.threads[user_id]
        thread["state"]["messages"].append(HumanMessage(content=message))
        
        final_state = await self.graph.ainvoke(
            thread["state"],
            config=thread["config"]
        )
        
        thread["state"] = final_state
        
        for msg in reversed(final_state["messages"]):
            if isinstance(msg, AIMessage):
                return msg.content
        
        return "How can I help you?"

# Usage
support = LangGraphSupport()
response = await support.process_message(
    "user123", 
    "I can't log into my account"
)
print(response)
```

---

## 🎯 Summary: What You've Learned in Part 3

✅ **RAG Systems Fundamentals**
- Document loading and preprocessing
- Chunking strategies (fixed, semantic, recursive, structure-based)
- Embeddings for semantic search
- Complete RAG pipeline

✅ **Vector Databases**
- Pinecone: Fully managed, easy to use
- Weaviate: Hybrid search, open source
- Milvus: Billion-scale, GPU acceleration
- Chroma: Lightweight, embedded
- Qdrant: Rust-powered, high performance

✅ **RAG Frameworks**
- LlamaIndex: Specialized for RAG, advanced indexing
- LangChain Retrieval: Integrated with agents
- Haystack: Production pipelines, evaluation

✅ **Multi-Agent Patterns**
- Planner-Executor: Task decomposition
- Supervisor: Coordination and routing
- Debate: Multiple perspectives
- Swarm: Parallel processing

✅ **Multi-Agent Frameworks**
- AutoGen: Conversational agents
- CrewAI: Role-based teams
- LangGraph: Graph-based workflows
- Semantic Kernel: Enterprise integration

---

## 👀 Preview: What's Coming in Part 4

In the next story, we'll focus on safety and reliability:

**Evaluation & Guardrails**
- Hallucination detection
- Red teaming your agents
- Output validation
- Bias mitigation
- Tools: LangSmith, TruLens, DeepEval, Guardrails AI

**Observability for Agents**
- Token usage tracking
- Latency monitoring
- Cost per request
- Drift detection
- Tools: Prometheus, Grafana, LangSmith, Helicon

**By the end of Part 4, you'll know how to make your agents safe, measurable, and production-ready.**

---

## 🚀 Your Mission for This Week

1. Build a RAG system with your own documents
2. Experiment with different chunking strategies and compare results
3. Set up a vector database (try Chroma for local development)
4. Build a multi-agent system with at least 2 specialized agents
5. Test with a complex scenario requiring multiple agents

---

**Coming up next in Part 4: Keeping Agents Safe — Evaluation, Guardrails, and Observability**

*Don't miss it! Follow me to get notified when the next story drops.*

---

*[End of Story 3 — 15,234 words]*

---

**[Click here for Story 4 →]** (Link to be added)

---
*� Questions? Drop a response - I read and reply to every comment.*
*📌 Save this story to your reading list - it helps other engineers discover it.*
**🔗 Follow me →**
- [**Medium**](mvineetsharma.medium.com) - mvineetsharma.medium.com
- [**LinkedIn**](www.linkedin.com/in/vineet-sharma-architect) -  www.linkedin.com/in/vineet-sharma-architect

*In-depth .NET, Node.js, Python, Cloud Architecture, and System Design. New articles weekly*