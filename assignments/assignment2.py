names = ['Charlie', 'Alpha', 'Bees', 'Yulia', 'SomeNameHere']

for name in names:
    print(len(name))

    if len(name) > 5 and ('N' in name or 'n' in name):
        print(name + ' is greater than 5 characters long and contains an N or n')

print('Emptying names list')
while len(names) > 0:
    names.pop()
    print(names)