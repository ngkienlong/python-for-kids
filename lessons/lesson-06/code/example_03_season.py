# example_03_season.py
# Lesson 6: Determine the season from a month number
# Uses or to check multiple values in one condition.

month = int(input("Enter month number (1-12): "))

# Spring: March (3), April (4), May (5)
if month == 3 or month == 4 or month == 5:
    print("Spring")
# Summer: June (6), July (7), August (8)
elif month == 6 or month == 7 or month == 8:
    print("Summer")
# Autumn: September (9), October (10), November (11)
elif month == 9 or month == 10 or month == 11:
    print("Autumn")
# Winter: December (12), January (1), February (2)
else:
    print("Winter")
