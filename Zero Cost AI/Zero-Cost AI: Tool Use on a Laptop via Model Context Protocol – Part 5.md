Here is **Story #5** of your **Zero-Cost AI** handbook series, following the exact same structure as Parts 1-4 with numbered story listings, detailed technical depth, and a 35-50 minute read length.

---

# Zero-Cost AI: Tool Use on a Laptop via Model Context Protocol – Part 5

## A Complete Handbook for How MCP 2026.1 Replaces Expensive Function-Calling APIs by Connecting Local LLMs to Your File System, SQLite Databases, Shell Commands, and Web APIs Through a Standardized JSON-RPC Protocol

---

## Introduction

You have a powerful local LLM running on your laptop. You have a frontend that streams responses in real time. You have an agent orchestrator that manages multi-step reasoning. Your system can answer questions, generate code, and even collaborate across multiple specialized agents.

But there's a critical missing piece.

Your agents are **read-only**. They can think and reason, but they cannot act. They cannot read files from your hard drive. They cannot query your database. They cannot execute code. They cannot send emails. They cannot control your system.

In the cloud world, you would reach for OpenAI's function-calling API ($2.50 per million tokens plus per-call overhead) or Anthropic's tool use API ($3 per million tokens). These proprietary protocols lock you into specific providers, charge per invocation, and send your data to third-party servers.

But this is the Zero-Cost AI handbook, and we don't do paid.

Enter the **Model Context Protocol (MCP) 2026.1** — an open standard developed by Anthropic and contributed to the open-source community. MCP provides a universal protocol for LLMs to call tools, read resources, and interact with external systems. It works with any LLM, runs entirely locally, and costs exactly $0.

MCP is not just another tool framework. It is a complete rethinking of how LLMs should interact with the world. Instead of each application implementing its own brittle function-calling logic, MCP provides a standardized JSON-RPC protocol over stdio or Server-Sent Events (SSE). LLMs generate MCP-compliant requests. MCP servers execute those requests and return results. The LLM never needs to know the implementation details of the tool — only the MCP schema.

In **Part 5**, you will master the Model Context Protocol. You will install and configure MCP servers for filesystem access, SQLite databases, shell commands, and web APIs. You will connect your LangGraph agents from Part 3 to MCP tools. You will build custom MCP servers for your specific use cases. You will learn security best practices for local tool use. And you will benchmark MCP performance against OpenAI's function-calling API.

No proprietary protocols. No per-call fees. No data leaving your laptop. Just a standardized, open protocol that gives your agents the power to act.

---

## Takeaway from Part 4

Before diving into MCP, let's review the essential foundations established in **Part 4: Replacing GPT-4 with Llama 3.3 70B Locally**:

- **Local Llama 3.3 70B matches GPT-4 on benchmarks.** With 86.4% on MMLU, 92.5% on GSM8K, and 68.9% on HumanEval, the gap between open-source and proprietary models has effectively closed. For 95% of real-world tasks, you will not notice the difference.

- **Quantization makes local models practical.** The Q4_K_M quantization method reduces memory from 140GB to 12GB while retaining 95% of the model's reasoning ability. This is the breakthrough that makes local LLMs viable on consumer hardware.

- **Context window management is critical.** The KV cache grows with each token. Limiting context to 4K-8K tokens keeps memory usage within 16GB while still supporting most real-world conversations.

- **Prompt engineering differs for local models.** Local models respond better to explicit system prompts, few-shot examples, chain-of-thought reasoning, and structured output formats. The techniques you learned in Part 4 are essential for reliable agent behavior.

- **Benchmarking validates performance.** Your benchmark framework from Part 4 allows you to test any model on your specific hardware. Run it before deploying to production to understand real-world performance characteristics.

With these takeaways firmly in place, you are ready to give your agents the power to act through the Model Context Protocol.

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

