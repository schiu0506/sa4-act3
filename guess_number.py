number = 10
max_guesses = 5
remaining_guesses = max_guesses

print("I'm thinking of a number...")

while remaining_guesses > 0:
    print(f"You have {remaining_guesses} guesses left.")
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
        remaining_guesses -= 1
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")

if remaining_guesses == 0:
    print("Sorry! You've run out of guesses. The number was", number)