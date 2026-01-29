import random

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 20.")

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

# You get 5 chances to guess
for i in range(5):
    guess = int(input("Take a guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Good job! You guessed my number {secret_number} in {i+1} tries!")
        break
else:
    print(f"😢 Sorry, you ran out of tries. The number was {secret_number}.") 