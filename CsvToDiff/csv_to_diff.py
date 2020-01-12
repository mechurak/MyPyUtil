import csv

INPUT_FILE = "50+50 English - 시트1.csv"
OUT_FILE_PRE_FIX = "50_English"

f_out_left = open(OUT_FILE_PRE_FIX+"_left.txt", 'w', encoding='utf-8')
f_out_right = open(OUT_FILE_PRE_FIX+"_right.txt", 'w', encoding='utf-8')


I_INDEX = 0
I_TITLE = 1
I_MEANING = 2
I_SPELLING = 3
I_DESCRIPTION = 4
I_PHONETIC = 5
I_USAGE = 6

f = open(INPUT_FILE, 'r', encoding='utf-8')
csv_reader = csv.reader(f)
for index, row in enumerate(csv_reader):
    if index == 0:
        continue
    print(index, row[0], row)
    f_out_left.write(row[I_INDEX] + '. ' + row[I_MEANING] + '\n')
    f_out_right.write(row[I_INDEX] + '. ' + row[I_MEANING] + '\n')
    f_out_left.write(row[I_SPELLING] + '\n')
    f_out_right.write('\n')
    f_out_left.write(row[I_DESCRIPTION] + '\n\n\n')
    f_out_right.write(row[I_DESCRIPTION] + '\n\n\n')

f.close()

