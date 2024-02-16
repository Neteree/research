# Prompts the user to enter their username and stores the string value in user_name
user_name = input("Please enter your user name: ")
# Prompts the user to enter their email and stores the string value in email
email = input("Please enter your email: ")
# Prompts the user to enter their phone number and if can be casted to an integer it is stored in phone
phone = int(input("Please enter your phone number: "))
# Prompts the user to enter their height in centimeters and if it can be casted to an integer it is stored in height
height = int(input("Please enter your height in centimeters: "))
# Prompts the user to enter their favourite number and if it can be casted to a float then it is stored in favourite_number
favourite_number = float(input("Please enter your favourite number: "))
# Prompts the user to enter their least favourite number and if it can be casted to a float then it is stored in least_favourite_number
least_favourite_number = float(input("Please enter your least favourite number: "))
# Prompts the user to enter a value that can be cast to an integer then then a boolean and stores it in is_answer_to_life
is_answer_to_life = bool(int(input("Enter 0 if the answer to life is not 42 and any other integer otherwise")))
# Prompts the user to enter a value that can be cast to an integer then then a boolean and stores it in is_cat_person
is_cat_person = bool(int(input("Enter 0 if you're not a cat person and any other integer otherwise")))

# Outputs "Your username is: (user_name)"
print("Your username is:", user_name)
# Outputs "Your email is: (email)"
print("Your email is:", email)
# Outputs "Your phone number is: (phone)"
print("Your phone number is:", phone)
# Outputs "Your height in centimeters is: (height)"
print("Your least favourite number is:", height)
# Outputs "Your favourite number is: (favourite_number)"
print("Your favourite number is:", favourite_number)
# Outputs "Your least favourite number is: (least_favourite_number)"
print("Your least favourite number is:", least_favourite_number)
# Outputs "The answer to life is 42: (is_answer_to_life)"
print("The answer to life is 42:", is_answer_to_life)
# Outputs "You are a cat person: (is_cat_person)"
print("You are a cat person:", is_cat_person)
