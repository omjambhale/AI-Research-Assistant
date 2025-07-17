# Contributing to AI Research Assistant

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Bugs
- Use the GitHub issue tracker
- Include a clear description of the bug
- Provide steps to reproduce the issue
- Include your Python version and operating system

### Suggesting Enhancements
- Use the GitHub issue tracker
- Describe the enhancement clearly
- Explain why this enhancement would be useful

### Code Contributions
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes thoroughly
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/ai-research-assistant.git
   cd ai-research-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   ```bash
   cp env.example .env
   # Edit .env with your API keys
   ```

4. Test your changes:
   ```bash
   python3 app.py
   ```

## Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused

## Testing

Before submitting a pull request:
- Test the application locally
- Ensure all existing functionality still works
- Test with different types of queries

## Security

- Never commit API keys or sensitive information
- Follow security best practices
- Report security vulnerabilities privately

Thank you for contributing! 🚀 