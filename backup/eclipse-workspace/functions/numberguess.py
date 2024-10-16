from random import *

def number_guessing_game():
    num = randint(1,100)
    
    print("Welcome to Number Guessing Game")
    
    guess = None
    
    while guess!=num:
            guess = int(input("Enter your guess: "))        
            if guess<num:
                print("Too low. Try again!")
            elif guess>num:
                print("Too high .. try again!")
            else:
                print("Congrats..") 
           
number_guessing_game()           