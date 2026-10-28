year = int(input("Year: "))
tu_year = year

while True:

    year +=1

    if year % 400 == 0:
        print(f"The next leap year after {tu_year} is {year}")
        break
    elif year % 100 == 0:
        print()
    elif year % 4 == 0:
        print(f"The next leap year after {tu_year} is {year}")
        break
