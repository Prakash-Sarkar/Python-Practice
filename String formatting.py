# person = {'name': 'Jehn', 'age':23}
#
# l = ['Jehn', 23]
#
# sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)
# print(sentence)

import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

#March 01, 2016 fell on a Tuesday and was the 061 day of the year.

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)
