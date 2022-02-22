from wandering import Comunwandering
from track import Track, track
from location import Location
from bokeh.plotting import figure, output_file,show


def walking(location, wandering, step):
    beginning = location.get_location(wandering)
    for  _ in range(step):
        location.move_wandering(wandering)


        return beginning.distance(location.get_location(wandering))