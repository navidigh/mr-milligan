import random
guesses = 0
number = random.randint(1, 101)

while guesses < 10:
    guesskyume = int(input("I am well, thinking of a number. a number that happens to be in between the numerical values of 1 and 100" ))
    guesses = guesses + 1

    if guesskyume > number:
        print("your guess is too high for my liking")

    elif guesskyume < number:
        print("your guess is too LOW for my liking")

    else:
        print("Good job! you guessed the number in " + str(guesses) + " tries!")
        break


    if guesses == 10:
        print("Sorry, the number was actually " + str(number))