import random


def play():
    print_oppening_message()
    secret_word = load_secret_word()
    letters_hit = start_letters_hit(secret_word)
    print(letters_hit)

    hung = False
    right = False
    miss = 0

    print(letters_hit)

    while(not hung and not right):

        guess = ask_guess()

        if(guess in secret_word):
            keep_right_guess(guess, letters_hit, secret_word)
            print(letters_hit)
        else:
            miss += 1

            hung = miss == 6
            right = "_" not in letters_hit
            print(letters_hit)

    if(right):
        print_message_winner()
    else:
        print_message_loser()

def print_message_winner():
    print("You Win!!!")

def print_message_loser():
    print("You lose!!!")

def keep_right_guess(guess, letters_hit, secret_word):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            letters_hit[index] = letter
        index += 1

def ask_guess():
    guess = input("Which letter? ")
    guess = guess.strip().upper()
    return guess

def start_letters_hit(word):
    return ["_" for letter in word]

def print_oppening_message():

    print("*************************")
    print("***Welcome to Hangman!***")
    print("*************************")

def load_secret_word():

    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0,len(words))
    secret_word = words[number].upper()
    return secret_word

if(__name__ == "__main__"):
   play()