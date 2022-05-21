list_persons = [{'name': 'Michael', 'age': 20, 'hobbies': ['gaming', 'movies']}, 
                {'name': 'Charlie', 'age': 31, 'hobbies': ['running', 'fishing']},
                {'name': 'Sarah', 'age': 26, 'hobbies': ['reading', 'walking']}]

list_names = [person['name'] for person in list_persons]
print(list_names)

allOlderThan20 = all([person['age'] > 20 for person in list_persons])
print('Are all persons older than 20? ' + str(allOlderThan20))

list_persons_copy = [person.copy() for person in list_persons] 
list_persons_copy[0]['name'] = 'Gavin'

print("list_persons_copy")
print(list_persons_copy)
print()
print("list_perons")
print(list_persons)
print()

for person in list_persons:
    print(person)
    name, age, hobbies = [val for (key, val) in person.items()]
    print(name + ' is ' + str(age) + ' years old. ' + name + '\'s hobbies are ' + str(hobbies))
