"""
Строитель - паттерн, который позволяет создавать сложные объекты пошагово.

Строитель дает возможность использовать один и тот же код строительства для получения разных представлений объектов
"""
import abc


class Car:
    pass


class Manal:
    pass


class Builder(abc.ABC):
    @abc.abstractmethod
    def reset(self):
        pass

    @abc.abstractmethod
    def set_seats(self):
        pass

    @abc.abstractmethod
    def set_engine(self):
        pass

    @abc.abstractmethod
    def set_trip_computer(self):
        pass

    @abc.abstractmethod
    def set_GPS(self):
        pass


class CarBuilder(Builder):
    _car: Car

    def reset(self):
        self._car = Car()

    def set_GPS(self):
        pass

    def set_engine(self):
        pass

    def set_seats(self):
        pass

    def set_trip_computer(self):
        pass

    def get_result(self):
        pass


class CarManualBuilder(Builder):
    _manual: Manal

    def reset(self):
        pass

    def set_seats(self):
        pass

    def set_engine(self):
        pass

    def set_trip_computer(self):
        pass

    def set_GPS(self):
        pass

    def get_result(self):
        pass


class Director:
    def construct_sport_car(self, builder: Builder):
        builder.reset()
        builder.set_seats(2)
        builder.set_engine(SportEngine())
        builder.set_trip_computer(True)
        builder.set_GPS(True)



director = Director()


builder = CarBuilder()

director.construct_sport_car(builder)

car = builder.get_result()
