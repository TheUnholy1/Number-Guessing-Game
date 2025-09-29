import random

lowerBound = 1
upperBound = 10
maxAttempts = 10
currentAttempts = 0
numberToGuess = random.randint(lowerBound,upperBound)
gameRunning = True
gameContinue = False
exitCondition = True

print(f"Welcome To My Number Guessing Game where you would guess the number from {lowerBound} to {upperBound}."
      f"Goodluck!\nEnter zero to Exit")

def playerInput():
    global  currentAttempts
    try:
        playerGuess = int(input("Please Enter Your Guess: "))
        print(numberToGuess)
        currentAttempts +=1
        if playerGuess == 0:
            return False
        if playerGuess < lowerBound or playerGuess > upperBound:
            print(f'Please Enter a number within the range of {lowerBound} and {upperBound}')
            return None
        if playerGuess < numberToGuess:
            print('Too Low!')
        elif playerGuess > numberToGuess:
            print('Too High!')
        else:
            print(f"You are Correct! It is {numberToGuess}.You did it in {currentAttempts} attempts!")
            if playAgain():
                 return False
    except ValueError:
        print('Invalid Input')

def playAgain():
    global numberToGuess
    while True:
        try:
            continuePlaying = input('Do you want to play again? Y/N: ')
            if continuePlaying.upper() == 'Y' or continuePlaying.upper() == 'N':
                if continuePlaying.upper() == 'Y':
                    numberToGuess = random.randint(lowerBound, upperBound)
                    return False
                else:
                    return True
            else:
                print("Please Enter Y or N only")
        except ValueError:
            print("Please enter Y or N only!")


def main():
    global exitCondition
    while gameRunning:
       exitCondition = playerInput()
       if exitCondition == False:
         print("Exiting The Game....")
         break
if __name__ == "__main__":
    main()
