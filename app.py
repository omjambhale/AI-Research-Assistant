import gradio as gr
import asyncio
import os
from dotenv import load_dotenv
from research_manager import ResearchManager

# Load environment variables
load_dotenv(override=True)

# Check if OpenAI API key is available
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("⚠️  WARNING: OPENAI_API_KEY not found in environment variables!")
    print("   Please set your OpenAI API key using:")
    print("   export OPENAI_API_KEY=your_api_key_here")
    print("   or create a .env file with: OPENAI_API_KEY=your_api_key_here")

# Global variable to store the research manager instance
research_manager = ResearchManager()

async def generate_questions(query: str):
    """Generate clarifying questions for the user's query"""
    if not query.strip():
        return "Please enter a research query first."
    
    try:
        clarification_data = await research_manager.generate_clarifying_questions(query)
        questions_text = "\n\n".join([f"{i+1}. {question}" for i, question in enumerate(clarification_data.questions)])
        return f"**Clarifying Questions:**\n\n{questions_text}\n\nPlease answer these questions to help me provide a more targeted research report."
    except Exception as e:
        return f"Error generating questions: {str(e)}"

async def run_research(query: str, answer1: str, answer2: str, answer3: str):
    """Run the research process with clarifying answers"""
    if not query.strip():
        yield "Please enter a research query."
        return
    
    if not all([answer1.strip(), answer2.strip(), answer3.strip()]):
        yield "Please answer all three clarifying questions before proceeding with research."
        return
    
    clarifying_answers = [answer1.strip(), answer2.strip(), answer3.strip()]
    
    try:
        result_text = ""
        async for chunk in research_manager.run_with_clarification(query, clarifying_answers):
            result_text += chunk + "\n\n"
            yield result_text
    except Exception as e:
        yield f"Error during research: {str(e)}"

# Create the Gradio interface
with gr.Blocks(theme=gr.themes.Default(primary_hue="sky"), title="AI Research Assistant") as ui:
    gr.Markdown("# 🤖 AI Research Assistant with Clarifying Questions")
    gr.Markdown("This assistant will help you research any topic by first asking clarifying questions to provide more targeted results.")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## 📝 Step 1: Enter Your Query")
            query_textbox = gr.Textbox(
                label="What topic would you like to research?",
                placeholder="e.g., Latest AI Agent frameworks in 2025",
                lines=3
            )
            generate_questions_btn = gr.Button("Generate Clarifying Questions", variant="primary")
            
            gr.Markdown("## ❓ Step 2: Answer Clarifying Questions")
            questions_output = gr.Markdown(label="Clarifying Questions")
            
            answer1 = gr.Textbox(label="Answer to Question 1", lines=2)
            answer2 = gr.Textbox(label="Answer to Question 2", lines=2)
            answer3 = gr.Textbox(label="Answer to Question 3", lines=2)
            
            run_research_btn = gr.Button("Start Research", variant="primary")
        
        with gr.Column(scale=1):
            gr.Markdown("## 📊 Research Results")
            report_output = gr.Markdown(label="Research Report")
    
    # Event handlers
    generate_questions_btn.click(
        fn=generate_questions,
        inputs=query_textbox,
        outputs=questions_output
    )
    
    run_research_btn.click(
        fn=run_research,
        inputs=[query_textbox, answer1, answer2, answer3],
        outputs=report_output
    )
    
    # Allow Enter key to submit
    query_textbox.submit(
        fn=generate_questions,
        inputs=query_textbox,
        outputs=questions_output
    )

if __name__ == "__main__":
    ui.launch(inbrowser=True, share=False) 