#Here we are setting up the class Hedgehog that takes a name for the 
#constructor and has the behaviours make_sound and flee. 
#I am following the open/closed principle so I have set it up in a way where 
#I am not going to have to modify it and can extend it via subclasses/children
#instead
class Hedgehog:
    #Here is the constructor which which we use for intantiating Hedgehog objects
    #and giving them a name
    def __init__(self, name):
        self.name = name

    #The make_sound method returns the sound the hedgehog makes interpolated into
    #a string along with their name
    def make_sound(self):
        return f"The hedgehog {self.name} snuffles"
    
    #The make_sound method returns the fleeing action the hedgehog makes interpolated
    #into a string along with their name
    def flee(self):
        return f"The hedgehog {self.name} curls up into a ball and rolls away"

#Creates a subclass LargeHedgehog of the base class Hedgehog, for 
#extension of code without needing to modify the base class
class LargeHedgehog(Hedgehog):
    #Here we are using polymorphism to give the make_sound method a new behaviour
    #In this case the hedgehog of the given name will now grunt
    def make_sound(self):
        return f"{self.name} grunts"
    
    #Here we are using polymorphism to give the flee method a new behaviour
    #In this case the hedgehog of the given name will now run for the hills
    def flee(self):
        return f"{self.name} runs for the hills"
    
    #Here we are extending the code and not modifying the base class
    #by creating a new method thump which makes the hedgehog of the given name
    # do a large thump
    def thump(self):
        return f"{self.name} does a large thump"

class SmallHedgehog(Hedgehog):
    def make_sound(self):
        return f"A small squeaking sound is let out by {self.name}"
        
    def flee(self):
        return f"The hedgehog {self.name} flees the scene of the crime"
        
    #Here we are extending the code and not modifying the base class
    #by creating a new method jump which makes the hedgehog of the given name
    # do a little jump
    def jump(self):
        return f"{self.name} does a little jump"
        
#Create an instance of the Hedgehog class, bob
bob = Hedgehog("bob")
#Create an instance of the LargeHedgehog class, Tiny
tiny = LargeHedgehog("Tiny")
#Create an instance of the LargeHedgehog class, Titan
titan = SmallHedgehog("Titan")

#Here I am simply outputing the results of the methods that I have created
#within the classes above
print(bob.make_sound()) 
print(bob.flee()) 
print(tiny.make_sound()) 
print(tiny.flee()) 
print(tiny.thump())
print(titan.make_sound())
print(titan.flee())
print(titan.jump())


#Closing remarks: Here you can see that I have started with a base class Hedgehog and instead
#of having to modify its existing behaviour I just extended it through the use of subclassing
#setting up the behaviour that I wanted in those subclasses instead
