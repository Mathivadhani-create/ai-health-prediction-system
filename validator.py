import re
from datetime import datetime


def validate_email(email):
    """Validate email format."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))


def validate_dob(dob):
    """Ensure DOB is not a future date."""
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        return dob_date <= datetime.today()
    except ValueError:
        return False


def validate_numeric(value):
    """Check if value is numeric."""
    try:
        float(value)
        return True
    except ValueError:
        return False