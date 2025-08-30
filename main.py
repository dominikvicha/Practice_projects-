# number guessing game that challenges the user to identify a randomly selected number in specified range 


import random

task_assignment = """
Welcome in the guessing game.
Your task is to guess the number in the selected range. 
You can select range 0-10 or 0-100.
            """
print(task_assignment)
                 

def user_choice1(user_choice): 


    if user_choice == "0-10":
        print("Youve selected range 0-10.")
        user_choice_number = random.randrange(11)
        attempts_number = 0
            
        while True:
            user_guess = input("Try to guess the number."
            "Or 'q' to exit Guessing game to choose the new range. " 
            "Or 'qq' to leave the programm.")

            if user_guess.lower() == "q":       #exiting the guessing game 
                return
            
            if user_guess.lower() == "qq":
                return "quit"                   #program exits completly (stop the guessing game, sending the messege "quit" back to the main() -> then main reads that..)
                
            if not user_guess.isdigit():
                print("You need to select just independent integer number.")
                continue

            user_guess = int(user_guess) 
            attempts_number += 1  
                
            if user_guess == user_choice_number:
                print("You guessed the correct number.")
                print("Your score is:", attempts_number)
                return

            elif user_guess < user_choice_number:
                print("Wrong. Try to guess higher number.")
                print("Your attempt number is:", attempts_number)
                
            else: # user_guess > user_choice_number
                print("Wrong. Try to guess lower number.")
                print("Your attempt number is:", attempts_number)

def main():

    while True:

        user_choice = input("Select the range 0-10 or 0-100 or 'quit' to leave.")
      

        if user_choice == "0-10":
            #user_choice1(user_choice)                  #if i dont want to shut down the programm after i select the range. 
            result = user_choice1(user_choice)
            if result == "quit":
                print("Leaving the game...")
                break
        elif user_choice == "0-100":
            break
        elif user_choice == "quit":
            print("Leaving the game.")
            break
        
        else:
            print("Invalid choice. Please type 0-10, 0-100 or 'quit'.")
    

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

3. ADD exit() 
- function is good but: 
    - ends program, even if theres clieanup or other code to run later 
    - example - adding another range it wouldnt work. 

if user_guess.lower() == "qq":
                exit()  


4. LOGIC BEHIND return "quit" 
- in case you dont want to go back where the function is called
- inside the while loop i can shut down the program 


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

