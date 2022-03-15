from calendar import c
import random;


class wardering:
    def __init__(self, name, x=0, y = 0):

        self.name = name
        self.x = x
        self.y = y

    def posicion(self):
        return (self.x, self.y)

    def distance_origin(self)
        return (self.x**2 + self.y**2)**5

class Comunwandering(wardering):
        def __init__(self, name):
            super().__init__(name)


        def walk(self):
            dx, dy =  random.choice([(0,1), (0,-1), (1,0), (-1,0)])
            self.x += dx
            self.y += dy
            return [dx, dy]

class RightWandering(wardering):
        def __init__(self, name):
            super().__init__(name)

        def walk(self):
            dx, dy =  random.choice([(0,5), (5,0),(-1, 0), (0, -1)])
            self.x += dx
            self.y += dy
            return [dx, dy]


class LeftWandering(wardering):
        def __init__(self, name):
            super().__init__(name)

        def walk(self):
            dx, dy =  random.choice([(0,1), (1,0),(-5, 0), (0, 5)])
            self.x += dx
            self.y += dy
            return [dx, dy]