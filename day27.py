# Day 27 - Python Date and Time

from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()

print("Current Date:", now.strftime("%d-%m-%Y"))
print("Current Time:", now.strftime("%H:%M:%S"))

# Calculate tomorrow's date
tomorrow = now + timedelta(days=1)

print("Tomorrow's Date:", tomorrow.strftime("%d-%m-%Y"))

# Display the current year
print("Current Year:", now.year)