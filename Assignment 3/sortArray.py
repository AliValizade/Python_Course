n = int(input("Plz enter the length of the array: "))
user_array = []
for i in range(n):
    user_array.append(int(input("Plz enter a number: ")))
print(user_array)
temp = 0
for i in range(n):
    for j in range(n-1):
        if user_array[j] > user_array[j+1]:
            temp = user_array[j]
            user_array[j] = user_array[j+1]
            user_array[j+1] = temp
print("Sorted array = ", user_array)
