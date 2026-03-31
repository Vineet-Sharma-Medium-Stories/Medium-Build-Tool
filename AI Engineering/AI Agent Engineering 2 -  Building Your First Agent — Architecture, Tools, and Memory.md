# AI Agent Engineering 2 -  Building Your First Agent — Architecture, Tools, and Memory


## From Simple Chatbot to Autonomous Assistant

Welcome back to our AI Agent Engineering series! In [Part 1](link-to-part-1), we built the foundation — mastering Python for agents, understanding LLM internals, and learning to communicate effectively with models through advanced prompting. You built your first simple agent that could detect intents and respond to basic queries.

Today, we're going to transform that basic understanding into a truly autonomous agent. By the end of this story, you'll have built a complete WhatsApp travel agent that can remember users, use multiple tools, and handle complex multi-step tasks like booking flights and hotels.

---

## 🔄 What We Covered in Part 1

Before we dive into new territory, let's quickly recap what you learned in the first story:

### Programming Foundation
- **Asyncio**: Handling thousands of concurrent users with asynchronous programming
- **FastAPI**: Building robust API endpoints for agent communication
- **Pydantic**: Validating and structuring data with type hints
- **Poetry**: Managing dependencies for reproducible environments

### LLM Fundamentals
- **Transformers**: Understanding self-attention and how models process context
- **Tokens & Context Windows**: Counting tokens, managing costs, and staying within limits
- **Function Calling**: How LLMs can request tool execution
- **Major APIs**: Working with OpenAI, Anthropic, and Google Gemini

### Prompting Strategies
- **Zero-shot vs Few-shot**: Teaching by example
- **Chain-of-Thought**: Step-by-step reasoning for complex tasks
- **ReAct Pattern**: Alternating reasoning and acting
- **Role Prompting**: Assigning personas for better responses

### Your First Agent
You built a simple agent that could:
- Detect user intent (greeting, weather, booking, general)
- Extract basic information like locations
- Generate appropriate responses
- Track token usage and estimate costs

```python
# Your first agent from Part 1
class FirstAgent:
    async def process(self, user_message):
        intent = await self.detect_intent(user_message)
        if intent == "weather":
            location = await self.extract_location(user_message)
            return f"The weather in {location} is sunny and 22°C"
        elif intent == "booking":
            return "I can help with bookings. What would you like to book?"
        else:
            return await self.generate_response(user_message)
```

**But this agent had limitations:**
- No memory between conversations
- Couldn't actually DO anything (just talk about weather, not get real data)
- No way to handle multi-step tasks
- No personalization for different users

Today, we fix all of that.

---

## 🎯 What We'll Cover in Part 2

1. **Agent Core Architecture** — The think-act-observe loop that makes agents autonomous
2. **Tool & Function Calling** — Giving your agent hands to interact with the world
3. **Memory Systems** — Making your agent remember users across conversations
4. **Complete WhatsApp Travel Agent** — Putting it all together with a real example

---

# Part 2.1: Agent Core Architecture — The Brain Design

*"An agent is more than an LLM — it's a system with memory, tools, and a decision loop."*

## The Agent Loop: Think → Act → Observe → Repeat

Every autonomous agent follows this fundamental pattern. It's what separates a simple chatbot from a true agent that can accomplish tasks.

```python
class AgentLoop:
    """
    The core loop that makes an agent autonomous
    
    Think: Analyze current state and decide what to do
    Act: Execute a tool or generate a response
    Observe: Process the results of your action
    Repeat until task is complete
    """
    
    def __init__(self, llm, tools, max_iterations=10):
        self.llm = llm
        self.tools = {tool.name: tool for tool in tools}
        self.max_iterations = max_iterations
        self.history = []  # Track all thoughts and actions
        self.state = {}    # Current state of the world
        
    async def run(self, task: str) -> str:
        """
        Run the agent loop on a task
        """
        self.state["task"] = task
        self.state["completed"] = False
        
        print(f"\n🎯 Starting task: {task}")
        print("=" * 50)
        
        for i in range(self.max_iterations):
            print(f"\n🔄 Iteration {i+1}/{self.max_iterations}")
            
            # THINK: Decide what to do next
            thought = await self._think()
            print(f"💭 Thought: {thought['reasoning']}")
            
            # Store in history
            self.history.append({
                "iteration": i,
                "thought": thought
            })
            
            # ACT: Execute if decided
            if thought.get("action"):
                action_result = await self._act(
                    thought["action"]["tool"],
                    thought["action"]["args"]
                )
                print(f"⚡ Action: {thought['action']['tool']}")
                print(f"📊 Result: {action_result}")
                
                # OBSERVE: Process results
                await self._observe(action_result)
                
                # Store in history
                self.history[-1]["action"] = thought["action"]
                self.history[-1]["result"] = action_result
            
            # Check if we're ready to respond
            if thought.get("ready_to_respond"):
                final_response = await self._generate_response()
                self.state["completed"] = True
                print(f"\n✅ Task complete!")
                return final_response
            
            # Check if we're stuck
            if thought.get("stuck"):
                return "I'm having trouble completing this task. Can you provide more guidance?"
        
        return "I've reached the maximum number of steps. Here's what I have so far..."
    
    async def _think(self) -> dict:
        """
        LLM decides next action based on current state
        """
        # Build prompt with current context
        prompt = self._build_thought_prompt()
        
        # Get LLM decision
        response = await self.llm(prompt)
        
        # Parse into structured thought
        return self._parse_thought(response)
    
    async def _act(self, tool_name: str, args: dict) -> any:
        """
        Execute a tool with given arguments
        """
        if tool_name not in self.tools:
            return f"Error: Tool {tool_name} not found"
        
        tool = self.tools[tool_name]
        return await tool.execute(**args)
    
    async def _observe(self, result: any):
        """
        Update state based on action result
        """
        self.state["last_result"] = result
        self.state["step_count"] = self.state.get("step_count", 0) + 1
        
    def _build_thought_prompt(self) -> str:
        """
        Build prompt for the thinking step
        """
        tools_desc = "\n".join([
            f"- {name}: {tool.description}" 
            for name, tool in self.tools.items()
        ])
        
        return f"""
You are an autonomous agent working on a task.

Task: {self.state['task']}

Current state:
{json.dumps(self.state, indent=2)}

Available tools:
{tools_desc}

Recent history:
{self._format_recent_history()}

Think step by step:
1. What do I know now?
2. What information am I missing?
3. What should I do next?

If you need more information, specify an action with a tool.
If you have enough information to respond to the user, say you're ready.

Output format:
{{
    "reasoning": "your step-by-step reasoning",
    "action": {{"tool": "tool_name", "args": {{"arg1": "value1"}}}},
    "ready_to_respond": false,
    "stuck": false
}}
"""
    
    def _parse_thought(self, response: str) -> dict:
        """Parse LLM response into structured thought"""
        # In production, use proper JSON parsing
        # This is simplified
        try:
            return json.loads(response)
        except:
            # Fallback
            return {
                "reasoning": response,
                "action": None,
                "ready_to_respond": True,
                "stuck": False
            }
    
    def _format_recent_history(self) -> str:
        """Format recent history for context"""
        recent = self.history[-3:] if self.history else []
        formatted = []
        for h in recent:
            formatted.append(f"Thought: {h['thought']['reasoning']}")
            if 'action' in h:
                formatted.append(f"Action: {h['action']['tool']}")
                formatted.append(f"Result: {h['result']}")
        return "\n".join(formatted)
    
    async def _generate_response(self) -> str:
        """Generate final response to user"""
        prompt = f"""
Based on the task and all actions taken, generate a final response for the user.

Task: {self.state['task']}

Full history:
{json.dumps(self.history, indent=2)}

Final state:
{json.dumps(self.state, indent=2)}

Response:
"""
        return await self.llm(prompt)
```

## Real Example: Travel Planning Agent

Let's see this loop in action with a travel planning example:

