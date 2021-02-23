from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def move(self) -> bool:
        pass

    @abstractmethod
    def stop(self) -> bool:
        pass


class Tractor(Car):
    def move(self) -> bool:
        pass  # do something

    def stop(self) -> bool:
        pass  # do anything


tractor = Tractor()  # => OK


class Kar(Car):
    def move(self) -> bool:
        pass  # do something


kar = Kar()  # => TypeError
# and => (mypy) error: Cannot instantiate abstract class 'Kar' with abstract attribute 'stop'


class BaseCar:
    def move(self) -> bool:
        raise NotImplementedError

    def stop(self) -> bool:
        raise NotImplementedError


class Truck(BaseCar):
    def move(self) -> bool:
        pass  # do something


truck = Truck().stop()  # => NotImplementedError