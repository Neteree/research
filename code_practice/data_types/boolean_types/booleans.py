# Imports the random module
import random
 
# Declares the variable is_greater_than and initialises it with 2 > 1 which evaluates to True
is_greater_than = 2 > 1
# Outputs the value of is_greater_than which is True
print(is_greater_than)

# Reassigns is is_greater_than with 1 > 1 which evaluates to False
is_greater_than = 1 > 1
# Outputs the value of is_greater_than which is False
print(is_greater_than)

# Declares and initialises is_less_than with 1 < 2 which evaluates to True
is_less_than = 1 < 2
# Outputs the value of is_less_than which is True
print(is_less_than)

# Reassigns is is_less_than with 1 < 1 which evaluates to False
is_less_than = 1 < 1
# Outputs the value of is_less_than which is False
print(is_less_than)

# Declares and initialises is_equal_to with 1 == 1 which evaluates to True
is_equal_to = 1 == 1
# Outputs the value of is_equal_to which is True
print(is_equal_to)

# Reassigns is_equal_to with 1 == 2 which evaluates to False
is_equal_to = 1 == 2
# Outputs the value of is_equal_to which is False
print(is_equal_to)

# Declares and initialises is_less_than with 2 >= 1 which evaluates to True
is_greater_or_equal_to = 2 >= 1
# Outputs the value of is_greater_or_equal_to which is True
print(is_greater_or_equal_to)

# Reassigns is_greater_or_equal_to with 1 >= 1 which evaluates to True
is_greater_or_equal_to = 1 >= 1
# Outputs the value of is_greater_or_equal_to which is True
print(is_greater_or_equal_to)

# Reassigns is_greater_or_equal_to with 1 >= 2 which evaluates to False
is_greater_or_equal_to = 1 >= 2
# Outputs the value of is_greater_or_equal_to which is False
print(is_greater_or_equal_to)

# Declares and initialises is_less_than with 1 <= 2 which evaluates to True
is_less_or_equal_to = 1 <= 2
# Outputs the value of is_less_or_equal_to which is True
print(is_less_or_equal_to)

# Reassigns is_greater_or_equal_to with 1 <= 1 which evaluates to True
is_less_or_equal_to = 1 <= 1
# Outputs the value of is_less_or_equal_to which is True
print(is_less_or_equal_to)

# Reassigns is_greater_or_equal_to with 2 <= 1 which evaluates to False
is_less_or_equal_to = 2 <= 1
# Outputs the value of is_less_or_equal_to which is False
print(is_less_or_equal_to)

# Declares the variable isTrue and initialises it with True and True which evaluates to true
isTrue = True and True
# Outputs the value of isTrue which is True
print(isTrue)

# Reassigns the variable isTrue to True and False which evaluates to False
isTrue = True and False
# Outputs the value of isTrue which is False
print(isTrue)

# Reassigns the variable isTrue to False and True which evaluates to False
isTrue = False and True
# Outputs the value of isTrue which is False
print(isTrue)

# Reassigns the variable isTrue to False and False which evaluates to False
isTrue = False and False
# Outputs the value of isTrue which is False
print(isTrue)

# Reassigns the variable isTrue to True or True which evaluates to True
isTrue = True or True
# Outputs the value of isTrue which is True
print(isTrue)

# Reassigns the variable isTrue to True or False which evaluates to True
isTrue = True or False
# Outputs the value of isTrue which is True
print(isTrue)

# Reassigns the variable isTrue to False or True which evaluates to True
isTrue = False or True
# Outputs the value of isTrue which is True
print(isTrue)

# Reassigns the variable isTrue to False or False which evaluates to False
isTrue = False or False
# Outputs the value of isTrue which is False
print(isTrue)

# Declares the variable is_alive and initialises with False if the random Integer is 0 and True if 1  
is_alive = bool(random.randint(0, 1))
# Outputs the value that is stored in is_alive that is True if the random integer that was converted from 1 and False if it was converted from 2
print(is_alive)

# Outputs "You are alive" if is_alive has evaluated to true and "You are not alive" otherwise
if is_alive:
    print("You are alive")
else:
    print("You are not alive")
