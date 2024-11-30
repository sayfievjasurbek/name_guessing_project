import random
import art

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

number_to_guess = random.randint(1, 100)
print(f"Pssst! The correct number is {number_to_guess}")  # This is just for testing, you can remove it later

while attempts > 0:
    asking_user = int(input(f"You have {attempts} attempts left. Guess the correct number: "))
    if asking_user == number_to_guess:
        print(f"You guessed correctly! The correct number is {number_to_guess}")
        break
    elif asking_user > number_to_guess:
        print(f"Sorry {asking_user} is too high.")
    elif asking_user < number_to_guess:
        print(f"Sorry {asking_user} is too low.")

    attempts -= 1  # Reduce the number of attempts after each guess

if attempts == 0:
    print(f"Game over! The correct number was {number_to_guess}")





