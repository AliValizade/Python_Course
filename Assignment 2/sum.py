sum = 0
while True:
    x = input("Plz enter a number: ")
    if x == "exit":
        break
    sum += int(x)
print("sum =", sum)