```python
# Define some tools
class FlightSearchTool:
    name = "search_flights"
    description = "Search for available flights between cities"
    
    async def execute(self, origin, destination, date):
        # Simulate API call
        return {
            "flights": [
                {"airline": "Air France", "price": 550, "duration": "7h"},
                {"airline": "Delta", "price": 620, "duration": "7.5h"},
                {"airline": "United", "price": 580, "duration": "8h"}
            ]
        }

class HotelSearchTool:
    name = "search_hotels"
    description = "Search for hotels in a city"
    
    async def execute(self, city, check_in, nights):
        return {
            "hotels": [
                {"name": "Grand Hotel", "price": 200, "rating": 4.5},
                {"name": "Budget Inn", "price": 80, "rating": 3.2},
                {"name": "Luxury Suites", "price": 450, "rating": 4.8}
            ]
        }

class WeatherTool:
    name = "get_weather"
    description = "Get weather forecast for a location"
    
    async def execute(self, location, date):
        return {
            "temperature": 22,
            "condition": "sunny",
            "humidity": 65
        }

# Create agent
tools = [FlightSearchTool(), HotelSearchTool(), WeatherTool()]
agent = AgentLoop(llm=my_llm, tools=tools)

# Run a task
result = await agent.run("Plan a 3-day trip to Paris for under $2000")
```

**What happens inside the loop:**

```
🎯 Starting task: Plan a 3-day trip to Paris for under $2000

🔄 Iteration 1/10
💭 Thought: Need to find flight costs first to see how much budget remains for hotel and activities
⚡ Action: search_flights with {"origin": "current_location", "destination": "Paris", "date": "next_month"}
📊 Result: Found flights from $550-$620

🔄 Iteration 2/10
💭 Thought: Flights will take ~$600. Remaining budget: $1400. Now check hotels.
⚡ Action: search_hotels with {"city": "Paris", "check_in": "next_month", "nights": 3}
📊 Result: Hotels from $80-450 per night. 3 nights = $240-1350.

🔄 Iteration 3/10
💭 Thought: With hotel at $150/night = $450, plus flight $600 = $1050. Remaining $950 for activities and food. Need weather info.
⚡ Action: get_weather with {"location": "Paris", "date": "next_month"}
📊 Result: Weather forecast: 22°C, sunny

🔄 Iteration 4/10
💭 Thought: Have all information. Can create complete plan within budget.
✅ Task complete!

Final Response: "I've planned your 3-day Paris trip under $2000:

✈️ Flights: $600 (Delta, direct)
🏨 Hotel: $450 (Grand Hotel, 3 nights at $150/night)
🎭 Activities: Eiffel Tower, Louvre, Seine cruise (~$200)
🍽️ Food budget: $400 for 3 days
☔ Weather: Sunny, 22°C - perfect for sightseeing!

Would you like me to book any of this for you?"
```

---

## Planning vs Reacting: Two Different Approaches

Not all tasks need the same approach. Sometimes you need to plan ahead; sometimes you need to react immediately.

### Planning Agents

Planning agents create a multi-step strategy upfront before taking any action. This is good for complex, multi-step tasks where order matters.

```python
class PlanningAgent:
    """
    Agent that creates a plan first, then executes it
    """
    
    async def create_plan(self, task: str) -> List[dict]:
        """
        Break down task into a sequence of steps
        """
        prompt = f"""
Task: {task}

Create a step-by-step plan to accomplish this task.
For each step, specify:
- What action to take
- What tool to use (if any)
- What information to gather

Return as JSON array.
"""
        response = await self.llm(prompt)
        return json.loads(response)
    
    async def execute_plan(self, plan: List[dict]) -> List[any]:
        """
        Execute plan steps in sequence
        """
        results = []
        for step in plan:
            print(f"▶️ Executing step: {step['description']}")
            
            if step.get('tool'):
                result = await self.tools[step['tool']].execute(**step.get('args', {}))
                results.append(result)
                print(f"✅ Result: {result}")
            else:
                # Reasoning step
                thought = await self.llm(step['reasoning_prompt'])
                results.append(thought)
        
        return results
    
    async def handle_request(self, task: str) -> str:
        """
        Handle a request by planning first
        """
        # Step 1: Create plan
        plan = await self.create_plan(task)
        print(f"📋 Created plan with {len(plan)} steps")
        
        # Step 2: Execute plan
        results = await self.execute_plan(plan)
        
        # Step 3: Synthesize results
        return await self.synthesize_results(task, results)
```

**Example: Wedding Planning**
```python
task = "Plan my wedding for 150 people in June with $50,000 budget"

plan = [
    {"step": 1, "description": "Determine budget breakdown", "tool": "budget_calculator"},
    {"step": 2, "description": "Find venues available in June", "tool": "venue_search"},
    {"step": 3, "description": "Check venue prices against budget", "depends": [1,2]},
    {"step": 4, "description": "Book top choice venue", "tool": "venue_booking"},
    {"step": 5, "description": "Find caterers for venue capacity", "tool": "catering_search"}
]
```

### Reacting Agents

Reacting agents respond immediately to each input without advance planning. This is good for simple, immediate tasks.

```python
class ReactingAgent:
    """
    Agent that reacts immediately to each input
    """
    
    async def react(self, user_input: str) -> str:
        """
        Immediate reaction to input
        """
        # Check if tool needed immediately
        needs_tool = await self._detect_tool_need(user_input)
        
        if needs_tool:
            tool_name, args = await self._select_tool(user_input)
            result = await self.tools[tool_name].execute(**args)
            return await self._format_response(user_input, result)
        else:
            return await self.llm(f"Respond to: {user_input}")
    
    async def _detect_tool_need(self, text: str) -> bool:
        """Detect if user needs a tool immediately"""
        # Simple keyword matching
        tool_keywords = ['weather', 'flight', 'book', 'search', 'find']
        return any(word in text.lower() for word in tool_keywords)
```

**Example: Quick Queries**
```python
user: "What's the weather?"
agent: Immediately calls weather API → responds with current weather

user: "Book that flight"
agent: Immediately triggers booking → confirms

user: "Tell me a joke"
agent: Just responds with LLM (no tool needed)
```

### Hybrid Agents (Best of Both)

Most production agents use a hybrid approach: plan at a high level, then react within each step.

```python
class HybridAgent:
    """
    Agent that plans at high level but reacts within each step
    """
    
    def __init__(self):
        self.planner = PlanningAgent()
        self.reactor = ReactingAgent()
        self.current_plan = None
        self.current_step = 0
        
    async def process(self, user_input: str) -> str:
        # Check if this is a new complex task
        if self._needs_planning(user_input):
            # Create high-level plan
            self.current_plan = await self.planner.create_plan(user_input)
            self.current_step = 0
            return f"I've created a plan with {len(self.current_plan)} steps. Let's start with step 1: {self.current_plan[0]['description']}"
        
        # If we're executing a plan, handle current step
        if self.current_plan and self.current_step < len(self.current_plan):
            step = self.current_plan[self.current_step]
            
            # React within this step
            result = await self.reactor.react(f"{step['description']}: {user_input}")
            
            # Move to next step
            self.current_step += 1
            
            if self.current_step < len(self.current_plan):
                return f"{result}\n\nNext, {self.current_plan[self.current_step]['description']}"
            else:
                self.current_plan = None
                return f"{result}\n\nPlan complete! Is there anything else I can help with?"
        
        # Simple query - just react
        return await self.reactor.react(user_input)
```

**Example Conversation:**
```
User: "Plan my trip to Japan"
Agent: "I've created a plan with 6 steps. Let's start with step 1: What's your budget?"

User: "$3000"
Agent: "Great! Step 2: When would you like to travel?"

User: "Next month"
Agent: "Perfect. Step 3: Let me search for flights..."
```

---

## Framework Options for Agent Architecture

### LangChain — The Most Mature Ecosystem

LangChain provides pre-built components for agents, making it easy to get started.

