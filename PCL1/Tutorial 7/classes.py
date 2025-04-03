# Author: Mert Erol

class frog():
    def __init__(self, name, age, hobby):
        """
        Initialize the frog object with a name, age and hobby
        """

        self.name = name
        self.age = age
        self.hobby = hobby

    def jump(self):
        """
        returns the string "Jumping"
        """

        return "Jumping"
    
    def swim(self):
        """       
        returns the string "Swimming"
        """

        return "Swimming"
    
    def croak(self):
        """
        returns the string "Croaking"
        """

        return "Croaking"

class pepe(frog):
    def makeMeme(self):
        return "Feels good man"

class kermit(frog):
    def playBanjo(self):
        return "Yay music"
    
if __name__ == "__main__":

    """
    Feel free to comment out the lines of code that you dont want to run and play around with the code. You can also add more lines of code to learn about classes
    """

    # Create objects
    frog1 = frog("Fred", 3, "playing with toy cars")
    pepe_the_frog = pepe("Pete", 2, "playing with toy cars")
    kermit_the_frog = kermit("Kermit", 4, "playing with toy cars")
    
    # Call methods
    print(frog1.jump())  # Output: Jumping
    print(pepe_the_frog.makeMeme())  # Output: Feels good man
    print(kermit_the_frog.playBanjo())  # Output: Yay music
    print(kermit_the_frog.croak())  # Output: Croaking
    print(pepe_the_frog.swim())  # Output: Swimming
    print(frog1.croak())  # Output: Croaking

    #! You dont need to understand the try except block yet

    try:
        print(pepe_the_frog.playBanjo())  # Output: AttributeError: 'pepe' object has no attribute 'playBanjo'
    except AttributeError as e:
        print(f"An error occurred: {e}")

    try:
        print(kermit_the_frog.makeMeme())  # Output: AttributeError: 'kermit' object has no attribute 'makeMeme'
    except AttributeError as e:
        print(f"An error occurred: {e}")