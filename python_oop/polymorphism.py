from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def move(self) -> None:
        pass


class Taxi(Car):
    def move(self) -> None:
        pass

    def stop(self) -> None:
        pass


class Truck(Car):
    def move(self) -> None:
        pass

    def load(self) -> None:
        pass


def get_car(model: str) -> Car:
    if model == "taxi":
        return Taxi()
    else:
        return Truck()


def stop_car(car: Car, model: str) -> None:
    # > ポリモーフィズムはそのインターフェイス（抽象･規格）に対してプログラムするということです。
    # -> 定義しているスコープの中で抽象クラスとして型アノテーションがついていればmypyがよしなにやってくれる。

    # 1. 引数に入れて抽象クラスで型ヒントをつける
    car.stop()  # => (mypy) error: "Car" has no attribute "stop"

    # 2. 代入前に変数に型ヒントを付ける
    car2: Car
    if model == "taxi":
        car2 = Taxi()
    else:
        car2 = Truck()
    car2.stop()  # => (mypy) error: "Car" has no attribute "stop"

    # 3. 出力がアノテーションされた関数などをかます。
    car3 = get_car(model)
    car3.stop()  # => (mypy) error: "Car" has no attribute "stop"


def get_car_legacy(model: str):
    if model == "taxi":
        car = Taxi()
    else:
        car = Truck()
    if isinstance(car, Car):
        return car
    raise TypeError


def stop_car_legacy(car, model: str) -> None:
    # > ポリモーフィズムはそのインターフェイス（抽象･規格）に対してプログラムするということです。
    # -> 定義しているスコープの中で抽象クラスとして型アノテーションがついていればmypyがよしなにやってくれる。

    # 1. 引数に入れて抽象クラスで型ヒントをつける
    if isinstance(car, Car):
        car.stop()  # => (mypy) error: "Car" has no attribute "stop"

    # 2. 代入前に変数に型ヒントを付ける
    car2: Car
    if model == "taxi":
        car2 = Taxi()
    else:
        car2 = Truck()
    if isinstance(car2, Car):
        car2.stop()  # => (mypy) error: "Car" has no attribute "stop"

    # 3. （検知不可）出力がアノテーションされた関数などをかます。
    car3 = get_car_legacy(model)
    car3.stop()