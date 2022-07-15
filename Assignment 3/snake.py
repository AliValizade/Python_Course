n = int(input("Plz enter the length of the snake: "))
while n > 0:
    if n % 2 == 0:
        print("#", end="")
    else:
        print("&", end="")
    n -= 1
