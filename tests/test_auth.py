from src.auth import validate_password


def test_accepts_password_with_eight_characters():
    assert validate_password("password") is True


def test_accepts_password_longer_than_eight_characters():
    assert validate_password("a_very_long_password_123") is True


def test_accepts_password_with_special_characters_and_numbers():
    assert validate_password("P@ssw0rd!") is True


def test_rejects_short_password():
    assert validate_password("short") is False


def test_rejects_seven_character_password():
    assert validate_password("1234567") is False


def test_rejects_empty_password():
    assert validate_password("") is False