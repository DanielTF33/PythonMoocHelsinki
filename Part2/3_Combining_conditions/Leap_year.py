year = int(input("Please type in a year:"))

if year % 400 == 0:
    print(f"That year is a leap year.")
elif year % 100 == 0:
    print(f"That year is not a leap year.")
elif year % 4 == 0:
    print(f"That year is a leap year.")
else:
    print(f"That year is not a leap year.")