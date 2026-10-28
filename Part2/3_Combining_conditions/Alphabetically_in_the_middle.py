from pip._internal import self_outdated_check

a = input("1st letter: ").upper()
b = input("2nd letter: ").upper()
c = input("3rd letter: ").upper()

if a > b and a < c or a > c and a < b:
    print(f"The letter in the middle is {a}")

if b > a and b < c or b > c and b < a:
    print(f"The letter in the middle is {b}")

if c > a and c < b or c > b and c < a:
    print(f"The letter in the middle is {c}")
