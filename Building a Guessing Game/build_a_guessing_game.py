import random

# Get the number from user between 1 to 49
guess_number = int( input( "Enter your guess number between 1 and 49:" ) )

# Create a random number between 1 to 49
random_number = random.randint( 1, 49 )

while True:
    if guess_number == random_number:
        print("WELL DONE!")
        break
    elif guess_number < random_number:
        print("Your guess number is low, try again!")
        guess_number = int( input( "Enter your guess number between 1 and 49:" ) )

    elif guess_number > random_number:
        print("Your guess number is high, try again!")
        guess_number = int( input( "Enter your guess number between 1 and 49:" ) )