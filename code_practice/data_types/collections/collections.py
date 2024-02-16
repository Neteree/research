# A list of fast foods that are represented by strings
fast_foods = ["pizza", "cheeseburger", "fried chicken", "fries"]
# A list containing the fibinacci numbers (integers) starting from 0 inclusive and ending at 89 inclusive
fibinacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Declared and initialised pi
pi = 3.1415
# Declared and initialised e
e = 2.718
# Declared and initialised golden_ratio
golden_ratio = 1.618
# A list of floats (famous decimals in math's)
famous_decimals = [pi, e, golden_ratio]
# A tuple containing the integers 0 and 1
bits = (0, 1)
# A tuple containing the booleans True and False
states = (True, False)
# A tuple containing 4 countries
country_names = ("New Zealand", "Korea", "Japan", "Brazil")
# A dictionary called workers with keys for their names and values for their professions
workers = {"Bob": "Electrician", "Smith": "CEO", "Ada": "Software Developer"}
# A dictionary called items items_for_sale which uses the names of the items as keys and prices as values
items_for_sale = {"Coffee Mug": 9.99, "Black T": 24.00, "Steak Knife": 53.75}
# A dictionary called movie_ratings with movie names as the keys and corresponing ratings as values
movie_ratings = {"LOTR": 8, "Harry Potter": 7, "Pirates of the Caribbean": 9}

# Outputs the value of the list fast_foods at index 0
print(fast_foods[0])
# Outputs the value of the list fibinacci_numbers at index 1
print(fibinacci_numbers[1])
# Outputs value of the list famous_decimals at index 2
print(famous_decimals[2])
# Outputs the  value of the list famous_decimals at the last index which is index 2
print(famous_decimals[-1])
# Outputs True because the first value of the tuple is zero
print(bits[0] + bits[1] == bits[1])
# states[0] evaluates to True but states[1] evaluates to False so True and False evaluates to False which is outputted with print
print(states[0] and states[1])
# Outputs False because country_names[3] and country_names[-1] both refer the value at the end of the tuple 
print(country_names[3] != country_names[-1])
# Outputs the proffesions of Smith
print(workers["Smith"])
# Outputs the proffesions of Ada
print(workers["Ada"])
# Outputs the total for all items if you were to buy one of each, rounded
print(round(items_for_sale["Coffee Mug"] + items_for_sale["Black T"] + items_for_sale["Steak Knife"]))
# Outputs False because Lord of the Rings did not receive a higher rating than Pirates of the Caribbean
print(movie_ratings["LOTR"] > movie_ratings["Pirates of the Caribbean"])
# Outputs True because Harry Potter did not receive a higher rating than Pirates of the Caribbean
print(movie_ratings["Harry Potter"] < movie_ratings["Pirates of the Caribbean"])
# Outputs False because Harry Potter did not receive the same rating as LOTR
print(movie_ratings["Harry Potter"] == movie_ratings["LOTR"])
