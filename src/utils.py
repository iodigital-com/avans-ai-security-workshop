# utils.py - Configuration and utilities
import os
from dotenv import load_dotenv

# Load .env file environment variables
load_dotenv()

def load_config():
    """Load configuration from environment."""
    return {
        "api_key": os.environ.get("SECRET_API_KEY", ""),
        "db_host": os.environ.get("DB_HOST", "localhost"),
    }


def format_name(first, last):
    # Convert None to empty string
    if first is None:
        first = ""
    if last is None:
        last = ""

    # Convert to string explicitly
    first = str(first)
    last = str(last)

    if first and last:
        return f"{first} {last}"
    if first:
        return first
    if last:
        return last
    return ""


def calculate_total(items):
    return sum(item["price"] for item in items)


# Temporary test
if __name__ == '__main__':
    print(format_name(None, "Smith"))  # Expected: Smith
    print(format_name("John", None))   # Expected: John
    print(format_name(None, None))      # Expected: (empty string)
