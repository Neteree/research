#Declares a list and initialises it with some abitrary values
my_list = ["a", "b", "c", "d"]
#Declares a list and initialises it with some abitrary key-value pairs
my_dictionary = {"bob": 1, "smith": 2}

#This is a function that tries to return a quotient
def divide(numerator, denominator):
    #Tries to return the quotient
    try:
        return numerator / denominator
    #When a zero division error occurrs a custom error message will be returned
    except ZeroDivisionError:
        message = "You can not divide another number by zero"
        return message
    #When a type error occurrs a custom error message will be returned
    except TypeError:
        message = "A type error has occurred"
        return message
    #If a different error occurrs the error object will be returned
    except Exception as error:
        return error

#This is a function that tries to get an element by a given index       
def get_by_index(index):
    #Tries to return an element by a given index
    try:
        return my_list[index]
    #When a index error occurrs a custom error message will be returned
    except IndexError:
        message = "You can not access by an index that is out of range"
        return message
    #If a different error occurrs the error object will be returned
    except Exception as error:
        return error

#This is a function that tries to get an element by a given key          
def get_by_key(key):
    #Tries to return an element by a given key
    try:
        return my_dictionary[key]
    #When a key error occurrs a custom error message will be returned
    except KeyError:
        message = "You can not access by a key that does not exist"
        return message
    #If a different error occurrs the error object will be returned
    except Exception as error:
        return error
        
#This function takes a boolean is_name_defined and if true this function should return the defined variable name
#otherise it should return the undefined variable name
def get_name_if_defined(is_name_defined):
    #Tries to return the variable name
    try:
        #If is_name_defined is true then name will be defined and return without issue
        if(is_name_defined):
            name = "Bob"
            return name
            #If is_name_defined is False then name will not be defined and returning it will cause 
            # a name error to occurr
        return name
    except NameError:
        return "name is not defined"
    #If a different error occurrs the error object will be returned
    except Exception as error:
        return error

#Here is a bunch of print statements that I used to test positive and negative test cases for the functions
#that I wrote above
print(divide(15, 2))
print(divide(5, 8))
print(divide(7, "a"))
print(divide(7, "a"))
print(divide(5, 0))
print(divide(7, "a"))
print(divide(7, None))
print(divide(13, 0))
print(get_by_index(7))
print(get_by_index(-14))
print(get_by_index(0))
print(get_by_index(2))
print(get_by_key("apple"))
print(get_by_key("pie"))
print(get_by_key("bob"))
print(get_by_key("smith"))
print(get_name_if_defined(True))
print(get_name_if_defined(" "))
print(get_name_if_defined(False))
print(get_name_if_defined(""))