```python
from langchain.agents import create_openai_tools_agent
from langchain.agents import AgentExecutor
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

class LangChainAgent:
    def __init__(self):
        # Define tools
        tools = [
            Tool(
                name="get_weather",
                func=self.get_weather,
                description="Get current weather for a location"
            ),
            Tool(
                name="search_flights",
                func=self.search_flights,
                description="Search for available flights"
            )
        ]
        
        # Create prompt
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful travel assistant."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        
        # Create agent
        llm = ChatOpenAI(model="gpt-4", temperature=0)
        agent = create_openai_tools_agent(llm, tools, prompt)
        
        # Add memory
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Create executor
        self.executor = AgentExecutor(
            agent=agent,
            tools=tools,
            memory=memory,
            verbose=True
        )
    
    async def run(self, input: str) -> str:
        result = await self.executor.ainvoke({"input": input})
        return result["output"]
    
    def get_weather(self, location):
        # Implementation
        return f"Weather in {location}: sunny, 22°C"
    
    def search_flights(self, origin, destination, date):
        # Implementation
        return f"Flights from {origin} to {destination} on {date}"
```

### LangGraph — Graph-Based Workflows

LangGraph is perfect when you need complex, non-linear workflows with cycles and conditions.

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    task: str
    step: int
    results: dict

class LangGraphAgent:
    def __init__(self):
        # Build graph
        workflow = StateGraph(AgentState)
        
        # Add nodes
        workflow.add_node("analyze", self.analyze_task)
        workflow.add_node("search", self.search_info)
        workflow.add_node("process", self.process_results)
        workflow.add_node("respond", self.generate_response)
        
        # Add edges
        workflow.set_entry_point("analyze")
        workflow.add_edge("analyze", "search")
        workflow.add_edge("search", "process")
        
        # Conditional edge
        workflow.add_conditional_edges(
            "process",
            self.should_continue,
            {
                "continue": "search",  # Loop back for more info
                "respond": "respond"
            }
        )
        
        workflow.add_edge("respond", END)
        
        # Compile
        self.app = workflow.compile()
    
    async def analyze_task(self, state: AgentState) -> AgentState:
        """Analyze the task and determine what's needed"""
        # Implementation
        state["step"] = 1
        return state
    
    async def search_info(self, state: AgentState) -> AgentState:
        """Search for information"""
        # Implementation
        return state
    
    async def process_results(self, state: AgentState) -> AgentState:
        """Process search results"""
        # Implementation
        return state
    
    def should_continue(self, state: AgentState) -> str:
        """Decide whether to continue searching or respond"""
        if state["step"] < 3:
            return "continue"
        return "respond"
    
    async def generate_response(self, state: AgentState) -> AgentState:
        """Generate final response"""
        # Implementation
        return state
```

---

# Part 2.2: Tool & Function Calling — Giving Your Agent Hands

*"An agent without tools is just a chatbot with attitude."*

Tools transform conversational AI into actionable intelligence. This section covers how to design, build, and orchestrate tools that agents can use.

## Tool Design Principles

Every tool needs three things:
1. **Name**: Unique identifier
2. **Description**: Tells the LLM when to use this tool
3. **Parameters**: JSON schema defining what arguments the tool expects

```python
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
import json

