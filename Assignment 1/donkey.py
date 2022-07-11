a = int(input("Plz enter first side of a traingle : "))
b = int(input("Plz enter second side of a traingle : "))
c = int(input("Plz enter third side of a traingle : "))

if a < b + c and b < a + c and c < a + b:
    print("We can draw a traingle with this numbers By 'Donkey Theory'.")
else:
    print("Error with Donkey Theory!!")