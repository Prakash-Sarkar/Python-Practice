#Dictionary comprehension:
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# my_dict = {}
# for name, heroes in zip(names, heroes):
#     my_dict[name] = heroes
# print (my_dict)

# my_dict = {name: hero for name, hero in zip (names, heroes)}
# print (my_dict)

#Set comprehension:
nums = [1,1,3,2,2,3,5,4,4,6,8,7,9,10]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print (my_set)

my_set = {n for n in nums}
print (my_set)