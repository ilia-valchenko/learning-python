class Dog:
    def __init__(self, name):
        self.name = name
        self.numberOfLegs = 4

    def speak(self):
        print(self.name + ' says: Bark!')

myDog = Dog('Rover')
myDog.speak()
