# Additional tests for Lab 2

# These tests should be added by students to test_app.py:

def test_format_username_none_input():
    """Test that None input raises ValueError"""
    with pytest.raises(ValueError):
        format_username(None)

def test_format_username_empty_string():
    """Test that empty string raises ValueError"""
    with pytest.raises(ValueError):
        format_username("")

def test_format_username_no_period():
    """Test that email without period in name part raises ValueError"""
    with pytest.raises(ValueError):
        format_username("admin@example.com")

def test_format_username_no_at_symbol():
    """Test that email without @ symbol raises ValueError"""
    with pytest.raises(ValueError):
        format_username("jane.doe.example.com")

def test_format_username_multiple_periods():
    """Test that email with multiple periods works correctly"""
    result = format_username("mary.jane.watson@example.com")
    # Should handle only first.last format or raise error


# Hardened version of format_username (final version for Lab 2):

def format_username_hardened(email):
    """Takes jane.doe@example.com -> Doe, Jane
    Hardened version that handles edge cases properly"""
    if not email or not isinstance(email, str):
        raise ValueError("Invalid email format for username extraction")
    
    if '@' not in email:
        raise ValueError("Invalid email format for username extraction")
    
    name_part = email.split("@")[0]
    
    if '.' not in name_part:
        raise ValueError("Invalid email format for username extraction")
    
    parts = name_part.split(".")
    if len(parts) != 2:
        raise ValueError("Invalid email format for username extraction")
    
    first, last = parts
    if not first or not last:
        raise ValueError("Invalid email format for username extraction")
        
    return f"{last.capitalize()}, {first.capitalize()}"
