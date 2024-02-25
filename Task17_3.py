class Shape:
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square
    def enter_colour(self):
        n1 = input('Установите цвет объекта: ')
        self.colour = n1
    def what_colour(self):
        print(f'{self.colour}')
    def enter_square(self):
        n2 = input('Задайте площадь объекта: ')
        self.square = n2
    def what_square(self):
        print(f'{self.square}')

a = Shape('Красный', 20)
b = Shape('Синий', 25)

a.enter_colour()
a.what_colour()
b.enter_square()
b.what_square()





