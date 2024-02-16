# 42 is casted from an integer to a string and stored in the variable the_answer
the_answer = str(42)
# 3.1415 is casted from a string to a float and stored in the variable pi
pi = float("3.1415")
# 11.5 is casted from a float to an integer and stored in the variable people_amount
people_amount = int(11.5)
# 176 is casted from a string to a float to an integer and stored in the variable height
height = int(float("176"))
# 11.22 is casted from a float to an integer to a string and stored in the variable character_name
character_name = str(int(11.22))
# 2 is casted from an integer to a string to a float and stored in the variable version
version = float(str(2))

# The string value of the variable the_answer is "42" so 42 is outputted
print(the_answer)
# The float value of the variable pi is 3.1415 so 3.1415 is outputted
print(pi)
# The integer value of the variable people_amount is 11 so 11 is outputted
print(people_amount)
# The integer value of the variable height is 176 so 176 is outputted
print(height)
# The string value of the variable character_name is "11" so 11 is outputted
print(character_name)
# The float value of the variable version is 2.0 so 2.0 is outputted
print(version)
# Casts each number to its corresponding character and concatenates them into the string "Hello, World!" which is then outputed
print(chr(72) + chr(101) + chr(108) + chr(108) + chr(111) + chr(44) + chr(32) + chr(87) + chr(111) + chr(114) + chr(108) + chr(100) + chr(33))
# Casts each character to its corresponding number, adds them and then outputs the sum
print(ord("H") + ord("e") + ord("l") + ord("l") + ord("l") + ord("o") + ord(",") + ord(" ") + ord("W") + ord("o") + ord("r") + ord("l") + ord("d") + ord("!"))
