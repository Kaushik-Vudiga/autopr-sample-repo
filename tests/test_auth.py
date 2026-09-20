from src.auth import validate_password


def test_accepts_valid_password():
    assert validate_password("Password1!") is True


def test_accepts_valid_long_password():
    assert validate_password("SuperSecureP@ssw0rd!") is True


def test_rejects_short_password():
    assert validate_password("P@ss1") is False


def test_rejects_seven_character_password():
    assert validate_password("P@sswo1") is False


def test_rejects_missing_uppercase():
    assert validate_password("password1!") is False


def test_rejects_missing_digit():
    # Example: Password! fails because it has no number
    assert validate_password("Password!") is False


def test_rejects_missing_special_character():
    # Example: Password1 fails because it has no special character
    assert validate_password("Password1") is False


def test_rejects_empty_password():
    assert validate_password("") is False


def test_rejects_only_digits():
    assert validate_password("12345678") is False


def test_rejects_only_special_characters():
    assert validate_password("!@#$%^&*") is False