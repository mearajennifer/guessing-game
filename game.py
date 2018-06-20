"""A number-guessing game."""
import random
import math
# Put your code here
best_score = 9223372036854775807

# greet player and ask for name
print("what up playa")
print("what's your name?")
name = input("> ")


def guess_game():
    # initiate counter, num, and get random number
    counter = 0
    low, high = input("Enter a low: "), input("Enter a high: ")
    low, high = int(low), int(high)
    random_num = random.randint(low, high)
    congrats = "well done {}! congrats on guessing a small number in {} tries"

    # ask user for number and repeat forever until they guess the correct one
    while True:
        print("guess a number between {} and {}".format(low, high))
        num = input("> ")
        counter += 1
        try:
            num = int(num)
        except ValueError:
            print("yer dumb")
        else:
            if num == random_num:
                print(congrats.format(name, counter))
                break
            elif num > high or num < low:
                print("hi, are you sure you're smart enough for this?")
            elif num < random_num:
                print("your guess is too looooow")
            elif num > random_num:
                print("that's too high", name)

        if counter > 10:
            print("this is taking too long, you lose")
            break
    points = math.floor((counter * 100) / len(range(low, high)))
    return points


def comp_guess_game():
    low, high = input("Enter a low: "), input("Enter a high: ")
    low, high = int(low), int(high)
    counter = 0

    # computer guesses while user responds until the guess is correct
    while True:
        comp_guess = math.floor((low + high) / 2)
        print("The computer guesses {}".format(comp_guess))
        counter += 1
        print("Too high? Too low? You won?")
        answer = input("> ")
        if answer == "you won":
            print("The computer is so smart!")
            break
        elif answer == "too high":
            high = comp_guess
        elif answer == "too low":
            low = comp_guess

    points = math.floor((counter * 100) / len(range(low, high)))
    return points


while True:
    print("""Do you
        A) Want to guess the computer's number? or
        B) Want the computer to guess your number?""")
    game_type = input("> ")
    if game_type == "A":
        new_score = guess_game()
    elif game_type == "B":
        new_score = comp_guess_game()

    if new_score < best_score:
        print("That's a new low score!")
        best_score = new_score
    print("The best score is {}.".format(best_score))
    print("do you want to play again? Y or N")
    answer = input("> ")
    if answer == "N":
        break
