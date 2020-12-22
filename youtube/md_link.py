import pandas as pd

df = pd.read_csv('raw_input.csv')
# print(df)

id_str = '75, 83, 112'
id_str.replace(' ', '')
id_list = id_str.split(',')

filtered_df = df[df['Number'].isin(id_list)]
# print(filtered_df)

for i in filtered_df.index:
    print(f"- {filtered_df['md_link'][i]}")