**5. 📎 Read** [Zero-Cost AI: Tool Use on a Laptop via Model Context Protocol – Part 5](#) *(you are here)*  
*How MCP 2026.1 replaces expensive function-calling APIs by connecting local LLMs to your file system, SQLite databases, shell commands, and web APIs through a standardized JSON-RPC protocol. First published in the Zero-Cost AI Handbook.*

**6. 📎 Read** [Zero-Cost AI: Code Agents on a Laptop Without Subscriptions – Part 6](#)  
*Using Claude Code CLI 2.1 and Aider 0.55 for AI pair programming, code generation, refactoring, bug fixing, and automated PRs — all powered by your local Llama 3.3 instance. First published in the Zero-Cost AI Handbook.*

**7. 📎 Read** [Zero-Cost AI: Deploy from Laptop to HuggingFace for Free – Part 7](#)  
*Packaging the complete $0 AI stack with Docker 27.0 and deploying to HuggingFace Spaces free tier with 16GB RAM, 2 vCPUs, automatic HTTPS, and custom domain support. First published in the Zero-Cost AI Handbook.*

**8. 📎 Read** [Zero-Cost AI: Observability on a Laptop Without Datadog – Part 8](#)  
*Logging, tracing, and monitoring agent behavior using structured JSON logs, OpenTelemetry collectors, and Grafana dashboards — entirely without paid observability tools. First published in the Zero-Cost AI Handbook.*

**9. 📎 Read** [Zero-Cost AI: RAG Pipeline on a Laptop for Free – Part 9](#)  
*Building retrieval-augmented generation with LlamaIndex 0.10, local ChromaDB 0.4, Qdrant 1.10, and all-MiniLM-L6-v2 embeddings — all running locally with zero cloud dependencies. First published in the Zero-Cost AI Handbook.*

**10. 📎 Read** [Zero-Cost AI: Data Layer on a Laptop Without Cloud Spend – Part 10](#)  
*Using SQLite 3.45 for production transactions, DuckDB 0.10 for analytical queries, and Supabase free tier for optional cloud sync with row-level security and real-time subscriptions. First published in the Zero-Cost AI Handbook.*

---

## MCP Architecture and Protocol Design

Before implementing MCP, you need a mental model of how the protocol works and how it fits into your zero-cost AI stack. The diagram below shows the complete MCP architecture, from LLM tool request to tool execution and back.

```mermaid
flowchart TB
    LLM[🤖 Local LLM\nLlama 3.3 70B\nGenerates tool request] -->|Natural language| Agent[🧠 Agent Orchestrator\nLangGraph/CrewAI\nPart 3]
    
    Agent -->|Convert to MCP| MCP_Client[📡 MCP Client\nJSON-RPC over stdio/SSE\nEmbedded in agent]
    
    MCP_Client -->|{"jsonrpc":"2.0","method":"tools/call","params":{...}}| MCP_Server[🖥️ MCP Server\nIndependent process\nstdio communication]
    
    MCP_Server -->|Route to tool| Tool1[📁 Filesystem Tool\nRead/write files\nList directories]
    MCP_Server -->|Route to tool| Tool2[🗄️ SQLite Tool\nQuery database\nExecute transactions]
    MCP_Server -->|Route to tool| Tool3[🐚 Shell Tool\nRun commands\nExecute scripts]
    MCP_Server -->|Route to tool| Tool4[🌐 Web Tool\nHTTP requests\nAPI calls]
    
    Tool1 -->|Result| MCP_Server
    Tool2 -->|Result| MCP_Server
    Tool3 -->|Result| MCP_Server
    Tool4 -->|Result| MCP_Server
    
    MCP_Server -->|{"result":{...}}| MCP_Client
    MCP_Client -->|Inject result| Agent
    Agent -->|Continue reasoning| LLM
    
    style LLM fill:#2ecc71,stroke:#27ae60,stroke-width:2px,color:#000
    style Agent fill:#e67e22,stroke:#d35400,stroke-width:2px,color:#fff
    style MCP_Client fill:#3498db,stroke:#2980b9,stroke-width:2px,color:#fff
    style MCP_Server fill:#9b59b6,stroke:#8e44ad,stroke-width:2px,color:#fff
```

### What is the Model Context Protocol?

MCP is an open protocol standardizing how LLMs interact with external tools, data sources, and systems. It was developed by Anthropic and released to the open-source community in 2025. The protocol has three core components:

**1. MCP Client** — Embedded in your agent orchestrator. The client translates the LLM's natural language tool requests into structured JSON-RPC messages and sends them to MCP servers.

**2. MCP Server** — An independent process that exposes tools, resources, and prompts. Servers run locally (for security) and communicate with clients via stdio (standard input/output) or SSE (Server-Sent Events).

**3. MCP Protocol** — A JSON-RPC 2.0 compliant protocol with standard methods for listing tools, calling tools, reading resources, and getting prompts.

### Why MCP Instead of Proprietary Function Calling?

| Feature | OpenAI Function Calling | Anthropic Tool Use | MCP |
|---------|------------------------|-------------------|-----|
| **Cost** | $2.50-$10 per million tokens + per-call overhead | $3-$15 per million tokens + per-call overhead | **$0** |
| **Data privacy** | Data sent to OpenAI | Data sent to Anthropic | **Local only** |
| **Tool ecosystem** | Must implement each tool | Must implement each tool | **Growing open ecosystem** |
| **Protocol standardization** | Proprietary | Proprietary | **Open standard** |
| **LLM compatibility** | OpenAI only | Anthropic only | **Any LLM** |
| **Transport** | HTTP (cloud) | HTTP (cloud) | **stdio/SSE (local)** |
| **Security** | Relies on API keys | Relies on API keys | **Filesystem permissions** |

### MCP JSON-RPC Message Format

**List available tools:**
```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {}
}
```

**Call a tool:**
```json
{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
        "name": "read_file",
        "arguments": {
            "path": "/tmp/data.txt"
        }
    }
}
```

**Tool response:**
```json
{
    "jsonrpc": "2.0",
    "id": 2,
    "result": {
        "content": [
            {
                "type": "text",
                "text": "File contents: Hello, world!"
            }
        ],
        "isError": false
    }
}
```

---

## Installing and Configuring MCP Servers

### Step 1: Install Node.js (Required for MCP Servers)

Most MCP servers are distributed as npm packages. Install Node.js if you haven't already:

```bash
# macOS
brew install node

# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify installation
node --version  # Should be v20.x or higher
npm --version
```

### Step 2: Install Essential MCP Servers

```bash
# Filesystem server - read/write files, list directories
npm install -g @modelcontextprotocol/server-filesystem

# SQLite server - query databases
npm install -g @modelcontextprotocol/server-sqlite

# Brave Search server - web search (requires free API key)
npm install -g @modelcontextprotocol/server-brave-search

# Fetch server - make HTTP requests
npm install -g @modelcontextprotocol/server-fetch

# Memory server - persistent knowledge graph
npm install -g @modelcontextprotocol/server-memory

# Git server - git operations
npm install -g @modelcontextprotocol/server-git

# Puppeteer server - browser automation
npm install -g @modelcontextprotocol/server-puppeteer
```

### Step 3: Configure MCP Servers

Create a configuration file for your MCP servers:

```json
// mcp_config.json
{
    "mcpServers": {
        "filesystem": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-filesystem",
                "/tmp",
                "/home/user/documents",
                "/home/user/projects"
            ],
            "env": {}
        },
        "sqlite": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-sqlite",
                "--db-path",
                "/home/user/data/agents.db"
            ],
            "env": {}
        },
        "brave-search": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-brave-search"
            ],
            "env": {
                "BRAVE_API_KEY": "your-api-key-here"
            }
        },
        "fetch": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-fetch"
            ],
            "env": {}
        },
        "memory": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-memory"
            ],
            "env": {}
        }
    }
}
```

### Step 4: Test MCP Servers Individually

Before integrating with your agent, test each MCP server directly:

```bash
# Test filesystem server
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' | \
    npx -y @modelcontextprotocol/server-filesystem /tmp

# Expected output: JSON list of available tools (read_file, write_file, list_directory, etc.)

# Test sqlite server
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' | \
    npx -y @modelcontextprotocol/server-sqlite --db-path test.db
```

---

## Building a Python MCP Client for LangGraph

Now integrate MCP into your LangGraph agent from Part 3.

### Step 1: Install MCP Python SDK

```bash
pip install mcp httpx sse-py
```

### Step 2: Create MCP Client Class

```python
# mcp_client.py
import json
import subprocess
import asyncio
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

@dataclass
class MCPTool:
    """Represents a tool exposed by an MCP server."""
    name: str
    description: str
    input_schema: Dict[str, Any]

class MCPClient:
    """Client for communicating with MCP servers via stdio."""
    
    def __init__(self, server_command: str, server_args: List[str], env: Dict[str, str] = None):
        self.server_command = server_command
        self.server_args = server_args
        self.env = env or {}
        self.process = None
        self.tools = []
        self.request_id = 0
    
    async def start(self):
        """Start the MCP server process."""
        self.process = await asyncio.create_subprocess_exec(
            self.server_command,
            *self.server_args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env={**os.environ, **self.env}
        )
        
        # Initialize the connection
        await self._send_request("initialize", {
            "protocolVersion": "2025-06-18",
            "capabilities": {}
        })
        
        # List available tools
        await self.list_tools()
    
    async def _send_request(self, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Send a JSON-RPC request to the MCP server."""
        self.request_id += 1
        request = {
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": method,
            "params": params
        }
        
        # Send request
        self.process.stdin.write((json.dumps(request) + "\n").encode())
        await self.process.stdin.drain()
        
        # Read response
        response_line = await self.process.stdout.readline()
        response = json.loads(response_line.decode())
        
        if "error" in response:
            raise Exception(f"MCP error: {response['error']}")
        
        return response.get("result", {})
    
    async def list_tools(self) -> List[MCPTool]:
        """List all available tools from the MCP server."""
        result = await self._send_request("tools/list", {})
        self.tools = [
            MCPTool(
                name=tool["name"],
                description=tool["description"],
                input_schema=tool.get("inputSchema", {})
            )
            for tool in result.get("tools", [])
        ]
        return self.tools
    
    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        """Call a tool on the MCP server."""
        result = await self._send_request("tools/call", {
            "name": tool_name,
            "arguments": arguments
        })
        
        # Extract text content from response
        content_parts = []
        for content in result.get("content", []):
            if content.get("type") == "text":
                content_parts.append(content.get("text", ""))
        
        return "\n".join(content_parts)
    
    async def stop(self):
        """Stop the MCP server process."""
        if self.process:
            self.process.terminate()
            await self.process.wait()
    
    def get_tools_description(self) -> str:
        """Get a human-readable description of all tools for LLM prompts."""
        descriptions = []
        for tool in self.tools:
            descriptions.append(f"- {tool.name}: {tool.description}")
        return "\n".join(descriptions)


class MCPManager:
    """Manage multiple MCP servers from configuration."""
    
    def __init__(self, config_path: str):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        self.clients = {}
    
    async def start_all(self):
        """Start all configured MCP servers."""
        for server_name, server_config in self.config.get("mcpServers", {}).items():
            print(f"Starting MCP server: {server_name}")
            client = MCPClient(
                server_command=server_config["command"],
                server_args=server_config["args"],
                env=server_config.get("env", {})
            )
            await client.start()
            self.clients[server_name] = client
            print(f"  ✅ Loaded {len(client.tools)} tools")
    
    async def call_tool(self, server_name: str, tool_name: str, arguments: Dict[str, Any]) -> str:
        """Call a tool on a specific server."""
        if server_name not in self.clients:
            raise ValueError(f"Server {server_name} not started")
        return await self.clients[server_name].call_tool(tool_name, arguments)
    
    def get_all_tools_description(self) -> str:
        """Get description of all tools across all servers."""
        descriptions = []
        for server_name, client in self.clients.items():
            descriptions.append(f"\n[{server_name}]")
            descriptions.append(client.get_tools_description())
        return "\n".join(descriptions)
    
    async def stop_all(self):
        """Stop all MCP servers."""
        for client in self.clients.values():
            await client.stop()
```

### Step 3: Integrate MCP with LangGraph Agent

Update your LangGraph agent from Part 3 to use MCP tools:

```python
# agent_with_mcp.py
import asyncio
from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, END

from mcp_client import MCPManager
from config import get_llm

class AgentState(TypedDict):
    input: str
    messages: List[Dict[str, str]]
    final_answer: str
    iteration: int
    mcp_calls: List[Dict[str, Any]]
    mcp_results: List[str]

class MCPAgent:
    """LangGraph agent with MCP tool access."""
    
    def __init__(self, mcp_config_path: str):
        self.mcp_manager = MCPManager(mcp_config_path)
        self.llm = get_llm()
        self.graph = self._build_graph()
    
    def _build_graph(self) -> StateGraph:
        """Build the LangGraph with MCP integration."""
        
        async def reasoning_node(state: AgentState) -> AgentState:
            """LLM decides which MCP tools to call."""
            
            # Get available tools description
            tools_desc = self.mcp_manager.get_all_tools_description()
            
            prompt = f"""You are an AI assistant with access to the following tools:

{tools_desc}

User request: {state['input']}

Decide which tools to call (if any). Respond with a JSON object:
- If you need to call tools: {{"action": "call_tools", "calls": [{{"server": "server_name", "tool": "tool_name", "arguments": {{}}}}]}}
- If you have the answer: {{"action": "answer", "answer": "your response"}}

Previous context: {state['messages'][-3:] if state['messages'] else 'None'}
"""
            
            response = self.llm.invoke(prompt)
            
            try:
                import json
                decision = json.loads(response.content)
                
                if decision.get("action") == "call_tools":
                    state["mcp_calls"] = decision.get("calls", [])
                    state["messages"].append({
                        "role": "assistant",
                        "content": f"Calling {len(state['mcp_calls'])} tool(s)..."
                    })
                else:
                    state["final_answer"] = decision.get("answer", response.content)
                    state["messages"].append({
                        "role": "assistant",
                        "content": state["final_answer"]
                    })
            except:
                # If not JSON, treat as final answer
                state["final_answer"] = response.content
                state["messages"].append({
                    "role": "assistant",
                    "content": response.content
                })
            
            state["iteration"] += 1
            return state
        
        async def tool_execution_node(state: AgentState) -> AgentState:
            """Execute MCP tool calls."""
            
            results = []
            for call in state.get("mcp_calls", []):
                server = call.get("server")
                tool = call.get("tool")
                arguments = call.get("arguments", {})
                
                print(f"🔧 Calling {server}.{tool} with {arguments}")
                
                try:
                    result = await self.mcp_manager.call_tool(server, tool, arguments)
                    results.append(f"✅ {tool}: {result[:500]}")
                    state["messages"].append({
                        "role": "tool",
                        "content": f"Result from {tool}: {result[:500]}"
                    })
                except Exception as e:
                    error_msg = f"❌ {tool} failed: {str(e)}"
                    results.append(error_msg)
                    state["messages"].append({
                        "role": "tool",
                        "content": error_msg
                    })
            
            state["mcp_results"] = results
            state["mcp_calls"] = []  # Clear pending calls
            return state
        
        def should_continue(state: AgentState) -> str:
            """Determine next step."""
            if state.get("mcp_calls"):
                return "tools"
            elif state.get("final_answer"):
                return "end"
            else:
                return "reason"
        
        # Build graph
        workflow = StateGraph(AgentState)
        workflow.add_node("reason", reasoning_node)
        workflow.add_node("tools", tool_execution_node)
        
        workflow.set_entry_point("reason")
        workflow.add_conditional_edges("reason", should_continue, {
            "tools": "tools",
            "end": END
        })
        workflow.add_edge("tools", "reason")
        
        return workflow.compile()
    
    async def run(self, user_input: str) -> str:
        """Run the agent on user input."""
        
        # Start MCP servers
        await self.mcp_manager.start_all()
        
        # Initialize state
        state = {
            "input": user_input,
            "messages": [{"role": "user", "content": user_input}],
            "final_answer": None,
            "iteration": 0,
            "mcp_calls": [],
            "mcp_results": []
        }
        
        # Run the graph
        final_state = await self.graph.ainvoke(state)
        
        # Stop MCP servers
        await self.mcp_manager.stop_all()
        
        return final_state.get("final_answer", "No answer generated")

# Run the agent
async def main():
    agent = MCPAgent("mcp_config.json")
    result = await agent.run("Read the file /tmp/notes.txt and summarize it")
    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Building Custom MCP Servers

While pre-built MCP servers cover many use cases, you'll eventually need custom tools for your specific application. Here's how to build them.

### Step 1: Create a Custom MCP Server (Python)

```python
# custom_mcp_server.py
#!/usr/bin/env python3
"""
A custom MCP server that exposes company-specific tools.
Run with: python custom_mcp_server.py
"""

import json
import sys
import sqlite3
from typing import Dict, Any

class CustomMCPServer:
    """Custom MCP server for company-specific operations."""
    
    def __init__(self):
        self.tools = self._register_tools()
    
    def _register_tools(self) -> Dict[str, callable]:
        """Register all available tools."""
        return {
            "get_customer_by_id": self.get_customer_by_id,
            "get_recent_orders": self.get_recent_orders,
            "calculate_shipping_cost": self.calculate_shipping_cost,
            "send_email": self.send_email,
        }
    
    def get_customer_by_id(self, customer_id: int) -> Dict[str, Any]:
        """Get customer details from database."""
        # Connect to your company database
        conn = sqlite3.connect("company.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name, email, tier FROM customers WHERE id = ?", (customer_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "tier": row[3]
            }
        return {"error": f"Customer {customer_id} not found"}
    
    def get_recent_orders(self, customer_id: int, limit: int = 5) -> list:
        """Get recent orders for a customer."""
        conn = sqlite3.connect("company.db")
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT order_id, total, status, created_at 
            FROM orders 
            WHERE customer_id = ? 
            ORDER BY created_at DESC 
            LIMIT ?
        """, (customer_id, limit))
        
        orders = [{"id": row[0], "total": row[1], "status": row[2], "date": row[3]} 
                  for row in cursor.fetchall()]
        conn.close()
        
        return orders
    
    def calculate_shipping_cost(self, weight_kg: float, distance_km: float, tier: str) -> float:
        """Calculate shipping cost based on weight, distance, and customer tier."""
        base_rate = 5.0  # $5 per kg per 100km
        cost = weight_kg * (distance_km / 100) * base_rate
        
        # Apply tier discount
        discounts = {"bronze": 0, "silver": 0.1, "gold": 0.2, "platinum": 0.3}
        discount = discounts.get(tier.lower(), 0)
        
        return round(cost * (1 - discount), 2)
    
    def send_email(self, to: str, subject: str, body: str) -> Dict[str, Any]:
        """Send an email (simulated for demo)."""
        # In production, integrate with SMTP or email API
        print(f"\n📧 SENDING EMAIL")
        print(f"   To: {to}")
        print(f"   Subject: {subject}")
        print(f"   Body: {body[:200]}...")
        
        return {"status": "sent", "to": to, "subject": subject}
    
    def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming JSON-RPC request."""
        method = request.get("method")
        params = request.get("params", {})
        
        if method == "tools/list":
            # Return list of available tools with schemas
            tools = []
            for name, func in self.tools.items():
                tools.append({
                    "name": name,
                    "description": func.__doc__ or f"Tool: {name}",
                    "inputSchema": self._get_schema_for_tool(name)
                })
            return {"tools": tools}
        
        elif method == "tools/call":
            tool_name = params.get("name")
            arguments = params.get("arguments", {})
            
            if tool_name in self.tools:
                try:
                    result = self.tools[tool_name](**arguments)
                    return {
                        "content": [
                            {"type": "text", "text": json.dumps(result, indent=2)}
                        ]
                    }
                except Exception as e:
                    return {
                        "content": [{"type": "text", "text": f"Error: {str(e)}"}],
                        "isError": True
                    }
            else:
                return {
                    "content": [{"type": "text", "text": f"Unknown tool: {tool_name}"}],
                    "isError": True
                }
        
        return {"error": f"Unknown method: {method}"}
    
    def _get_schema_for_tool(self, tool_name: str) -> Dict[str, Any]:
        """Generate JSON schema for a tool based on its signature."""
        schemas = {
            "get_customer_by_id": {
                "type": "object",
                "properties": {
                    "customer_id": {"type": "integer", "description": "Customer ID"}
                },
                "required": ["customer_id"]
            },
            "get_recent_orders": {
                "type": "object",
                "properties": {
                    "customer_id": {"type": "integer"},
                    "limit": {"type": "integer", "default": 5}
                },
                "required": ["customer_id"]
            },
            "calculate_shipping_cost": {
                "type": "object",
                "properties": {
                    "weight_kg": {"type": "number"},
                    "distance_km": {"type": "number"},
                    "tier": {"type": "string", "enum": ["bronze", "silver", "gold", "platinum"]}
                },
                "required": ["weight_kg", "distance_km", "tier"]
            },
            "send_email": {
                "type": "object",
                "properties": {
                    "to": {"type": "string"},
                    "subject": {"type": "string"},
                    "body": {"type": "string"}
                },
                "required": ["to", "subject", "body"]
            }
        }
        return schemas.get(tool_name, {"type": "object", "properties": {}})
    
    def run(self):
        """Run the MCP server, reading requests from stdin and writing to stdout."""
        print("Custom MCP server starting...", file=sys.stderr)
        
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            
            try:
                request = json.loads(line)
                response = self.handle_request(request)
                response["jsonrpc"] = "2.0"
                response["id"] = request.get("id")
                
                print(json.dumps(response))
                sys.stdout.flush()
                
            except json.JSONDecodeError as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {"code": -32700, "message": f"Parse error: {str(e)}"}
                }
                print(json.dumps(error_response))
                sys.stdout.flush()

if __name__ == "__main__":
    server = CustomMCPServer()
    server.run()
```

### Step 2: Add Custom Server to MCP Configuration

```json
// mcp_config.json (updated)
{
    "mcpServers": {
        "filesystem": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp", "/home/user/documents"]
        },
        "custom": {
            "command": "python",
            "args": ["custom_mcp_server.py"],
            "env": {}
        }
    }
}
```

---

## Security Best Practices for Local Tool Use

MCP servers run locally with full system access. Here are essential security practices:

### 1. Limit Filesystem Access

```json
// Only expose specific directories
{
    "filesystem": {
        "command": "npx",
        "args": [
            "@modelcontextprotocol/server-filesystem",
            "/tmp/ai-workspace",           // Temporary directory only
            "/home/user/documents/shared"   // Specific shared folder
        ]
    }
}
```

### 2. Implement Tool Permissions

```python
# permission_manager.py
class PermissionManager:
    """Manage which tools agents can access."""
    
    def __init__(self):
        self.permissions = {
            "read_file": {"allowed": True, "requires_approval": False},
            "write_file": {"allowed": True, "requires_approval": True},
            "delete_file": {"allowed": False, "requires_approval": False},
            "execute_command": {"allowed": True, "requires_approval": True},
            "send_email": {"allowed": True, "requires_approval": True},
            "web_search": {"allowed": True, "requires_approval": False},
        }
    
    def can_execute(self, tool_name: str) -> bool:
        """Check if a tool can be executed."""
        return self.permissions.get(tool_name, {}).get("allowed", False)
    
    def requires_approval(self, tool_name: str) -> bool:
        """Check if a tool requires human approval."""
        return self.permissions.get(tool_name, {}).get("requires_approval", False)

# Integrate with MCP client
permission_manager = PermissionManager()

async def call_tool_with_permissions(self, tool_name: str, arguments: Dict[str, Any]):
    if not permission_manager.can_execute(tool_name):
        return f"Tool {tool_name} is not permitted for security reasons."
    
    if permission_manager.requires_approval(tool_name):
        # Implement human-in-the-loop from Part 3
        approved = await request_human_approval(tool_name, arguments)
        if not approved:
            return f"Tool {tool_name} execution rejected by user."
    
    return await self.call_tool(tool_name, arguments)
```

### 3. Sanitize Tool Inputs

```python
# input_sanitizer.py
import re

class InputSanitizer:
    """Sanitize tool inputs to prevent injection attacks."""
    
    @staticmethod
    def sanitize_path(file_path: str) -> str:
        """Prevent path traversal attacks."""
        # Remove any '..' sequences
        safe_path = re.sub(r'\.\./', '', file_path)
        safe_path = re.sub(r'\.\.\\', '', safe_path)
        
        # Ensure path is within allowed directory
        allowed_prefixes = ["/tmp/ai-workspace/", "/home/user/documents/shared/"]
        if not any(safe_path.startswith(prefix) for prefix in allowed_prefixes):
            raise ValueError(f"Path {safe_path} is not in allowed directories")
        
        return safe_path
    
    @staticmethod
    def sanitize_command(command: str) -> str:
        """Prevent command injection."""
        # Block dangerous commands
        dangerous_patterns = ['rm -rf', 'sudo', 'chmod', 'chown', 'mkfs', 'dd']
        for pattern in dangerous_patterns:
            if pattern in command.lower():
                raise ValueError(f"Command contains dangerous pattern: {pattern}")
        
        return command
    
    @staticmethod
    def sanitize_sql_query(query: str) -> str:
        """Basic SQL injection prevention."""
        # Block DROP, DELETE, UPDATE, INSERT without WHERE
        dangerous_keywords = ['DROP TABLE', 'DELETE FROM', 'TRUNCATE']
        for keyword in dangerous_keywords:
            if keyword.upper() in query.upper():
                if 'WHERE' not in query.upper():
                    raise ValueError(f"Dangerous SQL without WHERE clause: {keyword}")
        
        return query
```

### 4. Sandbox Code Execution

```python
# sandbox.py
import subprocess
import tempfile
import resource
import signal

class Sandbox:
    """Execute code in a restricted sandbox environment."""
    
    def __init__(self, timeout_seconds: int = 10, memory_limit_mb: int = 256):
        self.timeout = timeout_seconds
        self.memory_limit = memory_limit_mb * 1024 * 1024
    
    def execute_python(self, code: str) -> str:
        """Execute Python code in a sandboxed process."""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_path = f.name
        
        try:
            # Set resource limits
            resource.setrlimit(resource.RLIMIT_AS, (self.memory_limit, self.memory_limit))
            resource.setrlimit(resource.RLIMIT_CPU, (self.timeout, self.timeout))
            
            # Execute with timeout
            result = subprocess.run(
                ['python', temp_path],
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            
            return result.stdout if result.returncode == 0 else result.stderr
        
        except subprocess.TimeoutExpired:
            return f"Execution timed out after {self.timeout} seconds"
        except Exception as e:
            return f"Sandbox error: {str(e)}"
        finally:
            # Clean up temp file
            import os
            os.unlink(temp_path)

# Use in MCP tool
sandbox = Sandbox()

def execute_python_code(code: str) -> str:
    """Execute Python code safely in sandbox."""
    return sandbox.execute_python(code)
```

---

## Benchmarking MCP vs OpenAI Function Calling

### Performance Comparison

```python
# mcp_benchmark.py
import asyncio
import time
import json
from mcp_client import MCPClient

async def benchmark_mcp(num_calls: int = 100):
    """Benchmark MCP tool call latency."""
    
    client = MCPClient("npx", ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"])
    await client.start()
    
    latencies = []
    
    for i in range(num_calls):
        start = time.perf_counter()
        result = await client.call_tool("read_file", {"path": "/tmp/test.txt"})
        latency = (time.perf_counter() - start) * 1000  # milliseconds
        
        latencies.append(latency)
    
    await client.stop()
    
    print(f"MCP Benchmark ({num_calls} calls):")
    print(f"  Average: {sum(latencies) / len(latencies):.2f}ms")
    print(f"  Median: {sorted(latencies)[len(latencies)//2]:.2f}ms")
    print(f"  P95: {sorted(latencies)[int(len(latencies)*0.95)]:.2f}ms")
    print(f"  P99: {sorted(latencies)[int(len(latencies)*0.99)]:.2f}ms")
    
    return latencies

def benchmark_openai_function_calling():
    """Compare with OpenAI function calling (requires API key)."""
    # This is illustrative - actual OpenAI latency is typically 200-500ms
    # plus network overhead
    print("\nOpenAI Function Calling (typical):")
    print("  Average: 250-500ms (includes network latency)")
    print("  Cost: Included in token pricing (~$0.0001 per call)")

if __name__ == "__main__":
    asyncio.run(benchmark_mcp())
```

**Expected results (local MCP):**
- Average latency: 5-15ms (tool execution only, no network)
- P95 latency: 20-30ms
- Cost: $0

**OpenAI function calling (for comparison):**
- Average latency: 200-500ms (includes network round trip)
- Cost: Included in token pricing (~$0.0001-0.001 per call)
- Data: Sent to OpenAI servers

---

## What's Next in This Series

You have just mastered the Model Context Protocol. Your agents can now read files, query databases, execute commands, search the web, and call custom APIs — all through a standardized, open protocol that costs exactly $0 and keeps all data local. In **Part 6**, you will add dedicated code agents that can write, review, and refactor code.

### Next Story Preview:

**6. 📎 Read** [Zero-Cost AI: Code Agents on a Laptop Without Subscriptions – Part 6](#)

*Using Claude Code CLI 2.1 and Aider 0.55 for AI pair programming, code generation, refactoring, bug fixing, and automated PRs — all powered by your local Llama 3.3 instance.*

**Part 6 will cover:**
- Installing and configuring Claude Code CLI with local Ollama
- Using Aider for automated code refactoring
- Building a code review agent that checks PRs for bugs and style issues
- Automated documentation generation
- Integrating code agents with git workflows
- Performance benchmarks for local vs cloud code generation

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

**5. 📎 Read** [Zero-Cost AI: Tool Use on a Laptop via Model Context Protocol – Part 5](#) *(you are here)*  
*How MCP 2026.1 replaces expensive function-calling APIs by connecting local LLMs to your file system, SQLite databases, shell commands, and web APIs through a standardized JSON-RPC protocol.*

**6. 📎 Read** [Zero-Cost AI: Code Agents on a Laptop Without Subscriptions – Part 6](#)  
*Using Claude Code CLI 2.1 and Aider 0.55 for AI pair programming, code generation, refactoring, bug fixing, and automated PRs — all powered by your local Llama 3.3 instance.*

**7. 📎 Read** [Zero-Cost AI: Deploy from Laptop to HuggingFace for Free – Part 7](#)  
*Packaging the complete $0 AI stack with Docker 27.0 and deploying to HuggingFace Spaces free tier with 16GB RAM, 2 vCPUs, automatic HTTPS, and custom domain support.*

**8. 📎 Read** [Zero-Cost AI: Observability on a Laptop Without Datadog – Part 8](#)  
*Logging, tracing, and monitoring agent behavior using structured JSON logs, OpenTelemetry collectors, and Grafana dashboards — entirely without paid observability tools.*

**9. 📎 Read** [Zero-Cost AI: RAG Pipeline on a Laptop for Free – Part 9](#)  
*Building retrieval-augmented generation with LlamaIndex 0.10, local ChromaDB 0.4, Qdrant 1.10, and all-MiniLM-L6-v2 embeddings — all running locally with zero cloud dependencies.*

**10. 📎 Read** [Zero-Cost AI: Data Layer on a Laptop Without Cloud Spend – Part 10](#)  
*Using SQLite 3.45 for production transactions, DuckDB 0.10 for analytical queries, and Supabase free tier for optional cloud sync with row-level security and real-time subscriptions.*

---

**Your agents can now act.** Through MCP, they can read files, query databases, execute commands, and call web APIs — all locally, all for free, all through an open standard. The protocol is mature, the ecosystem is growing, and the cost is exactly $0.

Proceed to **Part 6** when you're ready to add dedicated code agents that can write, review, and refactor code.

> *"The Model Context Protocol is the missing link between LLMs and the real world. It's open, it's free, and it works with any model. This is how AI should work." — Zero-Cost AI Handbook*

---

**Estimated read time for Part 5:** 35-50 minutes depending on whether you implement the custom MCP server.

Would you like me to write **Part 6** (Code Agents on a Laptop Without Subscriptions) now in the same detailed, 35-50 minute handbook style?