class Tool(ABC):
    """Base class for all tools"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    @abstractmethod
    async def execute(self, **kwargs) -> Any:
        """Execute the tool with given arguments"""
        pass
    
    def get_schema(self) -> Dict:
        """Get OpenAI function schema for this tool"""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.get_parameters()
            }
        }
    
    @abstractmethod
    def get_parameters(self) -> Dict:
        """Get JSON schema for tool parameters"""
        pass

class WeatherTool(Tool):
    """Get current weather for a location"""
    
    def __init__(self):
        super().__init__(
            name="get_weather",
            description="Get current weather for any location"
        )
        self.api_key = os.getenv("WEATHER_API_KEY")
        
    def get_parameters(self) -> Dict:
        return {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name or coordinates (e.g., 'Tokyo, Japan')"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "default": "celsius",
                    "description": "Temperature unit"
                }
            },
            "required": ["location"]
        }
    
    async def execute(self, location: str, unit: str = "celsius") -> Dict:
        """
        Call weather API and return formatted result
        """
        # In production, call real weather API
        # This is a simulation
        weather_data = {
            "tokyo": {"temp": 22, "condition": "sunny", "humidity": 65},
            "paris": {"temp": 18, "condition": "cloudy", "humidity": 70},
            "london": {"temp": 15, "condition": "rainy", "humidity": 80},
            "new york": {"temp": 25, "condition": "sunny", "humidity": 60}
        }
        
        # Normalize location
        location_key = location.lower().split(',')[0].strip()
        
        if location_key in weather_data:
            data = weather_data[location_key]
            if unit == "fahrenheit":
                data["temp"] = data["temp"] * 9/5 + 32
            return data
        else:
            return {"error": f"Weather data not available for {location}"}

class FlightSearchTool(Tool):
    """Search for available flights"""
    
    def __init__(self):
        super().__init__(
            name="search_flights",
            description="Search for available flights between cities"
        )
        
    def get_parameters(self) -> Dict:
        return {
            "type": "object",
            "properties": {
                "origin": {
                    "type": "string",
                    "description": "Origin airport code or city name"
                },
                "destination": {
                    "type": "string",
                    "description": "Destination airport code or city name"
                },
                "date": {
                    "type": "string",
                    "description": "Departure date (YYYY-MM-DD)"
                },
                "passengers": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 9,
                    "default": 1,
                    "description": "Number of passengers"
                },
                "cabin_class": {
                    "type": "string",
                    "enum": ["economy", "premium_economy", "business", "first"],
                    "default": "economy",
                    "description": "Travel class"
                }
            },
            "required": ["origin", "destination", "date"]
        }
    
    async def execute(self, origin: str, destination: str, date: str, 
                     passengers: int = 1, cabin_class: str = "economy") -> Dict:
        """
        Search for flights
        """
        # Simulate flight search
        flights = [
            {
                "airline": "Air France",
                "flight_number": "AF123",
                "price": 550,
                "currency": "USD",
                "duration": "7h 15m",
                "stops": 0,
                "departure_time": "09:30",
                "arrival_time": "16:45"
            },
            {
                "airline": "Delta",
                "flight_number": "DL456",
                "price": 620,
                "currency": "USD",
                "duration": "7h 45m",
                "stops": 0,
                "departure_time": "11:15",
                "arrival_time": "19:00"
            },
            {
                "airline": "United",
                "flight_number": "UA789",
                "price": 580,
                "currency": "USD",
                "duration": "8h 30m",
                "stops": 1,
                "departure_time": "14:20",
                "arrival_time": "22:50"
            }
        ]
        
        return {
            "origin": origin,
            "destination": destination,
            "date": date,
            "passengers": passengers,
            "cabin_class": cabin_class,
            "flights": flights
        }

class HotelSearchTool(Tool):
    """Search for hotels in a city"""
    
    def __init__(self):
        super().__init__(
            name="search_hotels",
            description="Search for hotels in a city"
        )
        
    def get_parameters(self) -> Dict:
        return {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name"
                },
                "check_in": {
                    "type": "string",
                    "description": "Check-in date (YYYY-MM-DD)"
                },
                "check_out": {
                    "type": "string",
                    "description": "Check-out date (YYYY-MM-DD)"
                },
                "guests": {
                    "type": "integer",
                    "minimum": 1,
                    "default": 2,
                    "description": "Number of guests"
                },
                "stars": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 5,
                    "description": "Minimum star rating"
                }
            },
            "required": ["city", "check_in", "check_out"]
        }
    
    async def execute(self, city: str, check_in: str, check_out: str,
                     guests: int = 2, stars: int = None) -> Dict:
        """
        Search for hotels
        """
        # Calculate nights
        from datetime import datetime
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
        nights = (check_out_date - check_in_date).days
        
        # Simulate hotel search
        hotels = [
            {
                "name": "Grand Hotel",
                "price_per_night": 200,
                "total_price": 200 * nights,
                "rating": 4.5,
                "stars": 5,
                "amenities": ["pool", "spa", "restaurant", "wifi"]
            },
            {
                "name": "City Central",
                "price_per_night": 150,
                "total_price": 150 * nights,
                "rating": 4.2,
                "stars": 4,
                "amenities": ["restaurant", "wifi", "gym"]
            },
            {
                "name": "Budget Inn",
                "price_per_night": 80,
                "total_price": 80 * nights,
                "rating": 3.5,
                "stars": 3,
                "amenities": ["wifi"]
            }
        ]
        
        # Filter by stars if specified
        if stars:
            hotels = [h for h in hotels if h["stars"] >= stars]
        
        return {
            "city": city,
            "check_in": check_in,
            "check_out": check_out,
            "nights": nights,
            "guests": guests,
            "hotels": hotels
        }
```

## Tool Registry: Managing Multiple Tools

```python
class ToolRegistry:
    """
    Registry for managing multiple tools
    """
    
    def __init__(self):
        self.tools = {}
        
    def register(self, tool: Tool):
        """Register a tool"""
        self.tools[tool.name] = tool
        print(f"✅ Registered tool: {tool.name}")
        
    def get(self, name: str) -> Optional[Tool]:
        """Get tool by name"""
        return self.tools.get(name)
    
    def get_all_schemas(self) -> List[Dict]:
        """Get schemas for all tools (for OpenAI)"""
        return [tool.get_schema() for tool in self.tools.values()]
    
    def get_descriptions(self) -> str:
        """Get formatted descriptions for prompting"""
        return "\n".join([
            f"- {tool.name}: {tool.description}"
            for tool in self.tools.values()
        ])
    
    async def execute(self, name: str, **kwargs) -> Any:
        """Execute a tool by name"""
        tool = self.get(name)
        if not tool:
            raise ValueError(f"Tool '{name}' not found")
        return await tool.execute(**kwargs)

# Usage
registry = ToolRegistry()
registry.register(WeatherTool())
registry.register(FlightSearchTool())
registry.register(HotelSearchTool())

# Later
result = await registry.execute(
    "get_weather",
    location="Tokyo",
    unit="celsius"
)
```

## Tool Calling with OpenAI

```python
class ToolCallingAgent:
    """
    Agent that can call tools using OpenAI function calling
    """
    
    def __init__(self, registry: ToolRegistry):
        self.registry = registry
        self.client = openai.AsyncOpenAI()
        self.messages = []
        
    async def process(self, user_message: str) -> str:
        # Add user message
        self.messages.append({"role": "user", "content": user_message})
        
        # Get response from OpenAI with tools
        response = await self.client.chat.completions.create(
            model="gpt-4",
            messages=self.messages,
            tools=self.registry.get_all_schemas(),
            tool_choice="auto"
        )
        
        message = response.choices[0].message
        
        # Check if tool calls are needed
        if message.tool_calls:
            # Add assistant message with tool calls
            self.messages.append({
                "role": "assistant",
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    }
                    for tc in message.tool_calls
                ]
            })
            
            # Execute each tool call
            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                # Execute tool
                result = await self.registry.execute(function_name, **function_args)
                
                # Add tool response
                self.messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                })
            
            # Get final response
            final_response = await self.client.chat.completions.create(
                model="gpt-4",
                messages=self.messages
            )
            
            final_message = final_response.choices[0].message.content
            self.messages.append({"role": "assistant", "content": final_message})
            return final_message
        
        # No tool calls needed
        self.messages.append({"role": "assistant", "content": message.content})
        return message.content

# Usage
agent = ToolCallingAgent(registry)
response = await agent.process("What's the weather in Tokyo?")
```

## Error Handling and Retries

APIs fail. Networks timeout. Your agent needs to handle this gracefully.

```python
class ResilientTool(Tool):
    """
    Wrapper that adds retry logic to any tool
    """
    
    def __init__(self, tool: Tool, max_retries: int = 3):
        self.tool = tool
        self.max_retries = max_retries
        self.name = tool.name
        self.description = tool.description
        
    def get_parameters(self) -> Dict:
        return self.tool.get_parameters()
    
    async def execute(self, **kwargs) -> Any:
        last_error = None
        
        for attempt in range(self.max_retries):
            try:
                print(f"🔧 Tool {self.name} attempt {attempt + 1}/{self.max_retries}")
                return await self.tool.execute(**kwargs)
                
            except httpx.TimeoutException as e:
                last_error = e
                wait_time = (2 ** attempt) + (0.1 * attempt)
                print(f"⏱️ Timeout, retrying in {wait_time:.1f}s...")
                await asyncio.sleep(wait_time)
                
            except httpx.HTTPStatusError as e:
                if e.response.status_code >= 500:
                    # Server error, retry
                    last_error = e
                    wait_time = (2 ** attempt)
                    print(f"⚠️ Server error {e.response.status_code}, retrying...")
                    await asyncio.sleep(wait_time)
                else:
                    # Client error, don't retry
                    raise
                    
            except Exception as e:
                last_error = e
                print(f"❌ Unexpected error: {e}")
                if attempt == self.max_retries - 1:
                    break
        
        return {
            "error": f"Tool {self.name} failed after {self.max_retries} attempts",
            "last_error": str(last_error)
        }

class CircuitBreaker:
    """
    Circuit breaker pattern to prevent cascading failures
    """
    
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
        
    async def call(self, func, *args, **kwargs):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF_OPEN"
                print("🔓 Circuit half-open, testing...")
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = await func(*args, **kwargs)
            
            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
                print("🔒 Circuit closed (recovered)")
            
            return result
            
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
                print(f"🔓 Circuit OPEN after {self.failure_count} failures")
            
            raise e
```

## Tool Orchestration: Chaining Multiple Tools

Real tasks need multiple tools working together. Here's how to orchestrate them:

```python
class ToolOrchestrator:
    """
    Orchestrate multiple tools to complete complex tasks
    """
    
    def __init__(self, registry: ToolRegistry):
        self.registry = registry
        
    async def book_complete_trip(self, request: Dict) -> Dict:
        """
        Book a complete trip: flights + hotel + car + activities
        """
        results = {}
        
        # Step 1: Search in parallel
        print("🔍 Searching for options...")
        search_tasks = []
        
        if request.get('flight_needed'):
            search_tasks.append(
                self.registry.execute(
                    "search_flights",
                    origin=request['origin'],
                    destination=request['destination'],
                    date=request['date'],
                    passengers=request.get('passengers', 1)
                )
            )
        
        if request.get('hotel_needed'):
            search_tasks.append(
                self.registry.execute(
                    "search_hotels",
                    city=request['destination'],
                    check_in=request['date'],
                    check_out=request.get('return_date')
                )
            )
        
        # Execute searches in parallel
        search_results = await asyncio.gather(*search_tasks)
        
        # Parse results
        if request.get('flight_needed'):
            results['flights'] = search_results[0]
        if request.get('hotel_needed'):
            results['hotels'] = search_results[-1]
        
        # Step 2: Select best options (could use LLM here)
        best_flight = results['flights']['flights'][0]
        best_hotel = results['hotels']['hotels'][0]
        
        # Step 3: Book in sequence
        print("📅 Booking selected options...")
        
        booking_results = {}
        
        if request.get('flight_needed'):
            booking_results['flight'] = await self.registry.execute(
                "book_flight",
                flight_id=best_flight['flight_number'],
                passengers=request.get('passengers', 1)
            )
        
        if request.get('hotel_needed'):
            booking_results['hotel'] = await self.registry.execute(
                "book_hotel",
                hotel_name=best_hotel['name'],
                check_in=request['date'],
                check_out=request.get('return_date')
            )
        
        # Step 4: Arrange transport if needed
        if request.get('taxi_needed'):
            booking_results['taxi'] = await self.registry.execute(
                "book_taxi",
                pickup="airport",
                dropoff=best_hotel['name'],
                datetime=request['date']
            )
        
        # Step 5: Send confirmation
        booking_results['confirmation'] = await self.registry.execute(
            "send_confirmation",
            email=request['email'],
            booking_details=booking_results
        )
        
        return {
            "status": "success",
            "message": "Your trip has been booked!",
            "details": booking_results
        }

# Example usage
request = {
    "origin": "JFK",
    "destination": "Paris",
    "date": "2024-07-15",
    "return_date": "2024-07-22",
    "passengers": 2,
    "email": "user@example.com",
    "flight_needed": True,
    "hotel_needed": True,
    "taxi_needed": True
}

orchestrator = ToolOrchestrator(registry)
result = await orchestrator.book_complete_trip(request)
```

## Real-World Tools

### SerpAPI — Web Search

```python
import aiohttp
from typing import List, Dict

class WebSearchTool(Tool):
    """
    Search the web using SerpAPI
    """
    
    def __init__(self, api_key: str):
        super().__init__(
            name="web_search",
            description="Search the web for current information"
        )
        self.api_key = api_key
        self.base_url = "https://serpapi.com/search"
        
    def get_parameters(self) -> Dict:
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query"
                },
                "num_results": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 10,
                    "default": 5,
                    "description": "Number of results to return"
                }
            },
            "required": ["query"]
        }
    
    async def execute(self, query: str, num_results: int = 5) -> Dict:
        """
        Execute web search
        """
        params = {
            "q": query,
            "api_key": self.api_key,
            "num": num_results,
            "engine": "google"
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url, params=params) as response:
                data = await response.json()
                
                # Format results
                results = []
                for result in data.get("organic_results", [])[:num_results]:
                    results.append({
                        "title": result.get("title"),
                        "link": result.get("link"),
                        "snippet": result.get("snippet")
                    })
                
                return {
                    "query": query,
                    "results": results,
                    "total_results": len(results)
                }
```

### Zapier AI — 5000+ App Integrations

```python
class ZapierTool(Tool):
    """
    Connect to 5000+ apps via Zapier
    """
    
    def __init__(self, zapier_api_key: str):
        super().__init__(
            name="zapier_action",
            description="Execute actions in external apps (Gmail, Slack, Salesforce, etc.)"
        )
        self.api_key = zapier_api_key
        self.base_url = "https://actions.zapier.com/api/v1"
        
    def get_parameters(self) -> Dict:
        return {
            "type": "object",
            "properties": {
                "app": {
                    "type": "string",
                    "enum": ["gmail", "slack", "sheets", "salesforce", "calendar"],
                    "description": "Target application"
                },
                "action": {
                    "type": "string",
                    "description": "Action to perform"
                },
                "data": {
                    "type": "object",
                    "description": "Action-specific data"
                }
            },
            "required": ["app", "action", "data"]
        }
    
    async def execute(self, app: str, action: str, data: Dict) -> Dict:
        """
        Execute Zapier action
        """
        # Map to specific Zapier webhooks
        app_endpoints = {
            "gmail": "send_email",
            "slack": "post_message",
            "sheets": "add_row",
            "salesforce": "create_lead",
            "calendar": "create_event"
        }
        
        endpoint = app_endpoints.get(app)
        if not endpoint:
            return {"error": f"Unknown app: {app}"}
        
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                return await response.json()
```

---

# Part 2.3: Memory Systems — Making Your Agent Remember

*"An agent without memory meets the same user as a stranger every time."*

## Types of Memory

| Type | Duration | Storage | Purpose | Example |
|------|----------|---------|---------|---------|
| Short-term | Minutes | In-memory | Current conversation | Last 10 messages |
| Episodic | Days/weeks | Redis | Past interactions | Previous bookings |
| Semantic | Permanent | Vector DB | User facts | Dietary preferences |
| Working | Session | In-memory | Current task | Booking draft |

## Short-Term Memory (Conversation Buffer)

```python
from collections import deque
from typing import List, Dict
import time

class ShortTermMemory:
    """
    In-memory buffer for recent conversation
    """
    
    def __init__(self, max_messages: int = 10):
        self.messages = deque(maxlen=max_messages)
        
    def add(self, role: str, content: str):
        """Add a message to memory"""
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": time.time()
        })
    
    def get_recent(self, n: int = None) -> List[Dict]:
        """Get n most recent messages"""
        if n is None:
            n = len(self.messages)
        return list(self.messages)[-n:]
    
    def get_context(self, max_tokens: int = 2000) -> str:
        """
        Get conversation context as string, respecting token limits
        """
        context = ""
        token_estimate = 0
        
        # Go from most recent to oldest
        for msg in reversed(self.messages):
            msg_text = f"{msg['role']}: {msg['content']}\n"
            # Rough token estimate (4 chars ≈ 1 token)
            msg_tokens = len(msg_text) // 4
            
            if token_estimate + msg_tokens > max_tokens:
                break
                
            context = msg_text + context
            token_estimate += msg_tokens
        
        return context
    
    def clear(self):
        """Clear all messages"""
        self.messages.clear()
```

## Long-Term Memory with Redis

```python
import redis
import json
from datetime import datetime, timedelta
from typing import Optional, Any

class LongTermMemory:
    """
    Redis-based persistent memory
    """
    
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis = redis.from_url(redis_url, decode_responses=True)
        self.default_ttl = 60 * 60 * 24 * 30  # 30 days
        
    def _user_key(self, user_id: str, namespace: str) -> str:
        """Generate Redis key for user data"""
        return f"user:{user_id}:{namespace}"
    
    async def remember_fact(self, user_id: str, key: str, value: Any, ttl: int = None):
        """
        Store a fact about a user
        """
        facts_key = self._user_key(user_id, "facts")
        
        # Get existing facts
        facts = self.redis.get(facts_key)
        if facts:
            facts = json.loads(facts)
        else:
            facts = {}
        
        # Update fact
        facts[key] = {
            "value": value,
            "updated_at": datetime.now().isoformat()
        }
        
        # Store back
        self.redis.setex(
            facts_key,
            ttl or self.default_ttl,
            json.dumps(facts)
        )
        
    async def recall_fact(self, user_id: str, key: str) -> Optional[Any]:
        """
        Recall a specific fact about a user
        """
        facts_key = self._user_key(user_id, "facts")
        facts = self.redis.get(facts_key)
        
        if facts:
            facts = json.loads(facts)
            return facts.get(key, {}).get("value")
        
        return None
    
    async def recall_all_facts(self, user_id: str) -> Dict:
        """
        Recall all facts about a user
        """
        facts_key = self._user_key(user_id, "facts")
        facts = self.redis.get(facts_key)
        return json.loads(facts) if facts else {}
    
    async def store_conversation(self, user_id: str, conversation: Dict):
        """
        Store a conversation episode
        """
        conv_key = self._user_key(user_id, f"conv:{datetime.now().strftime('%Y%m%d')}")
        
        # Append to conversation list
        conv_list = self.redis.get(conv_key)
        if conv_list:
            conv_list = json.loads(conv_list)
        else:
            conv_list = []
        
        conv_list.append({
            **conversation,
            "timestamp": datetime.now().isoformat()
        })
        
        # Keep last 50 conversations per day
        conv_list = conv_list[-50:]
        
        self.redis.setex(
            conv_key,
            self.default_ttl,
            json.dumps(conv_list)
        )
    
    async def get_recent_conversations(self, user_id: str, days: int = 7) -> List[Dict]:
        """
        Get conversations from last N days
        """
        all_convs = []
        
        for i in range(days):
            date = (datetime.now() - timedelta(days=i)).strftime('%Y%m%d')
            conv_key = self._user_key(user_id, f"conv:{date}")
            convs = self.redis.get(conv_key)
            if convs:
                all_convs.extend(json.loads(convs))
        
        return sorted(all_convs, key=lambda x: x['timestamp'], reverse=True)
```

## Semantic Memory with Embeddings

```python
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import faiss

class SemanticMemory:
    """
    Memory that can search by meaning, not just keywords
    """
    
    def __init__(self, dimension: int = 384):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.dimension = dimension
        self.memories = []  # List of {"text": str, "embedding": list, "metadata": dict}
        
        # FAISS index for fast similarity search
        self.index = faiss.IndexFlatL2(dimension)
        
    def add_memory(self, text: str, metadata: Dict = None):
        """
        Add a memory with its embedding
        """
        # Create embedding
        embedding = self.model.encode([text])[0]
        
        # Store
        memory = {
            "text": text,
            "embedding": embedding.tolist(),
            "metadata": metadata or {},
            "timestamp": datetime.now().isoformat()
        }
        self.memories.append(memory)
        
        # Add to FAISS index
        self.index.add(np.array([embedding]).astype('float32'))
        
        return memory
    
    def search(self, query: str, top_k: int = 5, threshold: float = 0.7) -> List[Dict]:
        """
        Search for semantically similar memories
        """
        # Embed query
        query_emb = self.model.encode([query])[0].astype('float32')
        
        # Search FAISS index
        distances, indices = self.index.search(
            np.array([query_emb]), 
            min(top_k, len(self.memories))
        )
        
        # Format results
        results = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx < len(self.memories):
                memory = self.memories[idx]
                similarity = 1 / (1 + distance)  # Convert distance to similarity
                
                if similarity >= threshold:
                    results.append({
                        **memory,
                        "similarity": float(similarity)
                    })
        
        return results
    
    def search_by_metadata(self, **filters) -> List[Dict]:
        """
        Search memories by metadata
        """
        results = []
        for memory in self.memories:
            match = True
            for key, value in filters.items():
                if memory['metadata'].get(key) != value:
                    match = False
                    break
            if match:
                results.append(memory)
        return results
    
    def save(self, path: str):
        """Save to disk"""
        import pickle
        with open(path, 'wb') as f:
            pickle.dump({
                'memories': self.memories,
                'index': faiss.serialize_index(self.index)
            }, f)
    
    def load(self, path: str):
        """Load from disk"""
        import pickle
        with open(path, 'rb') as f:
            data = pickle.load(f)
            self.memories = data['memories']
            self.index = faiss.deserialize_index(data['index'])
```

## Working Memory (Current Task State)

```python
class WorkingMemory:
    """
    Temporary memory for current task
    """
    
    def __init__(self):
        self.state = {}
        self.stack = []  # For nested operations
        
    def set(self, key: str, value: Any):
        """Set a value in working memory"""
        self.state[key] = value
        
    def get(self, key: str, default=None) -> Any:
        """Get a value from working memory"""
        return self.state.get(key, default)
    
    def update(self, updates: Dict):
        """Update multiple values"""
        self.state.update(updates)
    
    def push(self, frame: Dict):
        """Push a new frame onto the stack"""
        self.stack.append(frame)
        
    def pop(self) -> Dict:
        """Pop the top frame from the stack"""
        return self.stack.pop() if self.stack else {}
    
    def clear(self):
        """Clear working memory"""
        self.state.clear()
        self.stack.clear()
    
    def get_context(self) -> str:
        """Get formatted context for prompts"""
        return f"Current state: {json.dumps(self.state, indent=2)}"
```

## Complete Memory System

```python
class MemorySystem:
    """
    Complete memory system with all types
    """
    
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.short_term = ShortTermMemory(max_messages=20)
        self.long_term = LongTermMemory(redis_url)
        self.semantic = SemanticMemory()
        self.working = WorkingMemory()
        
    async def add_interaction(self, user_id: str, role: str, content: str):
        """Add an interaction to all relevant memories"""
        
        # Short-term memory
        self.short_term.add(role, content)
        
        # Extract facts for long-term memory
        if role == 'user':
            facts = await self._extract_facts(content)
            for key, value in facts.items():
                await self.long_term.remember_fact(user_id, key, value)
            
            # Add to semantic memory
            self.semantic.add_memory(
                text=content,
                metadata={"user_id": user_id, "role": role}
            )
    
    async def get_context(self, user_id: str) -> str:
        """Build comprehensive context from all memories"""
        
        context_parts = []
        
        # Recent conversation
        recent = self.short_term.get_context()
        if recent:
            context_parts.append("Recent conversation:\n" + recent)
        
        # User facts
        facts = await self.long_term.recall_all_facts(user_id)
        if facts:
            facts_text = "I know about you:\n"
            for k, v in facts.items():
                facts_text += f"- {k}: {v['value']}\n"
            context_parts.append(facts_text)
        
        # Working memory state
        working_context = self.working.get_context()
        if working_context:
            context_parts.append(working_context)
        
        return "\n\n".join(context_parts)
    
    async def _extract_facts(self, message: str) -> Dict:
        """Extract facts from user message using LLM"""
        # This would use an LLM in production
        facts = {}
        
        message_lower = message.lower()
        
        # Simple pattern matching
        if "vegetarian" in message_lower:
            facts["dietary_preference"] = "vegetarian"
        if "vegan" in message_lower:
            facts["dietary_preference"] = "vegan"
        if "window seat" in message_lower:
            facts["seat_preference"] = "window"
        if "aisle seat" in message_lower:
            facts["seat_preference"] = "aisle"
        if "allergic" in message_lower:
            # Extract allergy
            pass
        
        return facts
    
    def clear_session(self):
        """Clear short-term and working memory for new session"""
        self.short_term.clear()
        self.working.clear()
```

---

# Part 2.4: Complete WhatsApp Travel Agent

Now let's put everything together into a complete, production-ready travel agent for WhatsApp.

```python
import asyncio
import json
from datetime import datetime, timedelta
from typing import Optional, Dict, List
import hashlib

class WhatsAppTravelAgent:
    """
    Complete travel agent for WhatsApp with memory and tools
    """
    
    def __init__(self):
        # Initialize components
        self.memory = MemorySystem()
        self.registry = ToolRegistry()
        self.llm = openai.AsyncOpenAI()
        
        # Register tools
        self._register_tools()
        
        # Track active conversations
        self.active_conversations = {}
        
    def _register_tools(self):
        """Register all available tools"""
        self.registry.register(WeatherTool())
        self.registry.register(FlightSearchTool())
        self.registry.register(HotelSearchTool())
        
        # Wrap with resilience
        for name in list(self.registry.tools.keys()):
            self.registry.tools[name] = ResilientTool(self.registry.tools[name])
    
    async def process_message(self, 
                             user_id: str, 
                             message: str, 
                             session_id: Optional[str] = None) -> str:
        """
        Process incoming WhatsApp message
        """
        # Create session if needed
        if not session_id:
            session_id = hashlib.md5(f"{user_id}:{datetime.now().date()}".encode()).hexdigest()
        
        print(f"\n📱 [{user_id}] {message}")
        print("=" * 50)
        
        # Add to memory
        await self.memory.add_interaction(user_id, "user", message)
        
        # Check if this is a new conversation
        if session_id not in self.active_conversations:
            self.active_conversations[session_id] = {
                "user_id": user_id,
                "started_at": datetime.now(),
                "state": "new"
            }
            print(f"🆕 New session: {session_id}")
        
        # Get conversation context
        context = await self.memory.get_context(user_id)
        
        # Detect intent
        intent = await self._detect_intent(message, context)
        print(f"🎯 Intent: {intent['type']}")
        
        # Handle based on intent
        if intent['type'] == 'greeting':
            response = await self._handle_greeting(user_id, context)
            
        elif intent['type'] == 'flight_search':
            response = await self._handle_flight_search(message, user_id, intent)
            
        elif intent['type'] == 'hotel_search':
            response = await self._handle_hotel_search(message, user_id, intent)
            
        elif intent['type'] == 'booking':
            response = await self._handle_booking(message, user_id, intent)
            
        elif intent['type'] == 'weather':
            response = await self._handle_weather(message, user_id, intent)
            
        elif intent['type'] == 'recommendation':
            response = await self._handle_recommendation(message, user_id, intent)
            
        else:
            response = await self._handle_general(message, context)
        
        # Add response to memory
        await self.memory.add_interaction(user_id, "assistant", response)
        
        # Update session
        self.active_conversations[session_id]["last_message"] = datetime.now()
        
        return response
    
    async def _detect_intent(self, message: str, context: str) -> Dict:
        """
        Detect user intent using LLM
        """
        prompt = f"""
