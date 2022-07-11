score1 = float(input("Plz enter first score of student: "))
score2 = float(input("Plz enter second score of student: "))
score3 = float(input("Plz enter third score of student: "))
average = (score1 + score2 + score3) / 3
if average >= 17:
    result = "Great."
elif average < 12:
    result = "Fail."
else:
    result = "Normal."

print("Average of student is: ", result)