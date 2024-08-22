# student = {'name': 'John', 'age': '25', 'courses': ['math', 'science']}
#
# student.update({'name': 'jane', 'age': '26', 'phone': '555-5555'})
#
# print(student)

#to delete any dictionaries:
# student = {'name': 'John', 'age': '25', 'courses': ['math', 'science']}
#
# del student['age']
#
# print(student)

student = {'name': 'John', 'age': '25', 'courses': ['math', 'science']}

for key, value in student.items():
    print(key, value)