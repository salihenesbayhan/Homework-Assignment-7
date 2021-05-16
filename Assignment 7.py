names = ("Ross", "Rachel", "Chandler", "Monica", "Joey", "Phoebe")
friends_list = set()

for name in names:
    names_ = input(f'{name}, enter your friends you have invited separated by spaces: ')
    name_list = names_.split()
    for name in name_list:
        friends_list.add(name)

print('Here is the final list of people invited:')
for count, name in enumerate(friends_list, start=1):
    print(count, '.', name)