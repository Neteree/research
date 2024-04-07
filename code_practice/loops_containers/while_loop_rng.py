import math
import random

# This function takes a minimum and maximum number as user input that are integers and generates a number between them
# and returns it. The random number is inclusive of the minimum and maximum numbers
def rng():
    min_int = int(input("Enter the minimum integer that the random number can be:"))
    max_int = int(input("Enter the maximum integer that the random number can be:"))
    return random.randint(min_int, max_int)

#Will keepp looping until broken out of from within the body of the loop
while(True):
    #Generates the random number and stores it in random_number
    random_number = rng()
    #Ouputs a message and the random number that has been generated
    print("The random number that has been generated is:\n" + str(random_number))
    
    #Prompts the user to enter if they would like to continue or not and stores their answer in isContinuing
    isContinuing = input("Enter c if you would like to continue, or any other key to terminate:")
    #Breaks out of the loop unless the user has answered c/that they would like to continue
    if(isContinuing != "c"):
        break

#Outputs confirmation that the termination of the application was succesfull 
print("The application has succesfully terminated")
