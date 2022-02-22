
from wandering import Comunwandering
from track import Track
from location import Location
from bokeh.plotting import figure, output_file, show


def walking(location, wandering, step):
    beginning = location.get_location(wandering)
    for  _ in range(step):
        location.move_wandering(wandering)


    return beginning.distances(location.get_location(wandering))
    

def simulate_walk(steps, number_attempts, type_wandering):
    wandering = type_wandering(name='Alirio')
    origen = Track(0, 0)
    distances = []

    for _ in range(number_attempts):
        location = Location()
        location.add_wandering(wandering, origen)
        simulations_walk = walking(location, wandering, steps)
        distances.append(round(simulations_walk, 1))
    return distances

def graph(x, y):
    graphics = figure(title='camino del errante,' x_axis_label='pasos', y_axis_label='distancia')
    graphics.line(x, y, legend='distancia')
    show(graphics)


def main(distances_walk, number_attempts, type_wandering):
    average_walking_distance = []
    
    for steps in distances_walk:
        distances = simulate_walk(steps, number_attempts, type_wandering)
        middle_distance = round(sum(distances) / len(distances), 4)
        max_distances = max(distances)
        min_distances = min(distances)
        average_walking_distance.append(middle_distance)
        print(f'{type_wandering.__name__} caminata aleatoria de {steps} pasos')
        print(f'media=  {middle_distance}')
        print(f'max = {max_distances}')
        print(f'min = {min_distances}')
    graph(distances_walk, average_walking_distance)

if __name__ == '__main__':
    distances_walk = [10,100,1000,10000]
    number_attemps = 100
    main(distances_walk, number_attempts, Comunwandering)