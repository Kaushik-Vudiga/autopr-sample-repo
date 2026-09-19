"""Authentication helpers for the AutoPR sample project."""


def validate_password(password: str) -> bool:
    """Validate that a password meets security requirements.

    Requirements:
    - At least 8 characters long.
    - Contains at least one uppercase letter.
    - Contains at least one digit.
    - Contains at least one special character (non-alphanumeric).

    Args:
        password: The password string to validate.

    Returns:
        bool: True if the password meets all criteria, False otherwise.
    """
    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    return has_upper and has_digit and has_special