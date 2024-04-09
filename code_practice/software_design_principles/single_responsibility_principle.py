#The single responsibility of Hedgehog class is for representing instances of it by their name, 
#colour and age properties
class Hedgehog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        
#This clas was split out from the Hedgehog class in order for both classes to follow
#the single responsibility princible and this classes single responsibility is very 
# simply for managing the hedgehog collections/groups
class HedgehogDatabase:
    #Here for the constructor we have one property that is a list data structure
    #which every instance of the HedgehogDatabase class will use to store 
    #the instances of the Hedgehog class
    def __init__(self):
        self.hedgehogs = []

    #The method add_hedgehog does as the name suggests, adds a hedgehog to
    #an instance of the HedgehogDatabase
    def add_hedgehog(self, hedgehog):
        #Here is the code for appending/adding a hedgehog to an instance of
        #the HedgehogDatabase
        self.hedgehogs.append(hedgehog)
        #All though not needed here I am returning a helpful message so you have
        #confirmation that the hedgehog has been added to the database
        return f"{hedgehog.name} added to the database"

    #This method is simply for getting a hedgehog that has been stored in the 
    #database by its name
    def get_hedgehog_by_name(self, name):
        #When an iinstance of the Hedgehog class is found within an instance
        #HedgehogDatabase class with the same name as the age provided to the get_hedgehog_by_name
        #method return that hedgehog object and otherwise return a string saying
        #there was no hedgehog found in the database with that name
        for hedgehog in self.hedgehogs:
            if hedgehog.name == name:
                return hedgehog
        return f"No hedgehog found with the name {name} in the database"

    #This method is simply for getting a hedgehog that has been stored in the 
    #database by its age
    def get_hedgehog_by_age(self, age):
        #When an instance of the Hedgehog class is found within an instance
        #HedgehogDatabase class with the same age as the age provided to the get_hedgehog_by_age
        #method return that hedgehog object and otherwise return a string saying
        #there was no hedgehog found in the database with that age
        for hedgehog in self.hedgehogs:
            if hedgehog.age == age:
                return hedgehog
        return f"No hedgehog found with the age {age} in the database"

#Instantiates hedgehog1 and gives it a name color and age via the constructor 
hedgehog1 = Hedgehog("Spike", "Brown", 3)
#Instantiates hedgehog2 and gives it a name color and age via the constructor
hedgehog2 = Hedgehog("Prickles", "Gray", 4)

#Creates an HedgehogDatabase object and stores it in database
database = HedgehogDatabase()
#Adds hedgehog1 to database
database.add_hedgehog(hedgehog1)
#Adds hedgehog2 to database
database.add_hedgehog(hedgehog2)

#Outputs the hedgehog object that you have retrieved from the hedgehog database by
#its name "Spike"
print(database.get_hedgehog_by_name("Spike"))
#Outputs the hedgehog object that you have retrieved from the hedgehog database by
#its age 4
print(database.get_hedgehog_by_age(4))
