class Animal(object):

    @property
    def age(self):
        try:
            return self._age
        except AttributeError:
            print("Attribute Error")

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError

    owner = 'jack'

    def __init__(self, name):
        self._name = name
    def __init__(self):
        pass

    @classmethod
    def get_owner(cls):
        return cls.owner  

    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def make_sound(self):
        pass
    

class Dog(Animal):
    def make_sound(self):
        print(self.get_name() + 'is making sound wang wang wang')


class Cat(Animal):
    def make_sound(self):
        print(self.get_name() + 'is making sound miu miu miu')


# dog = Dog('my_dog')
# cat = Cat('my_cat')
# dog.make_sound()
# cat.make_sound()
# animals = [Dog('wang'), Cat('Kity'), Dog('hask'), Cat('dd')]
# for animal in animals:
#     animal.make_sound()

cat = Animal()
# cat.age = 3
cat.owner = 'peter'
print(cat.owner)
print(cat.age)


