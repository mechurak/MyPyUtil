import csv

INPUT_FILE = "50+50 English - 시트1.csv"
OUT_FILE_PRE_FIX = "50_English"

f_out_left = open(OUT_FILE_PRE_FIX+"_left.txt", 'w', encoding='utf-8')
f_out_right = open(OUT_FILE_PRE_FIX+"_right.txt", 'w', encoding='utf-8')


I_TITLE = 0
I_INDEX = 1
I_MEANING = 2
I_SPELLING = 3
I_DESCRIPTION = 4
I_HINT = 5
I_PHONETIC = 6
I_USAGE = 7

f = open(INPUT_FILE, 'r', encoding='utf-8')
csv_reader = csv.reader(f)
for index, row in enumerate(csv_reader):
    if index == 0:
        continue
    print(index, row[0], row)
    f_out_left.write(row[I_TITLE] + ' - ' + row[I_HINT] + '\n')
    f_out_right.write(row[I_TITLE] + ' - ' + row[I_HINT] + '\n')
    f_out_left.write(row[I_SPELLING] + '\n')
    f_out_right.write('\n')
    f_out_left.write('- - -\n\n')
    f_out_right.write('- - -\n\n')

f.close()

