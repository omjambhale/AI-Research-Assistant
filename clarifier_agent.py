from pydantic import BaseModel, Field
from agents import Agent

INSTRUCTIONS = """You are a helpful research assistant. Given a user's query, you need to generate exactly 3 clarifying questions 
that will help you better understand what they're looking for. These questions should be specific, relevant, and help narrow down 
the scope of the research. Focus on aspects like:
- Time period (current, historical, future trends)
- Specific aspects or angles they want to explore
- Target audience or context
- Depth of information needed
- Specific examples or use cases they're interested in

Make sure the questions are clear, concise, and will genuinely help improve the research quality."""

class ClarificationData(BaseModel):
    questions: list[str] = Field(description="A list of exactly 3 clarifying questions to ask the user.")

clarifier_agent = Agent(
    name="ClarifierAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=ClarificationData,
) 