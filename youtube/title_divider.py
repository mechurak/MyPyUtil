import pandas as pd

df = pd.read_csv('output.csv')
print(df)


def real_number(raw_title):
    # print(raw_title)
    first_space_i = raw_title.find('.')
    if first_space_i == -1:
        first_space_i = raw_title.find(' ')
    number = raw_title[:first_space_i]
    if number[-1] == '.':
        number = number[:-1]
    try:
        int(number)
    except ValueError:
        print(f'Check!!! {number} | {raw_title}')
    return number
    # title = title[first_space_i + 1:].strip()


def real_title(raw_title):
    # print(raw_title)
    first_space_i = raw_title.find('.')
    if first_space_i == -1:
        first_space_i = raw_title.find(' ')
    title = raw_title[first_space_i + 1:].strip()
    return title


df['Number'] = df['Title'].map(real_number)
df['RealTitle'] = df['Title'].map(real_title)

df.to_csv('output2.csv', header=True, index=False)
print('to_csv(). Done')
