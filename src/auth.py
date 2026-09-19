"""Authentication helpers for the AutoPR sample project."""


def validate_password(password: str) -> bool:
    """Return True when a password meets the current basic requirement.

    Current behavior intentionally only checks minimum length.
    The AutoPR work item will require stronger validation.
    """
    return len(password) >= 8
