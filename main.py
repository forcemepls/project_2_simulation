from base_entity import Entity
from entities import Creature, Herbivore, Predator, Grass, Rock, Tree
from simulation import Simulation, Actions, Map


def bfs():  # будет 9 ситуаций
    """ Поиск в ширину """
    pass

def main():

    map_size = 0

    while map_size <= 3:
        try:
            map_size = int(input('Введите размеры карты NxN (больше трёх): '))
        except ValueError:
            print('Введите целочисленное значение')

    world = Map()
    world.start(map_size)

if __name__ == '__main__':
    main()

# udp://1.1.1.1