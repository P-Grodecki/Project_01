"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    
    lower=1
    upper=10

    guess_attempts_record = 0
    
    play_again = True
    
    while play_again:
        
        correct_guess = False
        
        #Establish the Random Number to Guess
        rnd_num = random.randint(lower,upper)
        #Reset the number of Guess Attempts to Zero
        guess_attempts = 0
        
        #State the Current Record of Minimum Guesses, if not the first time playing.
        if guess_attempts_record != 0:
            print("\n\nWelcome back to the number guessing game.\nThe current number of guesses to beat is {}.\n".format(guess_attempts_record))
        else:
            print("Welcome to the Number Guessing Game!\n")
    
        
        while not correct_guess:
            #Increase the Guess Attempt Counter
            guess_attempts += 1
        
        
            valid_guess = False      
            while not valid_guess:
                user_guess = input("(Attempt #{}) Guess an Integer from {} to {}.  ".format(guess_attempts,lower,upper))
                try:
                    #Convert Entry to Integer
                    user_guess = int(user_guess)
                    if user_guess < lower or upper < user_guess:
                        raise ValueError
                
                except ValueError:
                    print("\nInvalid Guess Value of ""{}"". \n(Guess Value Must be Integer from {} to {}.)".format(user_guess,lower,upper))
                
                else:
                    #Exit the While Loop
                    valid_guess = True
            
            if user_guess == rnd_num:
                print("After {} attempts, your guess of {} was correct!".format(guess_attempts,user_guess))
                #Record the guess attempts if the number of attempts was less than the record
                if guess_attempts_record > guess_attempts or guess_attempts_record==0:
                    guess_attempts_record = guess_attempts
    
                #Set Correct Guess to True to Exit the Loop
                correct_guess = True
                
            elif user_guess < rnd_num:
                print("It's higher. Your Guess of {} was too low. Guess Again.".format(user_guess))
                
            elif user_guess > rnd_num:
                print("It's lower. Your Guess of {} was too high. Guess Again.".format(user_guess))
        
        
        #Ask the User if they would like to play again?
        correct_play_again_response = False
        while not correct_play_again_response:
            play_again_response = input("Would you like to play again? [y]Yes/[n]No ")
            if play_again_response.lower()=="y":
                play_again = True
                correct_play_again_response = True
            elif play_again_response.lower()=="n":
                correct_play_again_response = True
                play_again = False
            else:
                print("Your response to play again was invalid. Try again.")
                
    print("The game has Ended. Thank you for playing.")


# Kick off the program by calling the start_game function.
start_game()
