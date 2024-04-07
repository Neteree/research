string_one = "alphabetical"
string_two = ".,././"
string_three = "3"
string_four = "Hello World"
string_five = "HELLO WORLD"
string_six = " "

#Outputs the number of a's countained in string_one
print(string_one.count("a"))
#Outputs the number of l's countained in string_one
print(string_one.count("l"))
#Outputs the number of t's countained in string_one
print(string_one.count("t"))
#Outputs the number of e's countained in string_one
print(string_one.count("e"))
#Outputs the number of r's countained in string_one
print(string_one.count("r"))
#Outputs the index where alpha starts in string_one
print(string_one.find("alpha"))
#Ouputs -1 because string_one does not contain "apple"
print(string_one.find("apple"))
#Outputs if string_one is alphanumeric
print(string_one.isalnum())
#Outputs if string_two is alphanumeric
print(string_two.isalnum())
#Outputs if string_one is alphabetical
print(string_one.isalpha())
#Outputs if string_two is alphabetical
print(string_two.isalpha())
#Ouputs if string_one is a digit
print(string_one.isdigit())
#Ouputs if string_three is a digit
print(string_three.isdigit())
#Outputs if string_one is in title case
print(string_one.istitle()) 
#Outputs if string_four is in title case
print(string_four.istitle())        
#Outputs if string_one is in upper case
print(string_one.isupper()) 
#Outputs if string_four is in upper case
print(string_five.isupper())          
#Outputs if string_one is in lower case
print(string_one.islower()) 
#Outputs if string_four is in lower case
print(string_five.islower())  
#Outputs if string_one is a space
print(string_one.isspace())   
#Outputs if string_six is a space
print(string_six.isspace())
