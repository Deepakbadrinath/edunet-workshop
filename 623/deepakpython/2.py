month_days = {
    "January": 31,
    "February": 28,  
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

month = input("Enter the month name: ").capitalize() 
if month in month_days:
    days = month_days[month]
    print(f"{month} has {days} days.")
    if days > 30:
        print(f"{month} has greater than 30 days.")
    elif days < 30:
        print(f"{month} has less than 30 days.")
    else:
        print(f"{month} has exactly 30 days.")
else:
    print("Invalid month name. Please enter a valid month.")