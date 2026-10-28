PIN = 4321
contador = 1

while True:

    pin_respu = int(input("PIN: "))

    if  pin_respu == PIN and contador == 1:
        print("Correct! It only took you one single attempt!")
        break

    elif pin_respu == PIN:
        print(f"Correct! It took you {contador} attempts")
        break

    else:
        print("WRONG")
        contador += 1