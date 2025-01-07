import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self,  speed):
        self._coords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._coords[0] += dx * self.speed
        self._coords[1] += dy * self.speed
        self._coords[2] += dz * self.speed
        if self._coords[2] <= 0:
            print("It's too deep, i can't dive :(")
            self._coords[2] = 0

    def get_coords(self):
        print(f'X: {self._coords[0]}, Y:  {self._coords[1]}, Z:  {self._coords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._coords[2] = -(abs(dz) * self.speed)/2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill( AquaticAnimal, Bird, PoisonousAnimal):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = 'Click-click-click'

    def speak(self):
        print(self.sound)

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_coords()
db.dive_in(6)
db.get_coords()
db.lay_eggs()

db.lay_eggs()
db.dive_in(6)
db.get_coords()

db.lay_eggs()
