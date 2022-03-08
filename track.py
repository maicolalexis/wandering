class Track:
    def  __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        return Track(self.x + delta_x, self.y + delta_y)


    def distance(self, other_track):
        delta_x = self.x - other_track.x
        delta_y = self.y - other_track.y

        return(delta_x**2 + delta_y**2)**0.5