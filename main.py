# number guessing game that challenges the user to identify a randomly selected number in specified range 


import random

task_assignment = """
Welcome in the guessing game.
Your task is to guess the number in the selected range. 
You can select range 0-10 or 0-100.
            """
print(task_assignment)
                
user_choice = input("Select the range 0-10 or 0-100 or select 'q' to leave: ") 

def user_choice1(): # chybí podmínka ve které bude uživatel upozorněn na to že zvolil číslo mimo range. 


    if user_choice == "0-10":
        print("Youve selected range 0-10.")
        user_choice_number = random.randrange(11)
        attempts_number = 0  
            
        while True:
            user_guess = input("Try to guess the number or 'q' to close:")

            if user_guess.lower() == "q":
                return
                
            if not user_guess.isdigit():
                print("You need to select just independent integer number.")
                continue

            user_guess = int(user_guess) 
            attempts_number += 1  
                
            if user_guess == user_choice_number:
                print("You guessed the correct number. ")
                return

            elif user_guess < user_choice_number:
                print("Wrong. Try to guess higher number.")
                print("Your attempt number is:", attempts_number)
                
            else: # user_guess > user_choice_number
                print("Wrong. Try to guess lower number.")
                print("Your attempt number is:", attempts_number)

def main():

    while True:

        user_choice = input("Select the range 0-10 or 0-100 or 'q' to leave.")

        if user_choice == "0-10":
            user_choice1()
        elif user_choice == "0-100":
            break
        elif user_choice == "q":
            print("Leaving the game.")
            break
        else:
            print("Invalid chocie. Please type 0-10, 0-100 or q.")

if __name__ == "__main__":
    main()

                



"""
1. problem: 

while True: (outer loop)
    if user_choice == "0-10":
    
    while True: (inner loop for guesses)
        user_guess = input... 

- outer loop = keep game running forever
- inner loop = keep asking guesses forever


2. the q button

- typing q ould break out of the inner loop only
- but i was still inside the outer loop (while True at the top)
- thats why the q doesnt work 

3. differnce BREAK and RETURN

- break stop the loop but stay inside the function. Function keep going.

- return stops the function (and everything inside, including loops)
    - control goes where the function was called (no matter how many loops are there.)






"""







"""
while True: 

    if user_choice == "0-10":
        print("Youve selected range 0-10.")
        user_choice_number = random.randrange(11)
        attempts_number = 0  

        while True:
            user_guess = input("Try to guess the number or 'q' to close: ")
            
            if not user_guess.isdigit():
                print("You need to select just independent integer number.")
                continue

            if user_guess.lower() == "q":
                break

            user_guess = int(user_guess) 
            attempts_number += 1  
            
            if user_guess == user_choice_number:
                print("You guessed the correct number. ")
                break
            if user_guess <= user_choice_number:
                print("Try to guess higher number.")
                print("Your attempt number is:", attempts_number)
                continue

            if user_guess >= user_choice_number:
                print("Try to guess lower number.")
                print("Your attempt number is: ", attempts_number)
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


"""

