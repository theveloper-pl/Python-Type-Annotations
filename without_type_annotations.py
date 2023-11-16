class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        return f"{self.engine_type} engine started"







class Car:
    def __init__(self, model, engine, production_year):
        self.model = model
        self.engine = engine
        self.production_year = production_year

    def start_car(self):
        return f"{self.model} with {self.engine.start()}"

    def __str__(self):
        return f"{self.model} - {self.engine} - {self.production_year}"







my_car = Car("Mustang", "V8", "2000")
print(my_car)
print(my_car.start_car())
























# run with mypy
# pylance settings "python.analysis.typeCheckingMode": "strict",
# ctrl shift p     settings.json