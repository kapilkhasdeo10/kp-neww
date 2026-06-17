# import pandas as pd

# data = {
#     'Name': ['Pankaj','Alia','Ram','Kajal','Aman'],
#     'Age': [21,19,22,20,19],
#     'Marks': [85,65,75,99,56],
#     'City': ['Rom','Berlin','Tokyo','Moscow','London']
# }

# df = pd.DataFrame(data)
# # print(df)

# # print(df.shape)
# # print(df.head(2))
# # print(df.dtypes)
# # print(df.describe)


# # Select Columns
# print("df['Name']: \n" , df['Name'])
# print(df[['Name', 'Marks']])

# # Filter Rows
# print(df[df['Marks'] >= 85])
# print(df[df['City'] == 'Bhopal'])
# print(df[(df['Marks']>=88) & (df['City']=='Indore')])

# def get_grade(x):
#     if x >= 90:
#         return 'A'
#     elif x >= 75:
#         return 'B'
#     else:
#         return 'C'

# df['Grade'] = df['Marks'].apply(get_grade)
# print(df['Grade'])
# print("------------")
# print(df)

# City_avg = df.groupby('City')['Marks'].mean()
# print(City_avg)

# df.to_csv("students.csv",index=False)
# df2 = pd.read_csv("students.csv")
# # Cleaning
# df2.to_csv("clean_output.csv",index=False)
