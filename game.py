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


while True:
    new_score = guess_game()
    if new_score < best_score:
        print("That's a new low score!")
        best_score = new_score
    print("The best score is {}.".format(best_score))
    print("do you want to play again? Y or N")
    answer = input("> ")
    if answer == "N":
        break
