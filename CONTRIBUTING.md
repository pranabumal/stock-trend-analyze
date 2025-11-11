# Contributing to Stock Price vs Search Trends Analyzer

Thank you for your interest in contributing to this project! We welcome contributions from everyone. Please follow these guidelines to ensure a smooth contribution process.

## How to Contribute

### 1. **Fork the Repository**
- Click the "Fork" button on the GitHub repository
- This creates your own copy of the project

### 2. **Clone Your Fork**
```bash
git clone https://github.com/YOUR_USERNAME/stock-trend-analyze.git
cd stock-trend-analyze
```

### 3. **Create a Branch**
Create a new branch for your feature or bug fix:
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Use descriptive branch names like:
- `feature/add-portfolio-analysis`
- `fix/google-trends-rate-limit`
- `docs/improve-readme`

### 4. **Set Up Development Environment**
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (optional)
pip install pytest black flake8
```

### 5. **Make Your Changes**
- Make your code changes
- Keep changes focused and related to one issue/feature
- Write clear, descriptive commit messages
- Follow PEP 8 style guidelines

### 6. **Test Your Changes**
```bash
# Test the app locally
streamlit run streamlit_app.py

# Run any existing tests (if available)
pytest
```

### 7. **Commit Your Changes**
```bash
git add .
git commit -m "Brief description of changes"

# Example commits:
# "Add correlation strength visualization"
# "Fix pytrends rate limiting issue"
# "Update README with installation steps"
```

### 8. **Push to Your Fork**
```bash
git push origin feature/your-feature-name
```

### 9. **Create a Pull Request (PR)**
- Go to the original repository on GitHub
- Click "New Pull Request"
- Select your branch
- Fill in the PR template with:
  - **Title**: Clear, concise description
  - **Description**: What changes you made and why
  - **Related Issues**: Link any related issues (#123)
  - **Type**: Bug Fix / Feature / Documentation / Enhancement

### 10. **Code Review**
- Respond to feedback from maintainers
- Make requested changes by pushing new commits
- Be respectful and open to suggestions

---

## Types of Contributions We Welcome

### 🐛 Bug Reports
- Create an issue describing the bug
- Include steps to reproduce
- Share error messages and screenshots
- Specify your environment (OS, Python version, etc.)

### ✨ Feature Requests
- Suggest new features via GitHub issues
- Explain the use case and expected behavior
- Discuss implementation ideas

### 📝 Documentation
- Improve README or code comments
- Add usage examples
- Create tutorials or guides
- Fix typos and unclear explanations

### 🎯 Code Improvements
- Optimize performance
- Refactor for clarity and maintainability
- Add type hints
- Improve error handling

### 🧪 Testing
- Write unit tests
- Add integration tests
- Improve test coverage

### 🎨 UI/UX Enhancements
- Improve Streamlit UI
- Better visualizations
- Improved user experience

---

## Development Guidelines

### Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints where possible
- Write descriptive variable names
- Add docstrings to functions and classes

### Example Code Style:
```python
def calculate_correlation(price_series: pd.Series, trend_series: pd.Series) -> float:
    """
    Calculate Pearson correlation between price and trend series.
    
    Args:
        price_series: Stock price data
        trend_series: Search trend data
        
    Returns:
        Correlation coefficient (-1 to 1)
    """
    return price_series.corr(trend_series)
```

### Git Commit Messages
- Use the imperative mood ("Add feature" not "Added feature")
- First line should be max 50 characters
- Include a blank line and detailed description if needed
- Reference issues when relevant (#123)

Example:
```
Add correlation strength classification

- Classify correlations as Very Weak, Weak, Moderate, Strong
- Add color coding for visual clarity
- Update visualization to show strength badges
- Fixes #45
```

### Architecture
- Follow the existing **Ports & Adapters** pattern
- Keep separation of concerns (UI, Services, Infrastructure)
- Add interfaces for new data sources
- Make infrastructure pluggable

---

## Pull Request Guidelines

### Before Submitting a PR:
- ✅ Ensure your branch is up to date with `main`
- ✅ Test your code thoroughly
- ✅ Update documentation if needed
- ✅ Follow code style guidelines
- ✅ Keep PR focused on one feature/fix
- ✅ Write a clear PR description

### PR Title Format:
```
[TYPE] Brief description

Types:
- [FEATURE] New functionality
- [FIX] Bug fix
- [DOCS] Documentation
- [REFACTOR] Code refactoring
- [TEST] Test additions
```

### PR Description Template:
```markdown
## Description
Brief description of changes

## Related Issues
Closes #123

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
Describe how this was tested

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-reviewed changes
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated
```

---

## Issues and Discussions

### Reporting Issues
- Search existing issues first
- Use clear, descriptive titles
- Provide as much detail as possible
- Include error messages and logs
- Specify environment details

### Issue Labels
- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements needed
- `good first issue` - Good for new contributors
- `help wanted` - Extra attention needed

---

## Recognition

Contributors will be recognized in:
- Pull request acknowledgments
- Project CONTRIBUTORS.md file
- GitHub contributor statistics
- Project releases (if applicable)

---

## Code of Conduct

### Be Respectful
- Treat all contributors with respect
- Use welcoming and inclusive language
- Be patient with different skill levels

### Be Constructive
- Provide helpful feedback
- Explain your reasoning
- Suggest improvements, not just criticism

### Be Collaborative
- Work together toward solutions
- Ask questions politely
- Share knowledge and experience

### Unacceptable Behavior
- Harassment or discrimination
- Offensive language or behavior
- Disrespect or dismissiveness
- Trolling or spam

---

## Questions or Need Help?

- 💬 Open a GitHub Discussion
- 📧 Contact the maintainers
- 📖 Check existing documentation
- 🔍 Search closed issues for answers

---

## Additional Resources

- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [How to Write Good Commit Messages](https://chris.beams.io/posts/git-commit/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Project Design Document](docs/design.md)

---

## Thank You! 🎉

Your contributions help make this project better for everyone. We appreciate your time and effort!

Happy contributing! 🚀
