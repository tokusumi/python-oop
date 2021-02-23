from abc import ABC, abstractmethod


class Car(ABC):
    @property
    @abstractmethod
    def is_active(self) -> bool:
        pass

    @property
    @abstractmethod
    def gasoline(self) -> float:
        pass

    @gasoline.setter
    def gasoline(self, value: float) -> None:
        pass

    @abstractmethod
    def move(self) -> None:
        pass


def stop(car: Car) -> None:
    # 実行時の副作用の低減
    # setterを用意したものだけ変更可能に
    car.gasoline -= 0.1

    # read-onlyな属性の変更を検知
    car.is_active = False
    # => (mypy) error: Property "is_active" defined in "Car" is read-only


class Truck(Car):

    _is_active = False
    _gasoline = 0.0

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool) -> None:
        self._is_active = value

    @property
    def gasoline(self) -> float:
        return self._gasoline

    @gasoline.setter
    def gasoline(self, value: float) -> None:
        self._gasoline = value

    def move(self) -> None:
        # 継承先のmethod内の副作用の検知は容易にハック可能
        self.is_active = True
        self.gasoline -= 0.1


def stop_truck(car: Truck) -> None:
    # polymorphismでないと、容易にハック可能なので注意
    # ただし、Truck クラスにしか使わない関数としては正常
    car.gasoline -= 0.1

    # read-onlyな属性の変更を検知"できない"
    car.is_active = False