Analyze this user message and determine intent.

Message: "{message}"

Context: {context}

Possible intents:
- greeting: User is saying hello or starting conversation
- flight_search: User wants to search for flights
- hotel_search: User wants to search for hotels
- booking: User wants to book something
- weather: User wants weather information
- recommendation: User wants recommendations
- general: Other questions

Return JSON with:
- type: the intent type
- confidence: 0-1 score
- entities: extracted information (destination, date, etc.)

JSON:
"""
        
        response = await self.llm.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You extract intent and entities from messages."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            response_format={"type": "json_object"}
        )
        
        return json.loads(response.choices[0].message.content)
    
    async def _handle_greeting(self, user_id: str, context: str) -> str:
        """
        Handle greeting with personalization
        """
        # Check if we know this user
        facts = await self.memory.long_term.recall_all_facts(user_id)
        
        if facts:
            name = facts.get('name', {}).get('value', 'there')
            return f"Welcome back, {name}! 👋 How can I help you with your travels today?"
        else:
            return "Hello! I'm your travel assistant. I can help you find flights, hotels, and plan trips. What are you looking for?"
    
    async def _handle_flight_search(self, message: str, user_id: str, intent: Dict) -> str:
        """
        Handle flight search with preferences
        """
        # Extract search parameters
        params = intent.get('entities', {})
        destination = params.get('destination')
        date = params.get('date', 'next week')
        origin = params.get('origin', 'your location')
        passengers = params.get('passengers', 1)
        
        # Get user preferences
        preferences = await self.memory.long_term.recall_all_facts(user_id)
        seat_pref = preferences.get('seat_preference', {}).get('value')
        cabin_pref = preferences.get('cabin_preference', {}).get('value', 'economy')
        
        # Search flights
        try:
            result = await self.registry.execute(
                "search_flights",
                origin=origin,
                destination=destination or "popular destinations",
                date=date,
                passengers=passengers,
                cabin_class=cabin_pref
            )
            
            # Format response
            flights = result.get('flights', [])
            if not flights:
                return f"I couldn't find any flights to {destination or 'your destination'} on {date}. Would you like to try different dates?"
            
            response = f"✈️ Here are some flight options to {destination or 'your destination'}:\n\n"
            
            for i, flight in enumerate(flights[:3], 1):
                response += f"{i}. **{flight['airline']}** {flight['flight_number']}\n"
                response += f"   💰 ${flight['price']} | ⏱️ {flight['duration']}\n"
                response += f"   🕒 Depart: {flight['departure_time']} | Arrive: {flight['arrival_time']}\n\n"
            
            if seat_pref:
                response += f"ℹ️ I remembered you prefer {seat_pref} seats. I'll prioritize those when you're ready to book.\n"
            
            response += "Would you like to book any of these flights?"
            
            # Store search in working memory
            self.memory.working.set("last_search", {
                "type": "flight",
                "results": flights,
                "params": params
            })
            
            return response
            
        except Exception as e:
            return f"I'm having trouble searching flights right now. Please try again in a moment."
    
    async def _handle_hotel_search(self, message: str, user_id: str, intent: Dict) -> str:
        """
        Handle hotel search with preferences
        """
        params = intent.get('entities', {})
        city = params.get('destination') or params.get('city')
        check_in = params.get('check_in', 'next week')
        check_out = params.get('check_out')
        guests = params.get('guests', 2)
        
        if not check_out and check_in:
            # Assume 3 nights if not specified
            check_out = (datetime.strptime(check_in, "%Y-%m-%d") + timedelta(days=3)).strftime("%Y-%m-%d")
        
        # Get preferences
        preferences = await self.memory.long_term.recall_all_facts(user_id)
        star_pref = preferences.get('hotel_stars', {}).get('value')
        
        # Search hotels
        try:
            result = await self.registry.execute(
                "search_hotels",
                city=city or "your destination",
                check_in=check_in,
                check_out=check_out,
                guests=guests,
                stars=star_pref
            )
            
            hotels = result.get('hotels', [])
            if not hotels:
                return f"I couldn't find hotels in {city or 'that city'} for those dates."
            
            response = f"🏨 Here are some hotels in {city or 'your destination'}:\n\n"
            
            for i, hotel in enumerate(hotels[:3], 1):
                response += f"{i}. **{hotel['name']}** ⭐ {hotel['stars']} ({hotel['rating']}/5)\n"
                response += f"   💰 ${hotel['price_per_night']}/night | Total: ${hotel['total_price']}\n"
                response += f"   🛋️ Amenities: {', '.join(hotel['amenities'][:3])}\n\n"
            
            response += "Would you like to book any of these hotels?"
            
            self.memory.working.set("last_search", {
                "type": "hotel",
                "results": hotels,
                "params": params
            })
            
            return response
            
        except Exception as e:
            return f"I'm having trouble searching hotels. Please try again."
    
    async def _handle_booking(self, message: str, user_id: str, intent: Dict) -> str:
        """
        Handle booking confirmation
        """
        # Check if we have a pending search
        last_search = self.memory.working.get("last_search")
        
        if not last_search:
            return "I'm not sure what you want to book. Could you please search for flights or hotels first?"
        
        # Extract which option they want
        selection = intent.get('entities', {}).get('selection', 1)
        
        if last_search['type'] == 'flight':
            flights = last_search['results']
            if 1 <= selection <= len(flights):
                flight = flights[selection - 1]
                
                # Get user preferences
                preferences = await self.memory.long_term.recall_all_facts(user_id)
                
                # Book flight
                booking_result = await self.registry.execute(
                    "book_flight",
                    flight_id=flight['flight_number'],
                    passengers=last_search['params'].get('passengers', 1)
                )
                
                # Store booking in long-term memory
                await self.memory.long_term.store_conversation(user_id, {
                    "type": "flight_booking",
                    "details": flight,
                    "confirmation": booking_result
                })
                
                return f"✅ Flight booked successfully! Confirmation: {booking_result.get('booking_id', 'N/A')}\n\nA confirmation has been sent to your email. Would you like to book a hotel as well?"
        
        elif last_search['type'] == 'hotel':
            hotels = last_search['results']
            if 1 <= selection <= len(hotels):
                hotel = hotels[selection - 1]
                
                booking_result = await self.registry.execute(
                    "book_hotel",
                    hotel_name=hotel['name'],
                    check_in=last_search['params'].get('check_in'),
                    check_out=last_search['params'].get('check_out')
                )
                
                await self.memory.long_term.store_conversation(user_id, {
                    "type": "hotel_booking",
                    "details": hotel,
                    "confirmation": booking_result
                })
                
                return f"✅ Hotel booked successfully! Confirmation: {booking_result.get('confirmation_number', 'N/A')}\n\nIs there anything else I can help with?"
        
        return "I couldn't complete that booking. Please try again."
    
    async def _handle_weather(self, message: str, user_id: str, intent: Dict) -> str:
        """
        Handle weather inquiry
        """
        location = intent.get('entities', {}).get('location', 'your location')
        
        try:
            result = await self.registry.execute(
                "get_weather",
                location=location
            )
            
            if 'error' in result:
                return f"I couldn't get weather for {location}. Please check the location name."
            
            temp = result['temp']
            condition = result['condition']
            humidity = result['humidity']
            
            return f"☀️ Weather in {location.title()}:\nTemperature: {temp}°C\nCondition: {condition}\nHumidity: {humidity}%\n\nPerfect weather for travel! 🌍"
            
        except Exception as e:
            return f"I'm having trouble getting weather information right now."
    
    async def _handle_recommendation(self, message: str, user_id: str, intent: Dict) -> str:
        """
        Handle travel recommendations
        """
        preferences = await self.memory.long_term.recall_all_facts(user_id)
        
        # Build recommendation prompt
        prompt = f"""
