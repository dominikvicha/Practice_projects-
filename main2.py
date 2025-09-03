"""
WORD GUESSING GAME 
- user has to guess the caharcters in a randomly selected word by PC 
- programm provides feedback after each guess
- list of 12 words are prepared before the start of the game 
- welcome the user by sain HI with the name 

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

https://www.geeksforgeeks.org/python/python-program-for-word-guessing-game/   
"""

import random 

name = input("What is your name?")
print(
    f"Hello {name} \n" 
    f"Wish you good luck!\n"   
)