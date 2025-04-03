import abc

class Vehicle(abc.ABC):
    @abc.abstractmethod
    def move(self):
        """Abstract method for how the vehicle moves."""
        pass

class Car(Vehicle):
    def move(self):
        print("The car drives on the road.")

class Bicycle(Vehicle):
    def move(self):
        print("The bicycle pedals down the bike lane.")

class Plane(Vehicle):
    def move(self):
        print("The plane soars through the sky.")

if __name__ == "__main__":
    # Abstract classes can't be instantiated directly:
    # my_vehicle = Vehicle()  # This would cause an error.

    my_car = Car()
    my_bike = Bicycle()
    my_plane = Plane()

    my_car.move()      # The car drives on the road.
    my_bike.move()     # The bicycle pedals down the bike lane.
    my_plane.move()    # The plane soars through the sky.
