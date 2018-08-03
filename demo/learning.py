filename = 'you_can.txt'

print('\n print as a file')
with open(filename) as file_object:
    file_contant = file_object.read()
    print(file_contant)

print('\n print as loop')
with open(filename) as file_object:
    for single_line in file_object:
        print(single_line.strip())

print('\n storing lines in a list')
with open(filename) as file_object:
    list = file_object.readlines()
print(list)

