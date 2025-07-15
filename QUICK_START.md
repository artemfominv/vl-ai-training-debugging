# Quick Start Guide

## Setup

1. **Clone and navigate to project**:
   ```bash
   git clone <repository-url>
   cd vl-ai-training-debugging
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run application**:
   ```bash
   flask run
   ```

5. **Open browser**: http://127.0.0.1:5000

## Testing the Bugs

### Lab 1: Runtime Error
1. Navigate to "Calculate Severity"
2. Enter Impact: 10, Urgency: high
3. Click "Calculate" → Should see Internal Server Error

### Lab 2: Edge Cases
Test these in Python console:
```python
from app import format_username
format_username(None)  # Should crash
format_username("")    # Should crash
format_username("admin@example.com")  # Should crash
```

### Lab 3: Security
The hardcoded secret key will be detected by TruffleHog in CI/CD.

## Running Tests
```bash
pytest -v
```

## Expected Workflow
1. Use AI assistant to identify and fix bugs
2. Write comprehensive tests for edge cases
3. Harden functions to handle all scenarios
4. Set up automated security scanning
