#Declares integer_list and initialises it with a list of integers
integer_list = [12, 34, 22, 54, 93]
#Declares string_list and initialises it with a list of strings
string_list = ["Hello", "World", "!"]
#Declares bool_list and asigns it a list of integers
bool_list = [True, False, False, True, True]
#Declares integer_tuple and initialises it with a tuple of integers
integer_tuple = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
#Declares string_tuple and initialises it with a tuple of strings
string_tuple = ("a", "b", "c", "d", "e", "f", "g")
#Declares bool_tuple and asigns it a tuple of integers
bool_tuple = (False, True, False, True)
#Declares bank_numbers_dictionary with string keys representing the names corresponding the number values 
bank_numbers_dictionary = {"Adam": 12345678910, "Smith": 4128949821894, "John": 951529049109}

#Interates over the list of integers, printing out each one
for integer in integer_list:
    print(integer)
    
#Interates over the list of strings, printing out each one
for string in string_list:
    print(integer)
    
#Interates over the list of bools, printing out each one
for boolean in bool_list:
    print(integer)
    
#Interates over the tuple of integers, printing out each one
for integer in integer_tuple:
    print(integer)
    
#Interates over the tuple of strings, printing out each one
for string in string_tuple:
    print(integer)
    
#Interates over the tuple of bools, printing out each one
for bools in bool_tuple:
    print(integer)
    
#Interates over bank_numbers_dictionary, printing out each key
for key in bank_numbers_dictionary:
    print(key)
    
#Interates over bank_numbers_dictionary, printing out each value
for key in bank_numbers_dictionary:
    print(bank_numbers_dictionary[key])

#Interates over bank_numbers_dictionary, printing out each key and value pair
for key in bank_numbers_dictionary:
    print(key, bank_numbers_dictionary[key])

#Outputs the timestables from 1 to 12
for i in range(13):
    for j in range(13):
        print(i, "*", j, "=", i * j)
