from src.auth import validate_password


def test_accepts_password_with_eight_characters():
    assert validate_password("password") is True


def test_rejects_short_password():
    assert validate_password("short") is False
