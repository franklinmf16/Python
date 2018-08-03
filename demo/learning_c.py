filename = 'you_can.txt'
print('\n replace')
with open(filename) as file_object:
    list = file_object.readlines()

for message in list:
    message = message.replace('Python', 'C')
    print(message.strip())

