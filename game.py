"""A number-guessing game."""
import random
# Put your code here

# greet player and ask for name
print("what up playa")
print("what's your name?")
name = input("> ")

# initiate counter, num, and get random number
counter = 0
num = 0
random_num = random.randint(1, 100)
congrats = "well done {}! congrats on guessing a small number in {} tries"

# ask user for number and repeat forever until they guess the correct one
while num != random_num:
    print("guess a number between 1 and 100")
    num = input("> ")
    num = int(num)
    counter += 1
    if num > 100:
        print("hi, are you sure you're smart enough for this?")
    elif num < random_num:
        print("your guess is too looooow")
    elif num > random_num:
        print("that's too high", name)
    else:
        print(congrats.format(name, counter))
