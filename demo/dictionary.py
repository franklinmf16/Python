alien_0 = {'color': 'green', 'points': 5}
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
alien_1['y_position'] = 25
alien_1['x_position'] = 10

print(alien_0['color'])
print(alien_0['points'])
print('\n')



favourite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

friends = ['phil', 'sarah']
for name in favourite_language.keys():
    print(name.title())
    if name in friends:
        print(" Hi" + name.title() + 
            ", I see your favourite language is " + 
            favourite_language[name].title() + "!")

if 'erin' not in favourite_language.keys():
    print("erin, please take our poll!")
if 'python' in favourite_language.values():
    print("python is in the favourite language ")









