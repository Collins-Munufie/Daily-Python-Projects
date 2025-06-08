import random
import tkinter

secret_number = random.randint(1,100)

attempt = 0
max_attempts = 5

print ("Welcome to the Guess the Number Game")
print("I have selected a secret number between 1 and 100.")
print("You have 5 attempts to guess it correctly.")

while attempt < 5:
    guess = int(input("Guess the secret number (1-100): "))
    attempt += 1

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    elif guess < secret_number:
        print("Too low!, try again.")
    else:
        print("Too high!, try agagin.")
        print(f"Attempt {attempt} of {max_attempts}. You have {max_attempts - attempt} attempts left.")    

if attempt == max_attempts:
    print ("Game Over!")
    print (f"sorry! you've used all {attempt} attempt.Here was the secret number:{secret_number}🤣")
















# if attempt == max_attempts:
#     print(f"Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}.")
