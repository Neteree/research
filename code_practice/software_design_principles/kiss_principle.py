#Here are the name, colour, quill_amount and is_cute variable
#that were are declaring for our hedgehog 

name = "Spike"
colour = "brown"
quill_amount = 500
is_cute = True

#Here we are displaying the information that we have stored in the variables
#related to the hedgehog and using the is_cute to choose between 1 of 2 potential
#outputs
print(f"Meet {name}, the {color} hedgehog!")
print(f"{name} has approximately {quills} quills")
if is_cute:
    print(f"{name} is undeniably cute! 🥰")
else:
    print(f"{name} might be a bit prickly, but still lovable!")

#Here we have adhered to the kiss principle by keeping the code simple and straightforward.
#Were are just storing some information/data about a hedgehog and displaying/outputting it
