# Define a basic class called 'Car'
class Car:
    # The __init__ method is the constructor
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to describe the car
    def description(self):
        return f"{self.year} {self.make} {self.model}"

    # Method to simulate starting the engine
    def start_engine(self):
        return f"The {self.model}'s engine is now running."


# Define a subclass 'ElectricCar' that inherits from the Car class
class ElectricCar(Car):
    # The __init__ method in the subclass also calls the __init__ of the parent class
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)  # Call the parent class constructor
        self.battery_size = battery_size  # Additional attribute for ElectricCar

    # Override the start_engine method for ElectricCar
    def start_engine(self):
        return f"The {self.model}'s electric engine is now running silently."

    # New method specific to ElectricCar
    def battery_info(self):
        return f"The {self.model} has a {self.battery_size}-kWh battery."

# Demonstrating Polymorphism: Both Car and ElectricCar have a start_engine method,
# but each behaves differently based on the object type (this is polymorphism).
def start_vehicle_engine(vehicle):
    print(vehicle.start_engine())

if __name__ == "__main__":
    # Create objects (instances) of the Car and ElectricCar classes
    fun_car = Car("BMW", "M5", 2024)
    boring_car = ElectricCar("Tesla", "Model 3", 2023, 75)  # This is an ElectricCar object

    # Access object attributes
    print(fun_car.description())  # Output: 2021 Toyota Corolla
    print(boring_car.description())  # Output: 2023 Tesla Model 3

    # Call object methods
    print(fun_car.start_engine())  # Output: The Corolla's engine is now running.
    print(boring_car.start_engine())  # Output: The Model 3's electric engine is now running silently.

    # Call the new method in ElectricCar
    print(boring_car.battery_info())  # Output: The Model 3 has a 75-kWh battery.

    start_vehicle_engine(fun_car)  # Output: The Corolla's engine is now running.
    start_vehicle_engine(boring_car)  # Output: The Model 3's electric engine is now running silently.
