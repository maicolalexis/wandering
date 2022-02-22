from turtle import distance, title
from wandering import Comunwandering
from track import Track
from location import Location
from bokeh.plotting import figure, output_file,show


def walking(location, wandering, step):
    beginning = location.get_location(wandering)
    for  _ in range(step):
        location.move_wandering(wandering)


        return beginning.distance(location.get_location(wandering))
    

def simulate_walk(steps, number, attempts, type_wandering):
    wandering = type_wandering(name='Alirio')
    origen = Location(0, 0)
    distances = []

        for _ in range(number_attempts):
            track = Track()
            track.add_wandering(wandering, origen)
            simulate_walk = walking(track, wandering, steps)
            distances.append(round(simulations_walk, 1))
            return distances

        def graph(x, y):
            graphics = figure(title='camino del errante,' x_axis_label='pasos', y_axis_label='distancia')
            graphics.line(x, y, legend='distancia')
            show(graphics)


