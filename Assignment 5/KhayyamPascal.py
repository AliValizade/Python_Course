n = int(input('Plz enter the row number of the Khayyam-Pascal triangle: '))
khayyam_Pascal_traingle = [[1]] # Khayyam-Pascal Traingle starts with a row of a single number 1.

for i in range(n):
    base_row = [0] # Extend row with leading and ending zeroes.
    base_row.extend(khayyam_Pascal_traingle[-1])
    base_row.append(0)
    row = [base_row[j] + base_row[j+1] for j in range(len(base_row)-1)]
    khayyam_Pascal_traingle.append(row)

for row in khayyam_Pascal_traingle:
    row_text = ''
    for i in range(len(row)):
        row_text += str(row[i])
        if i < len(row) - 1:
            row_text += ' '
    print(row_text)
