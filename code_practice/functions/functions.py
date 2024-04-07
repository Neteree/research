#This function takes no arguments and simply returns "Hello world!" 
def greet_world():
  return "Hello world!"
#This function takes 3 numbers as arguments, adds them and returns the result
def add_three_numbers(num1, num2, num3):
    return num1 + num2 + num3
#This function takes 3 numbers as arguments, multiplies them and returns the result
def multiplies_three_numbers(num1, num2, num3):
    return num1 * num2 * num3
#Takes a range of integers and adds them all together    
def adds_integer_range(min_num, max_num):
    #delclares the local variable sum and intialises it with the value 0
    sum = 0
    #iterates over the range of integers and adds each one to sum (this is inclusive of max_num)
    for i in range(min_num, max_num + 1):
        sum += i
    #Returns the sum of all numbers in the range
    return sum
#Takes a range of integers and multiplies them all together    
def multiplies_integer_range(min_num, max_num):
    #delclares the local variable product and intialises it with the value 1
    product = 1
    #iterates over the range of integers and assigns the current product times the current
    # current integer to product (this is inclusive of max_num)
    for i in range(min_num, max_num + 1):
        product *= i
    #Returns the product of all numbers in the range
    return product    

#This function greet_custom takes the name of the person doing the greeting and the greeting itself as
#as arguments, concatenates them into a string and returns that string
#If arguments are not passed into this function the default arguments will be used instead
def greet_custom(greeter="Bob", greeting="Hello world!"):
    return greeter + ": " + greeting
    
#greet_world returns its greeting and it is output to the console
print(greet_world())
#add_three_numbers returns the sum of the three numbers passed in as arguments and it is output to the console
print(add_three_numbers(1,2,3))
#multiplies_three_numbers returns the product of the three numbers passed in as arguments and it is output to the console
print(multiplies_three_numbers(4,5,6))
#adds_integer_range returns the sum of all numbers from 1 to 10 inclusive and it is output it to the console
print(adds_integer_range(1, 10))
#_integer_range returns the product of all numbers from 1 to 10 inclusive and it is output it to the console
print(multiplies_integer_range(5, 9))
#greet_custom is passed in no arguments, so the default arguments are used instead and are returned as
#part of a concatenated string and this string is output to the console
print(greet_custom())
#greet_custom is passed one argument which is given to the parameter greeter, so the default argument is used
#for the parameter greeting and both arguments are returned as part of a concatenated string
#and this string is output to the console
print(greet_custom(greeter="Smith"))
#greet_custom is passed one argument which is given to the parameter greeting, so the default argument is used
#for the parameter greeter and both arguments are returned as part of a concatenated string and
#this string is output to the console
print(greet_custom(greeting="Kia ora!"))
#greet_custom is passed both arguments which are returned as part of a concatenated string and this string
#output to the console
print(greet_custom("John", "Goodbye!"))

