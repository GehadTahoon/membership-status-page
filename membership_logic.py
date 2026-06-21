def calculate_membership_status(days_left):
    """
    Calculates the status based on remaining days.
    """
    if days_left > 5:
        return "Active"
    elif 1 <= days_left <= 5:
        return "Expiring Soon"
    return "Expired"
