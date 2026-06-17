# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("Division failed")
#         return None
#     else:
#         print("Everything went fine")
#         return n
    
# print("-----------")
# print("reciprocal(2):", reciprocal(2))
# print("-----------")
# print("reciprocal(0):" , reciprocal(0))


# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("Division failed")
#         n = None
#     else:
#         print("Everything went fine")
#     finally:
#         print("It's time to say goodbye")
#     return n

# print(reciprocal(2))
# print(reciprocal(0))


# try:
#     i = int("Hello!")
# except Exception as e:
#     print(e)
#     print(e.__str__())


# class MyZeroDivisionError(ZeroDivisionError):    
#     pass
# def do_the_division(mine):
#     if mine:
#         raise MyZeroDivisionError("some worse news")
#     else:        
#         raise ZeroDivisionError("some bad news")
    
# do_the_division(False)

# with open('students.txt', 'w') as f:
#     f.write('Kapil,88,Indore\n')
#     f.write('lava,98,Indore\n')
#     f.write('yash,81,Indore\n')
    
# with open('studentd.txt', 'a') as f:
#     f.write('snaha,89,Indore\n') 

# import csv
# records = [
#     ['name','marks','city','grade'],
#     ['rahul',85,'indore','B'],
#     ['priya',87,'bhopal','A'],
#     ['amit',68,'gwalior','C'],
# ]
# with open('students.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)

# import csv

# with open('students.csv', 'r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row["name"]}: {row["marks"]} marks ({row["city"]}) ')   


# import csv
# studentrecords =  [
#     ["name","age","sub_marks1","sub_marks2", "sub_marks3"],
#     ["kapil",19,77,76,86],
#     ["yash",20,88,65,75],
#     ["yogesh",21,99,84,79],
# ]

# with open('students.csv','w')as f:
#     writer = csv.writer(f)
#     writer.writerow(studentrecords)
    
# with open('students.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
        
# search = input("enter name of student").lower()
# found = True
# with open("students.csv", "r") as f:

#     reader = csv.reader(f)
#     found = True
#     for row in reader:
#         if row:
#             if row[0] == search:
#                 found = False
#                 print(row)
# if found :
#     print("student found") 
# else :
#     print("student not found")


