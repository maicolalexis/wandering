class location:
    
    def __init__(self):
        self.location_wandering = {}
        
    def add_wardering(self, wandering, location):
        self.location_wandering[wandering] = location
            
    def move_wardering(self, wandering):
        delta_x, delta_y = wandering.walk()
        location_now = self.location_wandering[wandering]
        new_location = location_now.move(delta_x, delta_y)

        self.location_wandering[wandering] = new_location
    def get_location(self, wandering):
        return self.location_wandering[wandering]