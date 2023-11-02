"""
Прототип - паттерн, позволяющий копировать объекты не вдаваясь в подробности их реализации
"""
import abc


class Representable:
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.__dict__)}: {id(self)})\n"


class Shape(abc.ABC, Representable):
    X: int
    Y: int
    color: str

    def __init__(self, source: 'Shape') -> None:
        self.X = source.X
        self.Y = source.Y
        self.color = source.color

    @abc.abstractmethod
    def clone(self) -> 'Shape':
        pass


class Rectangle(Shape):
    width: int
    height: int

    def __init__(self, width: int, height: int, *, source: 'Rectangle' = None) -> None:
        self.width = width
        self.height = height

        if source is not None:
            super().__init__(source)
            self.width = source.width
            self.height = source.height

    def clone(self) -> 'Shape':
        return Rectangle(self.width, self.height, source=self)


class Circle(Shape):
    radius: int

    def __init__(self, radius: int, *, source: 'Circle' = None) -> None:
        self.radius = radius

        if source is not None:
            self.radius = source.radius
            super().__init__(source)

    def clone(self) -> 'Shape':
        return Circle(self.radius, source=self)


class ShapesList:
    shapes_list: list[Shape]

    def __init__(self, arr: list[Shape]):
        # Главное преимущество - мы можем получать копии объектов, через единый интерфейс
        self.shapes_list = [shape.clone() for shape in arr]


if __name__ == "__main__":
    shapes: list[Shape] = []
    circle = Circle(23)
    circle.X = 10
    circle.Y = 20
    circle.color = "yellow"

    rectangle = Rectangle(12, 23)
    rectangle.X = 34
    rectangle.Y = 45
    rectangle.color = "black"

    # Все инстансы класса, являются отдельными сущностями, что хорошо
    # видно при выводе адреса объекта через id()
    shapes.append(circle)
    shapes.append(rectangle)
    shapes.append(circle.clone())
    shapes.append(rectangle.clone())

    shape_list = ShapesList(shapes)

    # Созданный руками список
    print(shapes)

    # Скопированный из переданного список
    print(shape_list.shapes_list)
