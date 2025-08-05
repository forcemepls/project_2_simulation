from base_entity import Entity

# class Entity:
#     """ Все сущности """
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y

class Creature(Entity):
    """ Существо """
    def __init__(self, x: int, y: int, hp: int = 100):
        super().__init__(x, y)  # инициализация координат через родительский класс
        self.hp = 100


class Herbivore(Creature):
    """ Травоядные, стремящиеся найти ресурс (траву),
     может потратить свой ход на движение в сторону
     травы, либо на ее поглощение.
     Если HP травоядного снижается до 0, то оно исчезает."""
    def make_move(self):  # вызывает bfs??
        pass


class Predator(Creature):
    """ Хищники, обладающие силой атаки, свой ход
     тратят на перемещение в сторону к жертве
     (травоядному) или на атаку травоядного. При этом
     количество HP травоядного уменьшается на силу атаки
     хищника.
     Если HP хищника снижается до 0, то оно исчезает."""
    def make_move(self):  # вызывает bfs??
        pass


class Grass(Entity):  #
    """ Сущность трава - статическая обновляемая сущность.
    Может быть поглощена травоядным"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    def grow_up(self):
        """ Способность вырасти новой траве в случае недостатка ее на карте """
        pass


class Rock(Entity):
    """ Сущность камень - статическая сущность """
    def __init__(self, x: int, y: int):
        super().__init__(x, y)


class Tree(Entity):
    """ Сущность дерево - статическая сущность."""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)