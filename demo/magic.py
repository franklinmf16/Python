def show_magicians(names):
    print("Teir name is")
    for name in names:
        print("Name is " + name)

def make_great(names, great_name_set):
    while names:
        new_great_magicians = names.pop()
        print("The great " + new_great_magicians)
        great_name_set.append(new_great_magicians)
    

magicians_name = ['Andy', 'Ben', 'Cindy']
great_magicians = []

show_magicians(magicians_name)
make_great(magicians_name[:], great_magicians)

print("\ncheck")
print(magicians_name)
print(great_magicians)