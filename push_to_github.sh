#!/bin/bash

echo "🚀 Pushing AI Research Assistant to GitHub..."
echo "Repository: https://github.com/omjambhale/ai-research-assistant"

# Check if remote exists
if git remote get-url origin > /dev/null 2>&1; then
    echo "✅ Remote origin already configured"
else
    echo "🔧 Adding remote origin..."
    git remote add origin https://github.com/omjambhale/ai-research-assistant.git
fi

# Push to GitHub
echo "📤 Pushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo "✅ Successfully pushed to GitHub!"
    echo "🌐 Your repository is now live at: https://github.com/omjambhale/ai-research-assistant"
    echo ""
    echo "📋 Next steps:"
    echo "1. Visit your repository on GitHub"
    echo "2. Add a description and topics"
    echo "3. Share with others!"
else
    echo "❌ Failed to push. Make sure:"
    echo "   - Repository exists on GitHub"
    echo "   - You have proper permissions"
    echo "   - You're authenticated with GitHub"
fi 