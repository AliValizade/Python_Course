nums = int(input("Plz enter number of students: "))
scores = []
sum = 0
for i in range(nums):
    scores.append(float(input("Plz enter a score: ")))
    sum += scores[i]
print(scores) 
print("average =", sum / nums)
print("Max score is: ", max(scores))
print("Min score is: ", min(scores))