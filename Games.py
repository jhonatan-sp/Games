import Hangman
import Guessing_Game

def pick_game():
    print("*************************")
    print("***Pick your game!***")
    print("*************************")

    print("(1) Hangman (2) Guessing Game")

    game = int(input("Which game?"))

    if(game == 1):
        print("Playing Hangman")
        Hangman.play()
    elif(game == 2):
        print("Playing Guessing Game")
        Guessing_Game.play()

if(__name__ == "__main__"):
    pick_game()