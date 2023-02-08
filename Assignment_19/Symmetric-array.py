n = int(input('Please enter the number of array elements: '))
array = [int(input('Enter array elements: ')) for i in range(n)]
print(array)
count = 0
for i in range(n//2):
    if array[i] != array[n-1-i]:
        print('The array is not symmetric. ❌')
        break
    else:
        count +=1
if count == n//2:
    print('The array is symmetric. ✅')