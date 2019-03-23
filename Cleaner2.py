import csv

duplicates_file = input('enter duplicates.csv: ')
open_duplicates = open(duplicates_file)

row = []
prev_row = []
lines = []
names = []
count = 0

for line in open_duplicates:
    count = count + 1
    row = line.split(',')

    lines.append(row)

    if row[0] not in names:
        names.append(row[0])

    else:
        i = 0
        prev_row = lines[count-1]

        for word in row:
            if prev_row[i] == '':
                prev_row[i] = word
            i = i + 1
        print(prev_row)
