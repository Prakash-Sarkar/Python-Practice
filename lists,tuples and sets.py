#to get the lists:
# courses = ['math', 'physics', 'science']
# print(courses)

#to get any specific one:
# courses = ['math', 'physics', 'science']
# print(courses[2:])

#if we wants to add anything in to the lists:
# courses = ['math', 'physics', 'science']
#
# courses.append('art')
# print(courses)

#instat of append we can use insert and also can chose where we wants to put that insertion:
# courses = ['math', 'physics', 'science']
#
# courses.insert(1, 'art')
# print(courses)

#how to do extend:
# courses = ['math', 'physics', 'science']
# courses_2 = ['art', 'education']
#
# courses.extend(courses_2)
# print(courses)

#to remove anything:
# courses = ['math', 'physics', 'science']
#
# courses.remove('math')
# print(courses)

#to reverse any thing:
# courses = ['math', 'physics', 'science']
#
# courses.reverse()
# print(courses)

#to sort the list:
courses = ['math', 'physics', 'science', 'art']

courses.sort()
print(courses)