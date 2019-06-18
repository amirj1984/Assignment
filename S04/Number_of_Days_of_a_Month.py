# this program reads a month's name and shows its number of days
month_name = input("please eneter a name of a month: ")
thirty_one_days = ["January", "March", "May", "July", "August", "October", "December"]
thirty_days = ["April", "June", "September", "November"]

if month_name in thirty_one_days:
    print("this month has 31 days")
elif month_name in thirty_days:
    print("this month has 30 days")
elif month_name == "February":
    print("this month has 28 days in common years and 29 days in leap years")
