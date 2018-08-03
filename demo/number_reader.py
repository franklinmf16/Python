import json


filename = '/Users/boxianmo/Desktop/Code/Python/numbers.json'
with open(filename) as f_object:
    numbers = json.load(f_object)

print(numbers)


