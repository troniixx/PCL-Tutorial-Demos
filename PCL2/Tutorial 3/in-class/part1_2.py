class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def greet(self):
        """Print a greeting from the pet."""
        print(f"Hello, I am {self.name} the {self.species}!")

    def feed(self, food):
        """Feed the pet some food."""
        print(f"{self.name} munches on {food}.")

class Dog(Pet):
    def __init__(self, name):
        # We can assume a Dog is always species="Dog".
        # We call the base class constructor using super().
        super().__init__(name, "Dog")

    def greet(self):
        """Override the greet method for a dog."""
        print(f"Woof! My name is {self.name}. I'm a friendly dog!")

    def bark(self, times=1):
        """A brand-new method only available to Dog."""
        print("Woof! " * times)


if __name__ == "__main__":
    my_pet = Pet("Mittens", "Cat")
    my_pet.greet()        # Hello, I am Mittens the Cat!
    my_pet.feed("fish")   # Mittens munches on fish.

    my_dog = Dog("Buddy")
    my_dog.greet()        # Woof! My name is Buddy. I'm a friendly dog!
    my_dog.feed("bones")  # Buddy munches on bones.
    my_dog.bark(3)        # Woof! Woof! Woof!
