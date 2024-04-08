#Here we are creating the animal class with all the methods and properties
class Animal:
    #Here we allow a name to be given to any instance of the animal class by passing it in as
    #an argument to the constructor method when it is invoked/called later on
    def __init__(self, name):
        self.name = name

    #Subclasses of the animal class will inherit the make_noise method
    #and the implementation of make_noise will be done there
    def make_noise(self):
        pass

    #Subclasses of the animal class will inherit the defend method
    #and the implementation of defend will be done there
    def defend(self):
        pass

    #Subclasses of the animal class with inherit the sleep method, along with
    #its implementation here in the base class.
    #Here we are setting up the behaviour for what should happen when the instance of
    #this class sleeps and in this case it simply rests
    def sleep(self):
        return f"{self.name} rests"

#Here we are setting up the Armadillo class which inherits from our base class of animal
class Armadillo(Animal):
    #The constructor method takes a name and armor_level when creating an instance of this class/invoking the
    #constructor, passes the name to the base constructor to be dealt with there and finally the armor_level of
    #each instance of this class will be set to the armor_level that is passed in
    def __init__(self, name, armor_level):
        super().__init__(name)
        self.armor_level = armor_level

    #Here we are setting up the behaviour for what should happen when the instance of
    #this class makes a noise and in this case it grunts
    def make_noise(self):
        return f"{self.name} grunts!"

    #Here we are setting up the behaviour for what should happen when the instance of
    #this class defends itself and in this case it rolls up into a protective ball
    def defend(self):
        return f"{self.name} rolls up into a protective ball"

    #Here we are setting up the behaviour for what should happen when the instance of
    #this class digs and in this case it simply digs into the ground
    def dig(self):
        return f"{self.name} digs into the ground"
        
    #Here we are setting up the behaviour for what should happen when the instance of
    #this class forages and in this case it searches for insects (to eat)
    def forage(self):
        return f"{self.name} searches for insects"
        
    #Here we are simply setting up the method get_armor_level which will enable
    #us to get any instance of this classe's armor_level
    def get_armor_level(self):
        return self.armor_level

#Here we are setting up the Armadillo class which inherits from our base class of animal
class Hedgehog(Animal):
    #The constructor method takes a name and spines_count when creating an instance of this class/invoking the
    #constructor, passes the name to the base constructor to be dealt with there and finally the spines_count of
    #each instance of this class will be set to the spines_count that is passed in
    def __init__(self, name, spines_count):
        super().__init__(name)
        self.spines_count = spines_count

    #Here we are setting up the behaviour for what should happen when the instance of
    #this class makes a noise and in this case it snuffles
    def make_noise(self):
        return f"{self.name} snuffles!"

    #Here we are setting up the behaviour for what should happen when the instance of
    #this class defends itself and in this case it rolls up into a spiky ball
    def defend(self):
        return f"{self.name} curls up into a spiky ball"

    #Here we are setting up the behaviour for what should happen when the instance of
    #this class forages and in this case it searches for berries (to eat)
    def forage(self):
        return f"{self.name} searches for berries"

    #Here we are simply setting up the method get_spines_count which will enable
    #us to get any instance of this classe's spines_count
    def get_spines_count(self):
        return self.spines_count

#Here we are creating two instances of the animal class
#with the first being more specifically an isntance of the armadillo class which we are 
#passing in the name "Arlo" and the armor_level 5 into its constructor method and finally assigning 
#what is returned from this method to the variable we are declaring, armadillo.
#Are are doing the exactly the same for the second instance but in this situation it is an instance of
#the hedgehog class and we are passing in the name "Hedgy" and the spines_count 200 into the constructor method
# and assigning what is returned from this method to the variable we are declaring, hedgehog
armadillo = Armadillo("Arlo", armor_level=5)
hedgehog = Hedgehog("Hedgy", spines_count=200)

#Here we are outputting all the values returned from the methods for both of the instances we have created
print(armadillo.defend()) 
print(hedgehog.defend())
#For the next two example we have also used the name properties of each instance and outputed them
#as part of a larger string using string interpolation along with what is returned from an accessor methods
#that is specific to each of them
print(f"{armadillo.name} has armor level {armadillo.get_armor_level()}")
print(f"{hedgehog.name} has {hedgehog.get_spines_count()} spines")
print(armadillo.make_noise()) 
print(hedgehog.make_noise())  
print(armadillo.sleep())   
print(hedgehog.sleep()) 
print(armadillo.forage())   
print(hedgehog.forage()) 
