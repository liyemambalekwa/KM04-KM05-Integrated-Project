
"""
security.py
------------
Task 6: Password hashing and access control for sales reports.

This module demonstrates the CIA triad:
- Confidentiality
- Integrity
- Availability

It also demonstrates password hashing and access control.

IMPORTANT:
Never store a password as plain text. Store its hash instead.
SHA-256 is used here for learning purposes.
"""

import hashlib
import getpass


def hash_password(plain_text_password: str) -> str:
    """Convert a plain-text password into a SHA-256 hash."""
    password_bytes = plain_text_password.encode("utf-8")
    password_hash = hashlib.sha256(password_bytes).hexdigest()
    return password_hash


# Store the password hash, not the plain-text password.
# Sample project password: Thabo2026!
STORED_PASSWORD_HASH = hash_password("Thabo2026!")


def check_password(attempt: str, stored_hash: str) -> bool:
    """Check whether the entered password matches the stored hash."""
    attempted_hash = hash_password(attempt)
    return attempted_hash == stored_hash


def login_gate(stored_hash: str, max_attempts: int = 3) -> bool:
    """
    Ask the user for a password and allow limited attempts.

    Returns True if the password is correct.
    Returns False if all attempts fail.
    """
    for attempt_number in range(max_attempts):
        attempt = getpass.getpass(
            "Enter password to view reports: "
        )

        if check_password(attempt, stored_hash):
            print("Access granted.")
            return True

        print("Incorrect password. Try again.")

    print("Access denied - too many failed attempts.")
    return False


# SECURITY REFLECTION
#
# Confidentiality:
# The login gate helps prevent unauthorised users from viewing
# the sales reports.
#
# Integrity:
# Primary keys help prevent duplicate record IDs, while foreign
# keys help ensure sales refer to existing products. NOT NULL
# constraints also prevent certain missing values.
#
# Availability:
# If the laptop is damaged or the database file is lost, the
# reports may become unavailable. Regular backups help protect
# the data.
