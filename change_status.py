def change_status(days_left):
     if days_left > 5:
         return "Active"
     elif 1 <= days_left <= 5:
         return "Expiring Soon"
     return "Expired"