# Sets the initial value of actual_answer_to_life to 42
actual_answer_to_life = 42
# Sets the initial value of backwards_actual_answer_to_life to 24
backwards_actual_answer_to_life = 24;
# Promts the user to enter the initial value for user_answer_to_life and will be stored if it can be casted to an integer 
user_answer_to_life = int(input("What is the answer to life? "))
# Sets the initial values of secret_actual_answers_to_life to the first 5 prime numbers
secret_actual_answers_to_life = [1, 3, 5, 7, 11]

# If the user has input one of the correct answers they will get confirmation otherwise will be told to leave
if user_answer_to_life == actual_answer_to_life:
    # Outputs the confirmation that you have got the right answer 42
    print("Yes! the answer to life is " + str(actual_answer_to_life) + "!")
elif user_answer_to_life == backwards_actual_answer_to_life:
    # Outputs the confirmation that you have got the right answer but backwards
    print("Your answer " + str(backwards_actual_answer_to_life) + " is backwards!")
elif user_answer_to_life == secret_actual_answers_to_life[0]:
    # Outputs the confirmation that you have got the first secret answer
    print("Your answer " + str(secret_actual_answers_to_life[0]) + " is the first secret answer to life")
elif user_answer_to_life == secret_actual_answers_to_life[1]:
    # Outputs the confirmation that you have got the second secret answer
    print("Your answer " + str(secret_actual_answers_to_life[1]) + " is the second secret answer to life")
elif user_answer_to_life == secret_actual_answers_to_life[2]:
    # Outputs the confirmation that you have got the third secret answer
    print("Your answer " + str(secret_actual_answers_to_life[2]) + " is the third secret answer to life")
elif user_answer_to_life == secret_actual_answers_to_life[3]:
    # Outputs the confirmation that you have got the fourth secret answer
    print("Your answer " + secret_actual_answers_to_life[3] + " is the fourth secret answer to life")
elif user_answer_to_life == secret_actual_answers_to_life[4]:
    # Outputs the confirmation that you have got the last of the secret answers
    print("Your answer " + str(secret_actual_answers_to_life[4]) + " is the last secret answer to life")
else:
    # Outputs that confirmation that you have not got any of the possible answer and you should leave
    print("That is not a correct answer! Please leave!")
