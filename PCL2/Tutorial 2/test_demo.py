# test_calculator.py
"""Tests for the calculator module using pytest.
Includes both passing and intentionally failing tests for demonstration."""

import pytest
from demo import add, subtract, multiply, divide

# Passing tests
def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(2, 8) == -6

def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 4) == -8
    assert multiply(0, 5) == 0

def test_divide():
    """Test the divide function."""
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    """Test that dividing by zero raises an error."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

# Intentionally failing tests for demonstration purposes
def test_add_failure():
    """Demonstrates a failing equality test."""
    # This will fail because 1 + 2 is 3, not 4
    assert add(1, 2) == 4, "This should fail to show how assertion errors look"

def test_subtract_failure():
    """Demonstrates a failing test with a message."""
    result = subtract(10, 5)
    # This will fail because 10 - 5 is 5, not 6
    assert result == 6, f"Expected 6 but got {result}"

def test_expected_exception_failure():
    """Demonstrates a test that expects an exception that isn't raised."""
    # This will fail because dividing 10 by 2 doesn't raise a ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        divide(10, 2)

def test_unexpected_exception_failure():
    """Demonstrates a test where an unexpected exception occurs."""
    # This will fail because we're trying to multiply with non-numbers
    assert multiply("string", 5) == 0