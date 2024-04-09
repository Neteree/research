#Here were are creating a list hedgehogs which we will be using to store
#our hedgehog objects
hedgehogs = []

#Here were are creating the Hedgehog clase which we will be using to instantiate Hedgehog
#objects that have name and age properties
class Hedgehog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Here we are following the dry principle by not writing a line for every Hedgehog 
#that we append to the hedgehogs list and also not writing a line of code for every
#time we need to print the name and age of each hedgehog.
#Also for each hedgehog we are using i to give them each individual names, meaning
#this is also following the dry principle because we don't have to keep rewriting code
#to specify what the name and age should be.
#This has resulted in a fraction of the code that we would have had to write otherwise
for i in range(1000):
    hedgehogs.append(Hedgehog(f"hedgehog_{i}", i + 1))
    print(f"{hedgehogs[i].name} is {hedgehogs[i].age} years old")
