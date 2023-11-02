"""
Определяет общий интерфейс для создания объектов в
суперклассе, позволяя подклассам изменять тип создаваемых объектов
"""

import abc
import os

from common import describer


class ITransport(abc.ABC):
    @abc.abstractmethod
    def transport(self):
        pass

    @abc.abstractmethod
    def unload(self):
        pass

    @abc.abstractmethod
    def load(self):
        pass


class CarTransport(ITransport):
    @describer
    def transport(self):
        """
        Перевозка наземным способом
        """
        print("перевозка завершена")

    @describer
    def unload(self):
        """
        Разгрузка наземного транспорта
        """
        print("наземная разгрузка завершена")

    @describer
    def load(self):
        """
        Загрузка наземного транспорта
        """
        print("наземная загрузка завершена")


class ShipTransport(ITransport):
    @describer
    def transport(self):
        """
        Перевозка морским способом
        """
        print("перевозка завершена")

    @describer
    def unload(self):
        """
        Разгрузка морского транспорта
        """
        print("морская разгрузка завершена")

    @describer
    def load(self):
        """
        Загрузка морского транспорта
        """
        print("морская загрузка завершена")


class AStock(abc.ABC):
    def send_for_route(self):
        transport = self._create_transport()
        transport.load()
        transport.transport()

    @abc.abstractmethod
    def _create_transport(self) -> ITransport:
        pass


class CarStock(AStock):
    def _create_transport(self) -> ITransport:
        return CarTransport()


class ShipStock(AStock):
    def _create_transport(self) -> ITransport:
        return ShipTransport()


class TradeRoute:
    stock: AStock

    def __init__(self):
        match os.getenv('MODE'):
            case 'Car':
                self.stock = CarStock()
            case 'Ship':
                self.stock = ShipStock()
            case _:
                raise Exception("Error! Unknown transport")


trade_route = TradeRoute()
trade_route.stock.send_for_route()
