# AI-Assisted Debugging Workshop Lab

This project contains a "Buggy-Pedia" web application with intentional bugs to demonstrate AI-assisted debugging.

## Project Structure

```
├── app.py                 # Main Flask application file with bugs
├── requirements.txt       # Python dependencies
├── test_app.py           # Basic tests (to be extended)
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── calculate_severity.html
│   └── severity_result.html
├── static/              # CSS styles
│   └── style.css
└── .github/workflows/   # GitHub Actions for CI/CD
    └── security-scan.yml
```

## Known Bugs (for laboratory work)

### Lab 1: Runtime Error in calculate_severity()
- **Bug**: TypeError when multiplying string by string
- **Location**: `app.py:22` - `score = impact * urgency_multiplier`
- **Cause**: Form data comes as strings but is used in mathematical operations

### Lab 2: Issues in format_username()
- **Bugs**: Function crashes on edge cases
- **Location**: `app.py:26-30` 
- **Problems**:
  - Doesn't handle `None`
  - Doesn't handle empty strings
  - Doesn't handle email without dot in name (e.g., "admin@example.com")

### Lab 3: Security Issues
- **Bug**: Hardcoded secret key
- **Location**: `app.py:4` - `app.config['SECRET_KEY']`
- **Problem**: Secret key should not be in code

## Installation and Running

1. Create virtual environment:
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
flask run
```

4. Open browser: http://127.0.0.1:5000

## Testing

Run tests:
```bash
pytest
```

## Assignments

### Lab 1: Fixing Runtime Error
1. Reproduce the error on "Calculate Severity" page
2. Use AI assistant to explain the error
3. Apply the suggested fix

### Lab 2: Writing tests and hardening
1. Generate tests for `format_username()` function
2. Add tests for edge cases
3. Improve function to handle all cases

### Lab 3: CI/CD with AI checks
1. Create branch with security bug
2. Set up GitHub Action for automatic checks
3. Fix bug and ensure checks pass

## Expected Results

After completing all laboratory work:
- ✅ Application works without errors
- ✅ All tests pass (including edge cases)  
- ✅ No hardcoded secret data
- ✅ CI/CD pipeline automatically checks security
