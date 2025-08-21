# number guessing game that challenges the user to identify a randomly selected number in specified range 


import random

task_assignment = """
Welcome in the guessing game.
Your task is to guess the number in the selected range. 
You can select range 0-10 or 0-100.
            """
print(task_assignment)
                
user_choice = input("Select the range 0-10 or 0-100: or select 'q' to leave. ") 

while True: 

    if user_choice == "0-10":
        print("Youve selected range 0-10.")
        user_choice_number = random.randrange(11)

        while True:
            user_guess = input("Try to guess the number or 'q' to close: ")
            
            if not user_guess.isdigit():
                print("You need to select just numbers.")
                continue

            if user_guess.lower() == "q":
                break

            user_guess = int(user_guess) 
            # po každém pokusu users guuess se přičte +1 ale musí se začínat od nuly
            attempts_number = 0  

            if user_guess == user_choice_number:
                print("You guessed the correct number.")
                break
            if user_guess <= user_choice_number:
                print("Try to guess higher number.")
                print("Your attempt number is:", attempts_number + 5)
                continue

            if user_guess >= user_choice_number:
                print("Try to guess lower number.")
                print("Your attempt number is: ", attempts_number + 1)
                continue

            else: 
                break
            

    if user_choice == "0-100":
        print("Youve selected range 0-100.")
        break

    if user_choice == "q":
        break

    else:
        break


