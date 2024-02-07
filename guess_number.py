number = 10

print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? (Enter 'q' to quit) ")

    if guess == 'q':
        print(f"The number was {number}.")
        break

    try:
        guess = int(guess)
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        elif guess < number:
            print("Sorry! That's too low. Try a higher number.")
        else:
            print("Sorry! That's too high. Try a lower number.")
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")