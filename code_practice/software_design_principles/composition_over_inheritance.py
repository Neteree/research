#Here we have created the eyes class that will allow us to create instances of it that
#have an eye_amount property and look method
class Eyes:
    def __init__(self, eye_amount):
        self.eye_amount = eye_amount
    
    def look(self):
        return f"uses their {self.eye_amount} eyes to look around"

#Here we have created the arms class that will allow us to create instances of it that
#have an arm_amount property and swing method
class Arms:
    def __init__(self, arm_amount):
        self.arm_amount = arm_amount
    
    def swing(self):
        return f"swings their {self.arm_amount} arms around"
      
#Here we have created the legs class that will allow us to create instances of it that
#have an leg_amount property and walk method  
class Legs:
    def __init__(self, leg_amount):
        self.leg_amount = leg_amount
    
    def walk(self):
        return f"walks around with their {self.leg_amount} legs"
      
#Here we have created the spikes class that will allow us to create instances of it that
#have an spike_amount property and shoot method    
class Spikes:
    def __init__(self, spike_amount):
        self.spike_amount = spike_amount
    
    def shoot(self):
        return f"shoots their {self.spike_amount} spikes at unsuspecting victims"
        
#Here is our first example of composition where we write a class for building a Hedgehog
#out of eyes, legs and spikes and arguements we pass through the constructor method.
#We then use the methods of eyes, legs and spikes to easily implement the attack method
class Hedgehog:
    def __init__(self, eye_amount, leg_amount, spike_amount):
        self.eyes = Eyes(eye_amount)
        self.legs = Legs(leg_amount)
        self.spikes = Spikes(spike_amount)
        
    def attack(self):
        return f"The hedgehog {self.legs.walk()} and {self.eyes.look()} to {self.spikes.shoot()}"
        
#Here is our second example of composition where we write a class for building a Human
#out of eyes, legs and arms and arguements we pass through the constructor method.
#We then use the methods of eyes, legs and arms to easily implement the explore method
class Human:
    def __init__(self, eye_amount, leg_amount, arm_amount):
        self.eyes = Eyes(eye_amount)
        self.legs = Legs(leg_amount)
        self.arms = Arms(arm_amount)
        
    def explore(self):
        return f"The human {self.legs.walk()}, {self.eyes.look()} and {self.arms.swing()}"
    
#Here we create a hedgehog with 2 eyes, 4 legs and 1000 spikes
the_hedgehog = Hedgehog(2, 4, 1000)
#Here we create a hedgehog with 2 eyes, 2 legs and 2 legs
the_human = Human(2, 2, 2)

#Here we output the result of the_hedgehog's attack
print(the_hedgehog.attack())
#Here we output the result of the_human's attack
print(the_human.explore())

#Here we have used the composition over inheritance principle and by doing so we 
#have allowed ourselves to avoid issues like multiple inheritance, seen that once we
#have built a few of the components like eyes and legs for example we can reuse them easily,
#that we can easily compose new methods out of our components and avoid unessarily large classes 
#like we often have when going with inheritance. One final thing is that when I am building
#code using composition over using inheritance it is much easier to reason about when them
#codebase starts getting into thousands of lines of code
