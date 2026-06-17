# #  question 1
# a = int(input("Enter a perpendicular: "))
# b = int(input("Enter a base: "))
# c = (a**2 + b**2)**0.5
# print(c)


# # question 2
# print('''
#       +--------+
#       |        |
#       |        |
#       |        |
#       |        |
#       +--------+
#                ''')


# # question 3 
# print("+"+"-" *10+ "+")
# print(("|"+"-" *10+ "|\n")*5, end = "")
# print("+"+"-"*10+"+")

# # question 4
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the secand number: "))
# number3 = int(input("Enter the third number: "))

# largest_number = number1

# if number2 > largest_number:
#       larger_number = number2
# if number3 > largest_number:
#       larger_number = number3

# largest_number = max(number1, number2, number3)
# lowest_number = min(number1, number2, number3)
# print("the largest number is", largest_number)
# print("the lowest number is", lowest_number)


# question 5
# name = input("write something here")

# if name == "Spathiphillum":
#     print("Yes, this one")
# elif name == "spathiphillum":
#     print("No, not correct")
# else: print("Spathiphillum or spathiphillum")

import pandas as pd

data = {
    'Name': ['Pankaj','Alia','Ram','Kajal','Aman'],
    'Age': [21,19,22,20,19],
    'Marks': [85,65,75,99,56],
    'City': ['Rom','Berlin','Tokyo','Moscow','London']
}

df = pd.DataFrame(data)
# print(df)

# print(df.shape)
# print(df.head(2))
# print(df.dtypes)
# print(df.describe)


# Select Columns
print("df['Name']: \n" , df['Name'])
print(df[['Name', 'Marks']])

# Filter Rows
print(df[df['Marks'] >= 85])
print(df[df['City'] == 'Bhopal'])
print(df[(df['Marks']>=88) & (df['City']=='Indore')])

def get_grade(x):
    if x >= 90:
        return 'A'
    elif x >= 75:
        return 'B'
    else:
        return 'C'

df['Grade'] = df['Marks'].apply(get_grade)
print(df['Grade'])
print("------------")
print(df)

City_avg = df.groupby('City')['Marks'].mean()
print(City_avg)

df2 = pd.read_csv('student.csv')
# Cleaning
df2.to_csv('clean_output.csv',index=False)