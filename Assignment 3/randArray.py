import random
n = int(input("Plz enter the length of the array: "))
rand_array = []
while len(rand_array) < n:
    rand_number = random.randint(0, 100)
    if rand_number not in rand_array:
        rand_array.append(rand_number)
print(rand_array)