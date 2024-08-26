# def hello_func():
#     print('Hello Function.')
#
# hello_func()
# hello_func()
# hello_func()
# hello_func()

def student_info(*arg, **kwargs):
    print(arg)
    print(kwargs)

courses = ['math', 'art']
info = {'name': 'john', 'age': '22'}

student_info(*courses, **info)