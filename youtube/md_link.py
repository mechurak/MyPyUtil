import pandas as pd

# TODO: Check 251, 262, 384

df = pd.read_csv('temp.csv')
# df = pd.read_csv('output2.csv')
# print(df)
# df.info()

number_str = '658, 660, 664, 666, 668, 670, 673, 675, 677, 679, 681, 683, 685, 687, 690, 692, 695, 697, 701, 702, 706, 712'
number_str = number_str.replace(' ', '')
number_list = number_str.split(',')
number_list = [int(i) for i in number_list]

filtered_df = df[df['Number'].isin(number_list)]
# print(filtered_df)

for number in number_list:
    mask = filtered_df['Number'] == number
    temp = filtered_df[mask]
    print(f"    - [{temp['Number'].values[0]}. {temp['Name'].values[0]}]({temp['Link'].values[0]})")