User is asking for travel recommendations.

Their known preferences: {json.dumps(preferences, indent=2)}

Message: {message}

Provide personalized travel recommendations based on what you know about them.
If you don't have enough info, ask relevant questions.
"""
        
        response = await self.llm.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a knowledgeable travel advisor."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
    
    async def _handle_general(self, message: str, context: str) -> str:
        """
        Handle general conversation
        """
        response = await self.llm.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful travel assistant."},
                {"role": "user", "content": f"Context: {context}\n\nMessage: {message}"}
            ]
        )
        
        return response.choices[0].message.content
    
    async def get_conversation_history(self, user_id: str, days: int = 7) -> List[Dict]:
        """
        Get conversation history for a user
        """
        return await self.memory.long_term.get_recent_conversations(user_id, days)
    
    def get_stats(self) -> Dict:
        """
        Get agent statistics
        """
        return {
            "active_conversations": len(self.active_conversations),
            "tools_available": list(self.registry.tools.keys()),
            "short_term_memory_size": len(self.memory.short_term.messages),
            "semantic_memory_size": len(self.memory.semantic.memories)
        }

# FastAPI integration
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
agent = WhatsAppTravelAgent()

class WhatsAppRequest(BaseModel):
    user_id: str
    message: str
    session_id: Optional[str] = None

class WhatsAppResponse(BaseModel):
    response: str
    session_id: str

@app.post("/api/whatsapp/chat", response_model=WhatsAppResponse)
async def chat(request: WhatsAppRequest):
    """
    Chat endpoint for WhatsApp integration
    """
    try:
        # Generate session ID if not provided
        session_id = request.session_id or hashlib.md5(
            f"{request.user_id}:{datetime.now().date()}".encode()
        ).hexdigest()
        
        # Process message
        response = await agent.process_message(
            request.user_id,
            request.message,
            session_id
        )
        
        return WhatsAppResponse(
            response=response,
            session_id=session_id
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/whatsapp/history/{user_id}")
async def get_history(user_id: str, days: int = 7):
    """
    Get conversation history for a user
    """
    history = await agent.get_conversation_history(user_id, days)
    return {"user_id": user_id, "history": history}

@app.get("/api/whatsapp/stats")
async def get_stats():
    """
    Get agent statistics
    """
    return agent.get_stats()
```

## Example Conversation with the Complete Agent

```
User: "Hi, I'm planning a trip to Paris"

Agent: "Hello! I'm your travel assistant. I'd be happy to help you plan your trip to Paris! 

To get started, could you tell me:
1. When are you planning to travel?
2. Where will you be flying from?
3. How many people are traveling?

I'll remember your preferences to provide better recommendations."

---

User: "Next month from New York, 2 people"

Agent: "Great! Let me search for flights from New York to Paris next month for 2 people.

✈️ Here are some flight options:

1. **Air France** AF123
   💰 $550 | ⏱️ 7h 15m
   🕒 Depart: 09:30 | Arrive: 16:45

2. **Delta** DL456  
   💰 $620 | ⏱️ 7h 45m
   🕒 Depart: 11:15 | Arrive: 19:00

3. **United** UA789
   💰 $580 | ⏱️ 8h 30m (1 stop)
   🕒 Depart: 14:20 | Arrive: 22:50

Would you like to book any of these flights?"

---

User: "Book the Air France flight"

Agent: "✅ Flight booked successfully! Confirmation: AF-123456

A confirmation has been sent to your email. 

Would you like me to search for hotels in Paris as well?"

---

User: "Yes, please"

Agent: "🏨 Here are some hotels in Paris:

1. **Grand Hotel** ⭐⭐⭐⭐⭐ (4.5/5)
   💰 $200/night | Total for 5 nights: $1000
   🛋️ Amenities: pool, spa, restaurant

2. **City Central** ⭐⭐⭐⭐ (4.2/5)
   💰 $150/night | Total: $750
   🛋️ Amenities: restaurant, wifi, gym

3. **Budget Inn** ⭐⭐⭐ (3.5/5)
   💰 $80/night | Total: $400
   🛋️ Amenities: wifi

Which one would you like to book?"

---

User: "The Grand Hotel"

Agent: "✅ Hotel booked successfully! Confirmation: GH-789012

Your trip to Paris is all set!
- ✈️ Flight AF123, New York → Paris, next month
- 🏨 Grand Hotel, 5 nights

Total cost: $1,550

Is there anything else I can help with? Perhaps restaurant recommendations or activities in Paris?"

---

[Next day]

User: "I'm vegetarian, any restaurant recommendations?"

Agent: "I remember you're vegetarian! Based on your preference, here are some excellent vegetarian restaurants in Paris:

🥗 **Le Potager de Charlotte** - 100% vegan, amazing reviews
🥘 **Le Grenier de Notre-Dame** - Historic vegetarian restaurant
🍝 **Brutus** - Vegetarian Italian

Would you like me to make a reservation at any of these?"

---

User: "Book Le Potager for 2 next Friday at 8pm"

Agent: "✅ Reservation confirmed at Le Potager de Charlotte for 2 people next Friday at 8pm. Confirmation: RES-456789

Enjoy your meal! Is there anything else I can help with?"
```

---

## 🎯 Summary: What You've Learned in Part 2

✅ **Agent Core Architecture**
- The think-act-observe autonomous loop
- Planning vs reacting strategies
- LangChain and LangGraph frameworks
- Building stateful agents with proper loops

✅ **Tool & Function Calling**
- Designing robust JSON schemas
- Building reusable tools with proper error handling
- Tool registry for managing multiple tools
- Retry logic and circuit breakers for resilience
- Real tools: Weather, Flights, Hotels, Web Search

✅ **Memory Systems**
- Short-term memory for conversation context
- Long-term Redis-based persistent memory
- Semantic memory with embeddings for meaning-based recall
- Working memory for task state
- Complete memory system integration

✅ **Complete WhatsApp Travel Agent**
- Multi-step booking flows
- User preference tracking
- Context maintenance across days
- Personalized responses
- Error handling and resilience
- Production-ready FastAPI integration

---

## 👀 Preview: What's Coming in Part 3

In the next story, we'll take your agent to the next level with advanced capabilities:

**RAG Systems — Connecting to Knowledge Bases**
- Chunking strategies for large documents
- Vector databases (Pinecone, Weaviate, Milvus, Chroma, Qdrant)
- Semantic search and retrieval
- Building a customer support agent that knows your entire documentation

**Multi-Agent Systems — When One Agent Isn't Enough**
- Planner-executor pattern for complex task decomposition
- Supervisor agents for coordination and routing
- Debate agents for better decision making
- Swarm intelligence for parallel processing
- AutoGen, CrewAI, and LangGraph for multi-agent orchestration

**By the end of Part 3, you'll have a team of specialized agents working together to handle complex tasks that no single agent could manage alone.**

---

## 🚀 Your Mission for This Week

1. Add at least 3 tools to your agent (weather, flights, hotels, or your own)
2. Implement a memory system that remembers user preferences
3. Build a multi-step booking flow that spans multiple conversations
4. Test your agent with a complete scenario:
   - User asks about weather
   - Searches for flights
   - Selects and books a flight
   - Searches for hotels
   - Books a hotel
   - Comes back next day and agent remembers everything

---

**Coming up next in Part 3: Going Pro — RAG Systems and Multi-Agent Collaboration**

*Don't miss it! Follow me to get notified when the next story drops.*

---

*[End of Story 2 — 14,521 words]*

---

**[Click here for Story 3 →]** (Link to be added)

---
*� Questions? Drop a response - I read and reply to every comment.*
*📌 Save this story to your reading list - it helps other engineers discover it.*
**🔗 Follow me →**
- [**Medium**](mvineetsharma.medium.com) - mvineetsharma.medium.com
- [**LinkedIn**](www.linkedin.com/in/vineet-sharma-architect) -  www.linkedin.com/in/vineet-sharma-architect

*In-depth .NET, Node.js, Python, Cloud Architecture, and System Design. New articles weekly*