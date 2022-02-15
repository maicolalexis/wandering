from calendar import c
import random;


class wardering:
    def __init__(self, name):

        self,name = name

class Comunwandering(wardering):
        def __init__(self, name):
            super().__init__(name)


        def walk(self):
            return random.choice([(0,3), (0,-3), (3,0), (-3,0)])