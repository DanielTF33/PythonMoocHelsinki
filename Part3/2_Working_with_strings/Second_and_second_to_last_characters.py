string = input("Please type in a string: ")
p = string[1]
u = string[len(string)-2]

if  p == u:
    print(f"The second and the second to last characters are {p}")

if  p != u:
    print(f"The second and the second to last characters are different")