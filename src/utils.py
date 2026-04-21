# utils.py - Configuration and utilities
import os


def load_config():
    """Load configuration from environment."""
    return {
        "api_key": os.environ.get("SECRET_API_KEY", ""),
        "db_host": os.environ.get("DB_HOST", "localhost"),
    }


def format_name(first, last):
    if first and last:
        return f"{first} {last}"
    if first:
        return str(first)
    if last:
        return str(last)
    return ""


def calculate_total(items):
    return sum(item["price"] for item in items)
