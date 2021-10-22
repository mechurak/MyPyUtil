import pandas as pd

# TODO: Check 251, 262, 384

df = pd.read_csv('output2.csv')
# print(df)

number_str = '413, 430, 459, 463, 593'
number_str = number_str.replace(' ', '')
number_list = number_str.split(',')

filtered_df = df[df['Number'].isin(number_list)]
# print(filtered_df)

for number in number_list:
    mask = filtered_df['Number'] == number
    print(f"- {filtered_df[mask]['MarkdownLink'].values[0]}")
