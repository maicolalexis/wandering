
from turtle import color

from wandering import ComunWandering
from track import Track
from location import Location
from bokeh.plotting import figure, output_file, show




def know_type_wandering(type_wandering):
    if type_wandering.__name__ == "ComunWandering":
        return "herrante comun"
    elif type_wandering.__name__ == "RightWandering":
        return "herrante derechista"
    else:
        return "herrante izquierdista"


def walking(wandering, step, type_wandering):
    beginning = [wandering.posicion()]

    x_graph = [0]
    y_graph = [0]

    for  _ in range(step-1):
      wandering.walk()
      x, y = wandering.posicion()
      x_graph.append(x)
      y_graph.append(y)
    
    know_type = know_type_wandering(type_wandering)
    graph_step(x_graph, y_graph, know_type, step)
    return wandering.distance_origin()


    


    #return beginning.distance(location.get_location(wandering))
    

def simulate_walk(step, number_attempts, type_wandering):
    wandering =[]
    distances = []

    for i in range(number_attempts):
        wandering.append(type_wandering(name=f'Alirio {i}'))
        simulations_walk = walking(wandering[i], step, type_wandering)
        distances.append(round(simulations_walk, 1))
    return distances

def  graph_step(x_graph, y_graph, know_type, step):
    graphics = figure(title='camino del errante',  x_axis_label='pasos',  y_axis_label='distancia')
    graphics.line(x_graph, y_graph, legend_label=str(step)+' pasos')
    final_x = x_graph[-1]
    final_y = y_graph[-1]
    graphics.diamond_cross(0, 0, fill_color = "green", line_color ="green", size = 18)
    graphics.diamond_cross(final_x, final_y, fill_color ="red", line_color ="green", size = 18)
    straight_final_x = [0, final_x]
    straight_final_y = [0, final_y]
    graphics.line(straight_final_x, straight_final_y, line_width = 2, color="red")
    show(graphics)


def main(distances_walk, number_attempts, type_wandering):
    #average_walking_distance = []
    
    for step in distances_walk:
        distances = simulate_walk(step, number_attempts, type_wandering)
        middle_distance = round(sum(distances) / len(distances), 4)
        max_distances = max(distances)
        min_distances = min(distances)
        #average_walking_distance.append(middle_distance)
        print(f'{type_wandering.__name__} caminata aleatoria de {step} pasos')
        print(f'media=  {middle_distance}')
        print(f'max = {max_distances}')
        print(f'min = {min_distances}')
    #graph(distances_walk, average_walking_distance)

if __name__ == '__main__':
    distances_walk = [10000]
    number_attempts = 1
    main(distances_walk, number_attempts, ComunWandering)
