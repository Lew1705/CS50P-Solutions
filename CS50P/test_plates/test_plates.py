from plates import is_valid

def test_length():
    # Too short
    assert is_valid("A") is False
    # Too long (7 chars)
    assert is_valid("ABCDEFG") is False
    # Valid lengths
    assert is_valid("AA") is True
    assert is_valid("ABCDEF") is True


def test_start_with_two_letters():
    # Must start with two letters
    assert is_valid("1A") is False
    assert is_valid("A1") is False
    assert is_valid("AB") is True
    assert is_valid("AB123") is True


def test_numbers_at_end_only():
    # Numbers at the end are okay
    assert is_valid("AB123") is True
    assert is_valid("ABC12") is True
    # Numbers cannot be in the middle
    assert is_valid("A1B2") is False
    assert is_valid("ABC2D") is False
    assert is_valid("AA22A") is False


def test_first_number_not_zero():
    # First number cannot be 0
    assert is_valid("AB0") is False
    assert is_valid("AB012") is False
    # First digit non-zero is fine
    assert is_valid("AB1") is True
    assert is_valid("CS50") is True


def test_only_alphanumeric():
    # No punctuation, spaces, etc.
    assert is_valid("AB-12") is False
    assert is_valid("AB 12") is False
    assert is_valid("CS.50") is False
    # Pure alphanumeric is fine
    assert is_valid("HELLO") is True
