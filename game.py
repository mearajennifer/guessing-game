"""A number-guessing game."""
import random
# Put your code here
keep_playing = True
best_score = 9223372036854775807

# greet player and ask for name
print("what up playa")
print("what's your name?")
name = input("> ")


def guess_game():
    # initiate counter, num, and get random number
    counter = 0
    num = 0
    random_num = random.randint(1, 100)
    congrats = "well done {}! congrats on guessing a small number in {} tries"

    # ask user for number and repeat forever until they guess the correct one
    while num != random_num:
        print("guess a number between 1 and 100")
        num = input("> ")
        counter += 1
        try:
            num = int(num)
        except ValueError:
            print("yer dumb")
        else:
            if num > 100 or num < 1:
                print("hi, are you sure you're smart enough for this?")
            elif num < random_num:
                print("your guess is too looooow")
            elif num > random_num:
                print("that's too high", name)
            else:
                print(congrats.format(name, counter))
    return counter


while keep_playing:
    new_score = guess_game()
    if new_score < best_score:
        print("That's a new low score!")
        best_score = new_score
    print("do you want to play again? Y or N")
    answer = input("> ")
    if answer == "N":
        keep_playing = False
