class Engine:
    def __init__(self, engine_type: str) -> None:
        self.engine_type: str = engine_type

    def start(self) -> str:
        return f"{self.engine_type} engine started"


class Car:
    def __init__(self, model: str, engine: Engine, production_year: int) -> None:
        self.model: str = model
        self.engine: Engine = engine
        self.production_year: int = production_year

    def start_car(self) -> str:
        return f"{self.model} with {self.engine.start()}"


my_engine = Engine("V8")
my_car = Car("Mustang", my_engine, 2021)


print(my_car.start_car())