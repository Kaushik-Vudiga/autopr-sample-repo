"""Authentication helpers for the AutoPR sample project."""


def validate_password(password: str) -> bool:
    """Return True when a password meets the minimum character length requirement."""
    if not isinstance(password, str):
        return False
    return len(password) >= 8