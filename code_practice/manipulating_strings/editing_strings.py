#Declares the variable full_name_one and initialises it with the string literal "Cameron Belcher"
full_name_one = "Cameron Belcher"
#Declares the variable full_name_one and initialises it with the string literal "John Doe"
full_name_two = "john doe"
#Declares unstripped_string and initialises it with "\n bob\n "
unstripped_string = "\n bob\n "


#Replaces Cameron with Bob in full_name_one
full_name_one = full_name_one.replace("Cameron", "Bob")
#Ouputs the new value "Bob Belcher" for full_name_one
print(full_name_one)
#Replaces Doe with Smith in full_name_two
full_name_two = full_name_two.replace("doe", "smith")
#Ouputs the new value "john smith" for full_name_two
print(full_name_two)

#Ouputs full_name_one in upper case
print(full_name_one.upper())
#Ouputs full_name_two in upper case
print(full_name_two.upper())
#Ouputs full_name_one in lower case
print(full_name_one.lower())
#Ouputs full_name_two in lower case
print(full_name_two.lower())
#Ouputs full_name_one in title case
print(full_name_one.title())
#Ouputs full_name_two in lower case
print(full_name_two.title())
#Ouputs full_name_one in capital case
print(full_name_one.capitalize())
#Ouputs full_name_two in capital case
print(full_name_two.capitalize())
#Ouputs full_name_one with the cases swapped
print(full_name_one.swapcase())
#Ouputs full_name_two with the cases swapped
print(full_name_two.swapcase())
#Ouputs full_name_one but reversed with hyphens between each character
print("-".join(reversed(full_name_one)))
#Ouputs full_name_two but reversed with dollar signs between each character
print("$".join(reversed(full_name_one)))
#Outputs "bob"
print(unstripped_string.strip())
#Outputs "bob\n "
print(unstripped_string.lstrip())
#Outputs "\n bob"
print(unstripped_string.rstrip())
