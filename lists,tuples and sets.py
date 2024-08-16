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
# courses = ['math', 'physics', 'science', 'art']
#
# courses.sort()
# print(courses)

#how to sort words:
# courses = ['math', 'physics', 'science', 'art']
#
# sorted_courses = sorted(courses)
# print(sorted_courses)

#to check anything that is available in the list or not:
# courses = ['math', 'physics', 'science', 'art']
# print('education'in courses)

#for and index:
# courses = ['math', 'physics', 'science', 'art']
# for index, item in enumerate(courses, start=1):
#     print(index, item)

#how to use 'join' function:
# courses = ['math', 'physics', 'science', 'art']
# course_str = '-'.join(courses)
# print(course_str)

#Tuples are immutable:
# tuple_1 = ('math', 'physics', 'science', 'art')
# tuple_2 = tuple_1
#
# # print (tuple_1)
# # print (tuple_2)
#
# tuple_1[0] = 'art'
#
# print (tuple_1)
# print (tuple_2)

#sets:
# cs_courses = {'math', 'physics', 'english', 'computer'}
# art_courses = {'education', 'math', 'english', 'design'}
#
# print(cs_courses.intersection(art_courses))

# cs_courses = {'math', 'physics', 'english', 'computer'}
# art_courses = {'education', 'math', 'english', 'design'}
#
# print(cs_courses.difference(art_courses))

cs_courses = {'math', 'physics', 'english', 'computer'}
art_courses = {'education', 'math', 'english', 'design'}

print(cs_courses.union(art_courses))