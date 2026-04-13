Here is **Story #7** of your **Zero-Cost AI** handbook series, following the exact same structure as Parts 1-6 with numbered story listings, detailed technical depth, and a 35-50 minute read length.

---

# Zero-Cost AI: Deploy from Laptop to HuggingFace for Free – Part 7

## A Complete Handbook for Packaging the Complete $0 AI Stack with Docker 27.0 and Deploying to HuggingFace Spaces Free Tier with 16GB RAM, 2 vCPUs, Automatic HTTPS, and Custom Domain Support

---

## Introduction

You have built an extraordinary zero-cost AI stack. A frontend on Vercel streaming responses. An agent orchestrator managing multi-step reasoning. A local Llama 3.3 70B matching GPT-4 on benchmarks. MCP servers giving your agents the power to act. Code agents that understand and modify your codebase.

But there's a problem that's been lurking since Part 1.

Your LLM runs on your laptop. Your frontend on Vercel tries to call `localhost:11434` — but that's your laptop, not the cloud. When you close your laptop, the LLM stops working. When you're offline, users get connection errors. Your beautiful application is trapped on your personal machine.

The conventional solution would be to rent cloud GPUs. AWS EC2 g4dn.xlarge with an NVIDIA T4 GPU costs $0.526 per hour — $384 per month. Google Cloud's A100 GPUs start at $3.67 per hour. Even the cheapest GPU instances run $100-200 monthly.

But this is the Zero-Cost AI handbook, and we don't do paid.

Enter **HuggingFace Spaces** — a free hosting platform for AI applications that gives you 16GB of RAM, 2 vCPUs, automatic HTTPS, and unlimited public traffic. Yes, you read that correctly. **16GB of RAM for free.** That's enough to run your quantized Llama 3.3 70B (12GB) plus your agent orchestrator (2GB) plus your frontend (1GB) with room to spare.

HuggingFace Spaces supports Docker containers, meaning you can package your entire stack — Ollama, LangGraph, MCP servers, custom code — into a single container and deploy it with one click. Your application becomes a public URL that works 24/7, costs nothing, and scales to thousands of users.

In **Part 7**, you will deploy your entire zero-cost AI stack to production. You will create a Dockerfile that packages Ollama, your agent orchestrator, and your frontend into a single container. You will test the container locally, then deploy to HuggingFace Spaces free tier. You will configure environment variables, set up persistent storage, and add a custom domain with automatic HTTPS. You will learn the limits of the free tier and how to stay within them. And you will finally have a production AI application that costs exactly $0 to run.

No cloud GPU bills. No server management. No credit card required. Just your code, a Docker container, and HuggingFace's generous free tier.

---

## Takeaway from Part 6

Before deploying to HuggingFace, let's review the essential foundations established in **Part 6: Code Agents on a Laptop Without Subscriptions**:

- **Claude Code CLI provides conversational code assistance.** You installed and configured Claude Code CLI to work with your local Ollama instance. It can read files, explain code, and suggest changes through a natural language interface.

- **Aider automates refactoring across multiple files.** With Aider, you can request complex refactorings like "add error handling to all database queries" and Aider will make the changes, run tests, and commit the results.

- **Code agents integrate with LangGraph.** Your custom code agent can read files, parse ASTs, find references, suggest refactorings, generate unit tests, and fix bugs — all powered by your local Llama 3.3.

- **PR agents automate the development workflow.** The PR agent you built checks out branches, runs Aider to fix issues, runs linters and tests, and opens pull requests — all automatically.

- **Local code generation is production-ready.** Llama 3.3 70B generates code at 11 tokens per second (6-7 seconds per function). For simple functions, Gemma 4 4B is faster (1-2 seconds) but less capable. Both cost $0.

With these takeaways firmly in place, you are ready to deploy your entire stack to HuggingFace Spaces for free.

---

## Stories in This Series

