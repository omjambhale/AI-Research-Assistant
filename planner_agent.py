from pydantic import BaseModel, Field
from agents import Agent

HOW_MANY_SEARCHES = 3

INSTRUCTIONS = f"""You are a helpful research assistant. Given a query and the user's answers to clarifying questions, 
come up with a set of web searches to perform to best answer the query. The clarifying answers should help you 
create more targeted and relevant searches. Output {HOW_MANY_SEARCHES} terms to query for.

Use the clarifying answers to:
- Focus on specific time periods mentioned
- Target particular aspects or angles the user is interested in
- Consider the context and audience they specified
- Include specific examples or use cases they mentioned"""

class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")

planner_agent = Agent(
    name="PlannerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan,
) 