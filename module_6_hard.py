class Figure:
    sides_1 = []
    color_1 = []
    filled = False

    def __init__(self, rgb, *side):
        self.side = side[0]
        self.color = list(rgb)
        self.filled = True

    def get_color(self):
        self.color_1 = self.color
        self.filled = True
        return self.color_1

    def is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.is_valid_color(r, g, b):
            self.color = [self.r, self.g, self.b]

    def __is_valid_sides(self, *args):
        for side in self.sides:
            if len(self.sides) == self.sides_count and side > 0 and type(side) == int:
                return True
            else:
                return False

    def set_sides(self, *args):
        side_list = []
        self.sides = list(args)
        if self.__is_valid_sides(self, *args):
            self.get_sides()
        else:
            for i in range(self.sides_count):
                side_list.append(self.side)

            self.sides = side_list
            self.get_sides()

    def get_sides(self):
        self.sides_1 = self.sides
        return self.sides_1

    def __len__(self):
        return self.side * self.sides_count


class Circle(Figure):
    sides_count = 1
    radius = None

    def set_radius(self):
        self.radius = self.__len__() / (2 * 3.141569)
        return self.radius

    def get_square(self):
        self.set_radius()
        return (self.radius ** 2) * 3.141569


class Triangle(Figure):
    sides_count = 3
    height = None

    def get_square(self):
        return (self.side ** 2) * (3 ** 0.5) / 4

    def set_height(self):
        self.height = self.side * (3 ** 0.5) / 2
        return self.height


class Cube(Figure):
    sides_count = 12

    def set_side_cube(self):
        set_side_cube = []
        for element in range(self.sides_count):
            set_side_cube.append(self.side)
        self.sides_1 = set_side_cube
        return self.sides_1

    def get_volume(self):
        return self.side ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())



class Circle(Figure):
    sides_count = 1
    radius = None

    def set_radius(self):
        self.radius = self.__len__() / (2 * 3.141569)
        return self.radius

    def get_square(self):
        self.set_radius()
        return (self.radius ** 2) * 3.141569


class Triangle(Figure):
    sides_count = 3
    height = None

    def get_square(self):
        return (self.side ** 2) * (3 ** 0.5) / 4

    def set_height(self):
        self.height = self.side * (3 ** 0.5) / 2
        return self.height


class Cube(Figure):
    sides_count = 12

    def set_side_lst(self):
        set_side_lst = []
        for element in range(self.sides_count):
            set_side_lst.append(self.side)
        self.sides_1 = set_side_lst
        return self.sides_1

    def get_volume(self):
        return self.side ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
