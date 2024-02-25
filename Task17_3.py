class Shape:
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square
    def set_colour(self):
        n1 = input('Установите цвет объекта: ')
        self.colour = n1
    def get_colour(self):
        print(f'{self.colour}')
    def set_square(self):
        n2 = input('Задайте площадь объекта: ')
        self.square = n2
    def get_square(self):
        print(f'{self.square}')

a = Shape('Красный', 20)
b = Shape('Синий', 25)

a.set_colour()
a.get_colour()
b.set_square()
b.get_square()





