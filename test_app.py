import pytest
from app import format_username

def test_format_username_valid_email():
    """Test the happy path - valid email with firstname.lastname format"""
    result = format_username("jane.doe@example.com")
    assert result == "Doe, Jane"

def test_format_username_another_valid_email():
    """Test another valid email"""
    result = format_username("john.smith@company.org")
    assert result == "Smith, John"

# TODO: Add tests for edge cases:
# - None input
# - Empty string input  
# - Email without period in name part (e.g., "admin@example.com")
# These should raise ValueError exceptions
