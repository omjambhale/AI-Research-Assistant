# AI Research Assistant with Clarifying Questions

This project is an enhanced version of the deep research system that includes clarifying questions to provide more targeted and relevant research results. It's built as a Gradio web application that guides users through a two-step process.

## Features

- **Clarifying Questions**: The system generates 3 specific questions to better understand your research needs
- **Targeted Research**: Uses your answers to create more focused and relevant searches
- **Comprehensive Reports**: Generates detailed research reports based on web searches
- **User-Friendly Interface**: Clean Gradio web interface for easy interaction

## Project Structure

```
2_project/main/
├── app.py                 # Main Gradio application
├── research_manager.py    # Orchestrates the research process
├── clarifier_agent.py     # Generates clarifying questions
├── planner_agent.py       # Plans searches based on clarifications
├── search_agent.py        # Performs web searches
├── writer_agent.py        # Generates final reports
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## How It Works

1. **Query Input**: User enters their research topic
2. **Clarifying Questions**: System generates 3 specific questions to understand context, time period, focus areas, etc.
3. **User Answers**: User provides answers to the clarifying questions
4. **Targeted Research**: System uses answers to plan and execute focused web searches
5. **Report Generation**: Comprehensive report is generated incorporating all context

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ (recommended: Python 3.10+)
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-research-assistant.git
   cd ai-research-assistant
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   
   **Option A: Using .env file (recommended)**
   ```bash
   cp env.example .env
   # Edit .env and add your OpenAI API key
   ```
   
   **Option B: Using environment variable**
   ```bash
   export OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**:
   ```bash
   python3 app.py
   ```

5. **Access the interface**:
   Open your browser and go to `http://localhost:7860`

### ⚠️ Important Security Notes
- **Never commit your `.env` file** to version control
- **Never share your API keys** publicly
- The `.gitignore` file is configured to prevent accidental commits of sensitive files

## Usage

1. **Enter Your Query**: Type your research topic in the text box
2. **Generate Questions**: Click "Generate Clarifying Questions" to get 3 specific questions
3. **Answer Questions**: Provide detailed answers to help focus the research
4. **Start Research**: Click "Start Research" to begin the research process
5. **View Results**: The comprehensive report will appear in the right panel

## Key Improvements Over Original

- **Removed Email Functionality**: No more SendGrid dependencies or email sending
- **Added Clarifying Questions**: Better understanding of user needs
- **Enhanced Search Planning**: More targeted searches based on user context
- **Gradio Interface**: User-friendly web interface
- **Streaming Updates**: Real-time progress updates during research

## Example Workflow

1. Query: "Latest AI Agent frameworks in 2025"
2. Clarifying Questions:
   - What specific aspects of AI agent frameworks are you most interested in? (e.g., performance, ease of use, specific use cases)
   - Are you looking for frameworks for a particular industry or application domain?
   - Do you need information about commercial frameworks, open-source options, or both?
3. User provides detailed answers
4. System performs targeted searches
5. Comprehensive report is generated

## Dependencies

- `gradio`: Web interface
- `openai`: AI model access
- `python-dotenv`: Environment variable management
- `pydantic`: Data validation
- `asyncio`: Asynchronous programming
- Other standard Python libraries

## Notes

- The system uses OpenAI's GPT-4o-mini model for all AI operations
- Web searches are performed using the WebSearchTool
- All operations are traced and can be viewed at https://platform.openai.com/traces
- The interface is responsive and works on both desktop and mobile devices 