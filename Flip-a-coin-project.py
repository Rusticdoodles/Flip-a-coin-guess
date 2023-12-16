#User story 1: As a user I want to be able to guess the outcome of a random coin flip (heads/tails)
#User story 2: As a user I want to clearly see the result of the coin flip
#User story 3: As a user I want to clearly see whether or not I guessed correctly
#User story 1 challenge: As a user I want to clearly see the updated guess history (correct count/total count)
#User story 1 challenge: As a user I want to be able to quit the game or go again after each cycle

import random

#Guess history
guess_history = [ ]

#Coin toss function
def main(): 

    print("A coin has been flipped! What side does it show?")
    
#Coin Flip, 1 = Heads, 2 = Tails
    coin_flip = random.randint(1, 2)

#User guess input
    guess = input("Enter your guess (Heads or Tails):")
    print("You guessed, " + guess) 


#Determining if guess is correct or not
    if coin_flip == 1 and guess == "Heads":
        print("Correct!, the side was Heads!")
    elif coin_flip == 2 and guess == "Tails":
        print("Correct!, the side was Tails!")
    elif coin_flip != 1 and guess == "Heads":
        print("Incorrect, the side was Tails")
    elif coin_flip != 2 and guess == "Tails":
        print("Incorrect, the side was Heads")
    else:
        print("Please input either Heads or Tails.")
        main()

#Quit game or go again and printing guess history

    answer = input("Thank you for guessing! Do you want to try again? (Yes/No):")
    if "No" in answer:
        print("Thank you for playing!")
        guess_history.append(guess)
        print ("Guess history:", guess_history)
        return 
    elif "Yes" in answer:
        guess_history.append(guess)
        print("Guess history:", guess_history)
        main()

#Calling the coin toss function
main()