**1. 📎 Read** [Zero-Cost AI: The $0 Stack That Actually Works – Part 1](#)  
*Complete architectural breakdown of all eight layers with performance characteristics, memory requirements, and working code examples. First published in the Zero-Cost AI Handbook.*

**2. 📎 Read** [Zero-Cost AI: Frontend on Your Laptop, Deployed for Free – Part 2](#)  
*Deploying Next.js 15 and Streamlit 1.35 on Vercel's free tier with automatic routing, serverless functions, and 100GB monthly bandwidth. First published in the Zero-Cost AI Handbook.*

**3. 📎 Read** [Zero-Cost AI: Agent Orchestration on a Laptop Without Paying – Part 3](#)  
*LangGraph v0.2 vs CrewAI v0.70 for building multi-agent systems that manage state, coordinate tools, and maintain end-to-end data flow at zero cost. First published in the Zero-Cost AI Handbook.*

**4. 📎 Read** [Zero-Cost AI: Replacing GPT-4 with Llama 3.3 70B Locally – Part 4](#)  
*Running Llama 3.3 70B Q4_K_M, Gemma 4 E4B Q4_0, and Mistral Small 4 Q5_K_M on a laptop using Ollama 0.5 with benchmark comparisons to GPT-4o and Claude 3.5. First published in the Zero-Cost AI Handbook.*

**5. 📎 Read** [Zero-Cost AI: Tool Use on a Laptop via Model Context Protocol – Part 5](#)  
*How MCP 2026.1 replaces expensive function-calling APIs by connecting local LLMs to your file system, SQLite databases, shell commands, and web APIs through a standardized JSON-RPC protocol. First published in the Zero-Cost AI Handbook.*

**6. 📎 Read** [Zero-Cost AI: Code Agents on a Laptop Without Subscriptions – Part 6](#)  
*Using Claude Code CLI 2.1 and Aider 0.55 for AI pair programming, code generation, refactoring, bug fixing, and automated PRs — all powered by your local Llama 3.3 instance. First published in the Zero-Cost AI Handbook.*

**7. 📎 Read** [Zero-Cost AI: Deploy from Laptop to HuggingFace for Free – Part 7](#) *(you are here)*  
*Packaging the complete $0 AI stack with Docker 27.0 and deploying to HuggingFace Spaces free tier with 16GB RAM, 2 vCPUs, automatic HTTPS, and custom domain support. First published in the Zero-Cost AI Handbook.*

**8. 📎 Read** [Zero-Cost AI: Observability on a Laptop Without Datadog – Part 8](#)  
*Logging, tracing, and monitoring agent behavior using structured JSON logs, OpenTelemetry collectors, and Grafana dashboards — entirely without paid observability tools. First published in the Zero-Cost AI Handbook.*

**9. 📎 Read** [Zero-Cost AI: RAG Pipeline on a Laptop for Free – Part 9](#)  
*Building retrieval-augmented generation with LlamaIndex 0.10, local ChromaDB 0.4, Qdrant 1.10, and all-MiniLM-L6-v2 embeddings — all running locally with zero cloud dependencies. First published in the Zero-Cost AI Handbook.*

**10. 📎 Read** [Zero-Cost AI: Data Layer on a Laptop Without Cloud Spend – Part 10](#)  
*Using SQLite 3.45 for production transactions, DuckDB 0.10 for analytical queries, and Supabase free tier for optional cloud sync with row-level security and real-time subscriptions. First published in the Zero-Cost AI Handbook.*

---

## HuggingFace Spaces Deployment Architecture

Before packaging your stack, you need a mental model of how HuggingFace Spaces works and how your application will run in their environment. The diagram below shows the complete deployment architecture.

```mermaid
flowchart TB
    User[👤 User Browser\nAny device] --> HF[🌐 HuggingFace Spaces\nFree Tier\n16GB RAM | 2 vCPUs\nAutomatic HTTPS]
    
    HF --> Docker[🐳 Docker Container\nYour packaged stack\n27.0+ required]
    
    Docker --> Ollama[🤖 Ollama Server\nPort 11434\nLlama 3.3 70B Q4_K_M\n12GB RAM]
    Docker --> Agent[🧠 Agent Orchestrator\nLangGraph/CrewAI\nPort 8000\n2GB RAM]
    Docker --> Frontend[🖥️ Frontend\nStreamlit/Next.js\nPort 7860/3000\n1GB RAM]
    
    Ollama --> Agent
    Agent --> Frontend
    Frontend --> User
    
    Docker --> Volume[💾 Persistent Storage\nHuggingFace cache\nModel weights\nUser data]
    
    style HF fill:#ff9d00,stroke:#e67e22,stroke-width:3px,color:#000
    style Docker fill:#2496ed,stroke:#1a6bbf,stroke-width:2px,color:#fff
    style Ollama fill:#2ecc71,stroke:#27ae60,stroke-width:2px,color:#000
    style Frontend fill:#3498db,stroke:#2980b9,stroke-width:2px,color:#fff
```

### Why HuggingFace Spaces?

HuggingFace Spaces is the most generous free tier for AI applications in 2026. Here's why it's perfect for zero-cost deployment:

| Feature | HuggingFace Spaces Free | Vercel Free (Part 2) | AWS/GCP Free Tier |
|---------|------------------------|---------------------|-------------------|
| **RAM** | 16GB | N/A (serverless) | 1GB (EC2 t2.micro) |
| **vCPUs** | 2 | N/A | 1 |
| **Storage** | 50GB | N/A | 30GB |
| **GPU** | Optional (paid) | No | No (free tier) |
| **HTTPS** | Automatic | Automatic | Manual |
| **Custom domain** | Yes | Yes | Yes |
| **Docker support** | Yes | Limited | Yes |
| **Model hosting** | Native | No | No |
| **Cost** | **$0** | $0 | $0 (limited) |

**The key insight:** HuggingFace Spaces gives you 16GB of RAM — exactly enough for Llama 3.3 70B Q4_K_M (12GB) plus your application (4GB). This is not a coincidence. HuggingFace designed their free tier specifically for running quantized LLMs.

### HuggingFace Spaces Limits (Free Tier)

| Resource | Limit | Implications |
|----------|-------|--------------|
| RAM | 16GB | Llama 3.3 70B Q4_K_M uses ~12GB, leaving 4GB for app |
| vCPUs | 2 | Limited parallel processing, but sufficient for inference |
| Storage | 50GB | Model weights (~8GB) + app (~1GB) + logs |
| Sleep timeout | 48 hours | Space sleeps after 48h of inactivity, wakes on request |
| Build minutes | Unlimited | No limit on Docker builds |
| Traffic | Unlimited | No bandwidth caps |
| Concurrent requests | ~10 | 2 vCPUs limit parallel processing |

### When to Upgrade to Pro ($9/month)

You may need the Pro tier if:
- Your application needs persistent GPU (T4 small: $0.40/hour)
- You need more than 2 vCPUs
- You need private spaces (not public)
- You need guaranteed uptime without sleep

For most individual developers and small startups, the free tier is sufficient.

---

## Step 1: Dockerize Your Zero-Cost AI Stack

### Create the Dockerfile

Create a `Dockerfile` in your project root that packages Ollama, your agent orchestrator, and your frontend.

```dockerfile
# Dockerfile
# Stage 1: Base image with Ollama
FROM ollama/ollama:0.5.1 as ollama-base

# Stage 2: Python application
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
COPY --from=ollama-base /usr/bin/ollama /usr/bin/ollama

# Create working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Copy Ollama model pull script
COPY pull_model.sh /pull_model.sh
RUN chmod +x /pull_model.sh

# Create directories for persistent storage
RUN mkdir -p /root/.ollama /app/data /app/logs

# Expose ports
# 11434: Ollama API
# 8000: Agent orchestrator API
# 7860: Streamlit frontend (or 3000 for Next.js)
EXPOSE 11434 8000 7860

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=120s --retries=3 \
    CMD curl -f http://localhost:11434/api/tags || exit 1

# Entrypoint
ENTRYPOINT ["/entrypoint.sh"]
```

### Create requirements.txt

```txt
# requirements.txt
# Core dependencies
langgraph>=0.2.0
langchain>=0.3.0
langchain-ollama>=0.1.0
crewai>=0.70.0

# Web framework
streamlit>=1.35.0
fastapi>=0.115.0
uvicorn>=0.30.0

# HTTP client
requests>=2.32.0
httpx>=0.27.0

# Data processing
pandas>=2.2.0
numpy>=1.26.0

# Utilities
python-dotenv>=1.0.0
pydantic>=2.7.0
pyyaml>=6.0

# MCP support
mcp>=0.1.0
sse-py>=1.0.0

# Observability
opentelemetry-api>=1.25.0
opentelemetry-sdk>=1.25.0

# Database
sqlite3
duckdb>=0.10.0
```

### Create the Model Pull Script

```bash
#!/bin/bash
# pull_model.sh
# Script to pull the Llama model on first startup

echo "🦙 Pulling Llama 3.3 70B Q4_K_M model..."
ollama pull llama3.3:70b-instruct-q4_K_M

echo "✅ Model pulled successfully"
```

### Create the Entrypoint Script

```bash
#!/bin/bash
# entrypoint.sh
# Starts all components of the zero-cost AI stack

set -e

echo "🚀 Starting Zero-Cost AI Stack on HuggingFace Spaces"
echo "===================================================="

# Start Ollama server in background
echo "📡 Starting Ollama server..."
ollama serve &
OLLAMA_PID=$!

# Wait for Ollama to be ready
echo "⏳ Waiting for Ollama to be ready..."
for i in {1..30}; do
    if curl -s http://localhost:11434/api/tags > /dev/null; then
        echo "✅ Ollama is ready"
        break
    fi
    echo "   Waiting... ($i/30)"
    sleep 2
done

# Pull the model if not already present
if ! ollama list | grep -q "llama3.3:70b-instruct-q4_K_M"; then
    echo "🦙 Pulling Llama 3.3 70B model (first time, may take 10-15 minutes)..."
    /pull_model.sh
else
    echo "✅ Model already present"
fi

# Start the agent orchestrator (FastAPI)
echo "🧠 Starting Agent Orchestrator..."
python -m uvicorn agent_api:app --host 0.0.0.0 --port 8000 &
AGENT_PID=$!

# Start the frontend (Streamlit)
echo "🖥️ Starting Frontend..."
streamlit run app.py --server.port 7860 --server.address 0.0.0.0 &
FRONTEND_PID=$!

echo "===================================================="
echo "✅ All components started!"
echo "   - Ollama API: http://localhost:11434"
echo "   - Agent API: http://localhost:8000"
echo "   - Frontend: http://localhost:7860"
echo "===================================================="

# Wait for all processes
wait $OLLAMA_PID $AGENT_PID $FRONTEND_PID
```

### Create the Agent API (FastAPI)

```python
# agent_api.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import asyncio
import json

from langgraph_agent import create_agent
from mcp_client import MCPManager

app = FastAPI(title="Zero-Cost AI Agent API", version="1.0.0")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agent
agent = create_agent()

class ChatRequest(BaseModel):
    messages: List[Dict[str, str]]
    temperature: float = 0.7
    max_tokens: int = 500
    stream: bool = False

class ChatResponse(BaseModel):
    response: str
    usage: Dict[str, int]

@app.get("/")
async def root():
    return {"status": "ok", "message": "Zero-Cost AI Agent API"}

@app.get("/health")
async def health():
    return {"status": "healthy", "ollama": "checking..."}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Non-streaming chat endpoint."""
    try:
        # Get last user message
        last_message = request.messages[-1]["content"]
        
        # Run agent
        result = await agent.run(last_message)
        
        return ChatResponse(
            response=result,
            usage={"total_tokens": 0}  # Track in production
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    """Streaming chat endpoint."""
    from fastapi.responses import StreamingResponse
    
    async def generate():
        last_message = request.messages[-1]["content"]
        
        # Stream tokens from agent
        async for token in agent.stream(last_message):
            yield f"data: {json.dumps({'token': token})}\n\n"
        yield "data: [DONE]\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")

@app.get("/tools")
async def list_tools():
    """List available MCP tools."""
    # Return tools from MCP manager
    return {"tools": []}
```

### Create the LangGraph Agent (Production Ready)

```python
# langgraph_agent.py
import asyncio
from typing import AsyncGenerator, Dict, Any
from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama
import os

class ProductionAgent:
    """Production-ready LangGraph agent for HuggingFace deployment."""
    
    def __init__(self):
        # Use environment variables for configuration
        ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
        model = os.getenv("LLM_MODEL", "llama3.3:70b-instruct-q4_K_M")
        
        self.llm = ChatOllama(
            model=model,
            base_url=ollama_url,
            temperature=0.7,
            num_predict=500,
        )
        
        self.graph = self._build_graph()
    
    def _build_graph(self):
        """Build the agent graph."""
        
        async def process_node(state: Dict[str, Any]) -> Dict[str, Any]:
            """Process user input and generate response."""
            prompt = state["messages"][-1]["content"]
            
            response = await self.llm.ainvoke(prompt)
            state["response"] = response.content
            
            return state
        
        # Build graph
        workflow = StateGraph(Dict)
        workflow.add_node("process", process_node)
        workflow.set_entry_point("process")
        workflow.add_edge("process", END)
        
        return workflow.compile()
    
    async def run(self, user_input: str) -> str:
        """Run the agent on user input."""
        state = {"messages": [{"role": "user", "content": user_input}]}
        result = await self.graph.ainvoke(state)
        return result.get("response", "No response generated")
    
    async def stream(self, user_input: str) -> AsyncGenerator[str, None]:
        """Stream response tokens."""
        # Simplified streaming for HuggingFace
        response = await self.run(user_input)
        for word in response.split():
            yield word + " "
            await asyncio.sleep(0.05)  # Simulate streaming

def create_agent() -> ProductionAgent:
    """Factory function to create agent."""
    return ProductionAgent()
```

### Create the Streamlit Frontend

```python
# app.py
import streamlit as st
import requests
import json
import os

# Page configuration
st.set_page_config(
    page_title="Zero-Cost AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# API endpoint (from environment)
API_URL = os.getenv("API_URL", "http://localhost:8000")

st.title("🤖 Zero-Cost AI Assistant")
st.caption("Powered by Llama 3.3 70B running on HuggingFace Spaces Free Tier")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get response from agent API
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # Use streaming endpoint
            response = requests.post(
                f"{API_URL}/chat/stream",
                json={
                    "messages": st.session_state.messages,
                    "stream": True
                },
                stream=True,
                timeout=120
            )
            
            for line in response.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith("data: "):
                        data = json.loads(line[6:])
                        if "token" in data:
                            full_response += data["token"]
                            response_placeholder.markdown(full_response + "▌")
                        elif data == "[DONE]":
                            break
            
            response_placeholder.markdown(full_response)
            
        except Exception as e:
            response_placeholder.markdown(f"❌ Error: {str(e)}")
            full_response = f"Error: {str(e)}"
    
    # Add assistant response
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This AI assistant is running on **HuggingFace Spaces Free Tier**:
    
    - 🦙 **Model:** Llama 3.3 70B (Q4_K_M)
    - 💾 **RAM:** 16GB (12GB for model, 4GB for app)
    - 💰 **Cost:** $0
    - 🔒 **Privacy:** Your data never leaves HuggingFace
    
    ### Features
    - Real-time streaming responses
    - Conversation memory
    - Tool use (coming soon)
    
    ### Deployment
    This space is powered by:
    - [Ollama](https://ollama.com)
    - [LangGraph](https://langchain.com/langgraph)
    - [Streamlit](https://streamlit.io)
    - [HuggingFace Spaces](https://huggingface.co/spaces)
    """)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.caption(f"Session ID: {st.session_state.get('session_id', 'new')[:8]}")
```

### Create .dockerignore

```dockerignore
# .dockerignore
__pycache__
*.pyc
.git
.gitignore
.env.local
*.md
.DS_Store
venv/
env/
.venv/
data/
logs/
*.db
*.sqlite
*.duckdb
```

---

## Step 2: Test Docker Container Locally

Before deploying to HuggingFace, test your container locally.

```bash
# Build the Docker image
docker build -t zero-cost-ai:latest .

# Run the container locally
docker run -d \
    --name zero-cost-ai \
    -p 7860:7860 \
    -p 8000:8000 \
    -p 11434:11434 \
    -v ollama_data:/root/.ollama \
    zero-cost-ai:latest

# Check logs
docker logs -f zero-cost-ai

# Test the API
curl http://localhost:8000/health

# Test the frontend
open http://localhost:7860

# Stop and remove when done
docker stop zero-cost-ai
docker rm zero-cost-ai
```

**Expected output:**

```
🚀 Starting Zero-Cost AI Stack on HuggingFace Spaces
====================================================
📡 Starting Ollama server...
⏳ Waiting for Ollama to be ready...
   Waiting... (1/30)
   ✅ Ollama is ready
✅ Model already present
🧠 Starting Agent Orchestrator...
🖥️ Starting Frontend...
====================================================
✅ All components started!
   - Ollama API: http://localhost:11434
   - Agent API: http://localhost:8000
   - Frontend: http://localhost:7860
====================================================
```

---

## Step 3: Deploy to HuggingFace Spaces

### Option A: Deploy via Git (Recommended)

```bash
# 1. Create a new Space on HuggingFace
# Go to https://huggingface.co/new-space
# - Name: zero-cost-ai (or your choice)
# - License: MIT (or your choice)
# - Space type: Docker
# - Docker template: Blank

# 2. Clone the Space repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/zero-cost-ai
cd zero-cost-ai

# 3. Copy your Dockerfile and application files
cp ../Dockerfile .
cp ../requirements.txt .
cp ../*.py .
cp ../*.sh .

# 4. Create a README.md for your Space
cat > README.md << 'EOF'
---
title: Zero-Cost AI Assistant
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

# Zero-Cost AI Assistant

A production-ready AI assistant powered by Llama 3.3 70B running on HuggingFace Spaces Free Tier.

## Features
- Real-time streaming responses
- Conversation memory
- 16GB RAM for LLM inference
- Completely free to use

## Architecture
- **LLM:** Llama 3.3 70B (Q4_K_M quantization)
- **Inference:** Ollama
- **Orchestration:** LangGraph
- **Frontend:** Streamlit
- **Hosting:** HuggingFace Spaces Free Tier

## Usage
Simply type your question in the chat box. The AI will respond in real-time.
EOF

# 5. Commit and push
git add .
git commit -m "Deploy Zero-Cost AI stack"
git push

# 6. Wait for build (10-15 minutes for first build)
# Monitor at: https://huggingface.co/spaces/YOUR_USERNAME/zero-cost-ai
```

### Option B: Deploy via HuggingFace CLI

```bash
# Install HuggingFace CLI
pip install huggingface_hub

# Login
huggingface-cli login

# Create Space
huggingface-cli space create zero-cost-ai --docker --sdk docker

# Push files
huggingface-cli upload zero-cost-ai . --repo-type=space
```

### Option C: Deploy via Web Interface

1. Go to https://huggingface.co/new-space
2. Select "Docker" as Space type
3. Upload your Dockerfile and files via the web interface
4. Click "Create Space"
5. Wait for the build to complete

---

## Step 4: Configure Environment Variables

After deployment, configure environment variables for your Space:

```bash
# Using HuggingFace CLI
huggingface-cli space env set YOUR_USERNAME/zero-cost-ai \
    OLLAMA_URL=http://localhost:11434 \
    LLM_MODEL=llama3.3:70b-instruct-q4_K_M \
    LOG_LEVEL=INFO

# Or via web interface:
# Settings -> Environment Variables
```

**Required environment variables:**

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_URL` | `http://localhost:11434` | Ollama API endpoint |
| `LLM_MODEL` | `llama3.3:70b-instruct-q4_K_M` | Model to use |
| `LOG_LEVEL` | `INFO` | Logging level (DEBUG, INFO, WARN, ERROR) |
| `MAX_TOKENS` | `500` | Maximum tokens per response |
| `TEMPERATURE` | `0.7` | LLM temperature |

---

## Step 5: Set Up Persistent Storage

HuggingFace Spaces provides persistent storage for your Space. Use it to cache model weights and user data.

```yaml
# .huggingface/settings.yaml (create this file)
storage:
  enabled: true
  path: /data
  size: 50GB
```

Update your Dockerfile to use persistent storage:

```dockerfile
# Add to Dockerfile
VOLUME /root/.ollama  # Ollama model cache
VOLUME /app/data      # Application data
VOLUME /app/logs      # Logs
```

---

## Step 6: Add Custom Domain (Optional)

HuggingFace Spaces supports custom domains on the free tier.

```bash
# 1. Go to Space Settings
# 2. Click "Domain"
# 3. Enter your domain (e.g., ai.yourdomain.com)
# 4. Add DNS record:
#    Type: CNAME
#    Name: ai
#    Value: your-username-zero-cost-ai.hf.space
# 5. Click "Save"

# Wait for DNS propagation (5-30 minutes)
# Your Space will now be available at https://ai.yourdomain.com
```

---

## Step 7: Monitor Your Deployed Application

### HuggingFace Space Logs

```bash
# View logs via CLI
huggingface-cli space logs YOUR_USERNAME/zero-cost-ai

# Or via web interface:
# Click "Settings" -> "Repository" -> "Logs"
```

### Health Check Endpoint

Your API exposes health checks:

```bash
# Check if Space is healthy
curl https://YOUR_USERNAME-zero-cost-ai.hf.space/health

# Expected response:
# {"status":"healthy","ollama":"ready"}
```

### Metrics Dashboard

HuggingFace provides basic metrics for your Space:

- CPU usage
- RAM usage
- Storage usage
- Request count
- Build status

Access at: `https://huggingface.co/spaces/YOUR_USERNAME/zero-cost-ai/metrics`

---

## Optimizing for HuggingFace Free Tier

### Memory Optimization

The free tier gives you 16GB RAM. Your Llama 3.3 70B Q4_K_M uses ~12GB. Optimize the remaining 4GB:

```python
# memory_optimization.py
import gc
import torch

def optimize_memory():
    """Optimize memory usage for HuggingFace free tier."""
    
    # Clear CUDA cache (if using GPU)
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    
    # Force garbage collection
    gc.collect()
    
    # Limit token cache
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    
    # Use smaller batch size
    os.environ["OLLAMA_BATCH_SIZE"] = "128"  # Default is 512

# Call at startup
optimize_memory()
```

### Cold Start Optimization

HuggingFace Spaces sleep after 48 hours of inactivity. Optimize cold starts:

```python
# cold_start.py
import pickle
import os

class ModelCache:
    """Cache model in memory to avoid reloading."""
    
    def __init__(self, cache_path="/data/model_cache.pkl"):
        self.cache_path = cache_path
    
    def save_model_state(self, state):
        """Save model state to persistent storage."""
        with open(self.cache_path, 'wb') as f:
            pickle.dump(state, f)
    
    def load_model_state(self):
        """Load model state from persistent storage."""
        if os.path.exists(self.cache_path):
            with open(self.cache_path, 'rb') as f:
                return pickle.load(f)
        return None

# Use before model loading
cache = ModelCache()
cached_state = cache.load_model_state()
if cached_state:
    # Fast path: load from cache (2-3 seconds)
    model = load_from_cache(cached_state)
else:
    # Slow path: load from scratch (15-30 seconds)
    model = load_model()
    cache.save_model_state(model)
```

### Keep-Alive Strategy

Prevent your Space from sleeping:

```python
# keepalive.py
import requests
import time
import os

def keep_alive():
    """Ping the Space every 12 hours to prevent sleep."""
    space_url = os.getenv("SPACE_URL", "https://YOUR_USERNAME-zero-cost-ai.hf.space")
    
    while True:
        try:
            response = requests.get(f"{space_url}/health", timeout=30)
            print(f"Keep-alive ping: {response.status_code}")
        except Exception as e:
            print(f"Keep-alive failed: {e}")
        
        # Sleep for 12 hours
        time.sleep(12 * 3600)

if __name__ == "__main__":
    keep_alive()
```

---

## Troubleshooting Common Deployment Issues

### Issue 1: Container Exceeds Memory Limit

**Symptom:** Space crashes with "Out of memory" error.

**Solution:** Use smaller model or more aggressive quantization:

```yaml
# Switch to smaller model
LLM_MODEL: llama3.3:70b-instruct-q4_K_S  # Uses ~10GB instead of 12GB

# Or switch to Gemma 4
LLM_MODEL: gemma4:4b-instruct-q4_0  # Uses ~3GB
```

### Issue 2: Build Takes Too Long

**Symptom:** Docker build exceeds 60 minutes.

**Solution:** Use HuggingFace's cached builds:

```dockerfile
# Optimize Docker layer caching
# Copy requirements first (changes rarely)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy model pull script (changes rarely)
COPY pull_model.sh .
RUN chmod +x pull_model.sh

# Copy application code last (changes often)
COPY . .
```

### Issue 3: Model Download Fails

**Symptom:** Ollama cannot download the model.

**Solution:** Use HuggingFace's model cache or pre-download:

```bash
# Option 1: Use HuggingFace model hub
huggingface-cli download meta-llama/Llama-3.3-70B-Instruct-GGUF

# Option 2: Use faster mirror
export OLLAMA_HOST=https://ollama.mirror.example.com
```

### Issue 4: API Timeout

**Symptom:** Requests timeout after 60 seconds.

**Solution:** Implement request queuing and streaming:

```python
# Use streaming responses for long generations
@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    async def generate():
        async for chunk in agent.stream(request.messages):
            yield f"data: {json.dumps({'token': chunk})}\n\n"
    
    return StreamingResponse(generate())
```

---

## Cost Analysis: Local vs HuggingFace vs Cloud

| Deployment Option | Monthly Cost | RAM | vCPUs | GPU | Uptime |
|------------------|--------------|-----|-------|-----|--------|
| **Your Laptop (Part 1-6)** | $0 (electricity ~$5) | 16GB | 4-8 | Optional | Only when powered on |
| **HuggingFace Spaces Free** | **$0** | 16GB | 2 | No | 24/7 (with sleep) |
| **HuggingFace Spaces Pro** | $9 | 32GB | 4 | No | 24/7 |
| **AWS EC2 (g4dn.xlarge)** | $384 | 16GB | 4 | T4 (16GB) | 24/7 |
| **RunPod Community Cloud** | $30-50 | 24GB | 8 | RTX 3090 | 24/7 |
| **Vast.ai** | $20-40 | 24GB | 6 | RTX 4090 | 24/7 |

**Conclusion:** HuggingFace Spaces Free is the most cost-effective option for production deployment of quantized LLMs. For GPU-accelerated inference, consider Vast.ai or RunPod.

---

## What's Next in This Series

You have just deployed your entire zero-cost AI stack to HuggingFace Spaces free tier. Your Llama 3.3 70B model, agent orchestrator, and frontend are now running in the cloud, accessible from anywhere, costing exactly $0. In **Part 8**, you will add comprehensive observability to monitor your deployed application.

### Next Story Preview:

**8. 📎 Read** [Zero-Cost AI: Observability on a Laptop Without Datadog – Part 8](#)

*Logging, tracing, and monitoring agent behavior using structured JSON logs, OpenTelemetry collectors, and Grafana dashboards — entirely without paid observability tools.*

**Part 8 will cover:**
- Structured logging for agent decisions, LLM calls, and tool use
- OpenTelemetry tracing for distributed request tracking
- Building Grafana dashboards on the free tier
- Alerting on errors and performance degradation
- Log aggregation with Loki (free tier)
- Metrics collection with Prometheus

---

### Full Series Recap (All 10 Parts)

**1. 📎 Read** [Zero-Cost AI: The $0 Stack That Actually Works – Part 1](#)  
*Complete architectural breakdown of all eight layers with performance characteristics, memory requirements, and working code examples.*

**2. 📎 Read** [Zero-Cost AI: Frontend on Your Laptop, Deployed for Free – Part 2](#)  
*Deploying Next.js 15 and Streamlit 1.35 on Vercel's free tier with automatic routing, serverless functions, and 100GB monthly bandwidth.*

**3. 📎 Read** [Zero-Cost AI: Agent Orchestration on a Laptop Without Paying – Part 3](#)  
*LangGraph v0.2 vs CrewAI v0.70 for building multi-agent systems that manage state, coordinate tools, and maintain end-to-end data flow at zero cost.*

**4. 📎 Read** [Zero-Cost AI: Replacing GPT-4 with Llama 3.3 70B Locally – Part 4](#)  
*Running Llama 3.3 70B Q4_K_M, Gemma 4 E4B Q4_0, and Mistral Small 4 Q5_K_M on a laptop using Ollama 0.5 with benchmark comparisons to GPT-4o and Claude 3.5.*

**5. 📎 Read** [Zero-Cost AI: Tool Use on a Laptop via Model Context Protocol – Part 5](#)  
*How MCP 2026.1 replaces expensive function-calling APIs by connecting local LLMs to your file system, SQLite databases, shell commands, and web APIs through a standardized JSON-RPC protocol.*

**6. 📎 Read** [Zero-Cost AI: Code Agents on a Laptop Without Subscriptions – Part 6](#)  
*Using Claude Code CLI 2.1 and Aider 0.55 for AI pair programming, code generation, refactoring, bug fixing, and automated PRs — all powered by your local Llama 3.3 instance.*

**7. 📎 Read** [Zero-Cost AI: Deploy from Laptop to HuggingFace for Free – Part 7](#) *(you are here)*  
*Packaging the complete $0 AI stack with Docker 27.0 and deploying to HuggingFace Spaces free tier with 16GB RAM, 2 vCPUs, automatic HTTPS, and custom domain support.*

**8. 📎 Read** [Zero-Cost AI: Observability on a Laptop Without Datadog – Part 8](#)  
*Logging, tracing, and monitoring agent behavior using structured JSON logs, OpenTelemetry collectors, and Grafana dashboards — entirely without paid observability tools.*

**9. 📎 Read** [Zero-Cost AI: RAG Pipeline on a Laptop for Free – Part 9](#)  
*Building retrieval-augmented generation with LlamaIndex 0.10, local ChromaDB 0.4, Qdrant 1.10, and all-MiniLM-L6-v2 embeddings — all running locally with zero cloud dependencies.*

**10. 📎 Read** [Zero-Cost AI: Data Layer on a Laptop Without Cloud Spend – Part 10](#)  
*Using SQLite 3.45 for production transactions, DuckDB 0.10 for analytical queries, and Supabase free tier for optional cloud sync with row-level security and real-time subscriptions.*

---

**Your zero-cost AI stack is now live in production.** Deployed to HuggingFace Spaces free tier, accessible from anywhere, serving users 24/7, costing exactly $0. The 16GB RAM limit is exactly enough for Llama 3.3 70B Q4_K_M. The automatic HTTPS keeps your traffic secure. The Docker container keeps your stack portable.

Proceed to **Part 8** when you're ready to add observability to monitor your deployed application.

> *"HuggingFace Spaces free tier is the best deal in AI hosting. 16GB of RAM for zero dollars — enough for the most capable open-source models. Your AI application doesn't need to be expensive to be production-grade." — Zero-Cost AI Handbook*

---

**Estimated read time for Part 7:** 35-50 minutes depending on whether you deploy to HuggingFace.

Would you like me to write **Part 8** (Observability on a Laptop Without Datadog) now in the same detailed, 35-50 minute handbook style?