import random
from entities import Tree, Rock, Grass, Herbivore, Predator


GRAY = '\033[90m'
DARK_GRAY = '\033[30m'
RESET = '\033[0m'


ENTITY_SYMBOLS = {
    'Herbivore': '🦙',
    'Predator': '🐆',
    'Grass': '🌿',
    'Stone': '⛰️',
    'Tree': '🌳',
    'Empty': ' ',
}


class Simulation:
    """ Главный класс приложения, включает в себя:
     - Карту
     - Счётчик ходов
     - Рендерер поля
     - Actions - список действий, исполняемых перед
     стартом симуляции или на каждом ходу"""
    def __init__(self):
        pass


class Actions:
    """ Действие, совершаемое над миром.
     Например - сходить всеми существами. Это действие
     итерировало бы существ и вызвало каждому make_move().
     Каждое действие описывается отдельным классом
     и совершает операции над картой.
     Симуляция содержит 2 массива действий:
     - init_actions - действия, совершаемые перед стартом
     симуляции;
     - turn_actions - действия, совершаемые каждый ход.
     Примеры - передвижение существ, добавить травы или
     травоядных, если их осталось слишком мало"""
    pass


class Map:
    """ Карта - содержит в себе коллекцию для хранения
     существ и их расположения. """
    def __init__(self):
        self.map_data = {}  # словарь: здесь хранится информация о клетках


    def map_data_information(self, map_size: int, count_objects: list):
        """ Заполнения словаря map_data информацией (для каждой клетки) """

        # Просто перебор всевозможных координат
        coordinates = [(x, y) for x in range(map_size) for y in range(map_size)]

        # Пока что, до расстановки, каждая клетка пустая
        for i in coordinates:
            self.map_data[i] = None

        object_classes = {
            Tree: count_objects[0],
            Rock: count_objects[1],
            Grass: count_objects[2],
            Herbivore: count_objects[3],
            Predator: count_objects[4],
        }

        # Принимаю пару ключ-значение (Класс-Значение)
        for object_type, count in object_classes.items():
            for _ in range(count):
                coord = random.choice(coordinates)

                # поиск пустой клетки
                while self.map_data[coord] is not None:
                    coord = random.choice(coordinates)

                # создаю объект в соответствующей клетке
                self.map_data[coord] = object_type(x=coord[0], y=coord[1])

                # и убираю эту клетку из доступных для выбора
                coordinates.remove(coord)


    def __get_cell_color(self, x: int, y: int):
        """ Определение цвета клетки (для чередования) """
        if (x + y) % 2 == 0:
            return GRAY
        else:
            return DARK_GRAY


    def __draw_board(self, map_size: int):
        """ Выводит доску с объектами на ней """


    def __count_random(self, map_size: int):
        """ Рандомно вычисляем количество объектов на карте"""
        total = map_size**2 // 3

        total_trees = total // 5
        total_stones = total // 5
        total_grasses = total // 5
        total_herbivores = total // 5
        total_predators = total // 5

        return [total_trees, total_stones, total_grasses, total_herbivores, total_predators]


    def show_board(self):
        print(self.map_data)


    def start(self, map_size):
        count_objects = self.__count_random(map_size)
        self.map_data_information(map_size, count_objects)
        self.__draw_board(map_size)
        self.show_board()