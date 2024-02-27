#name = input('what is your name? ')
#print('hello ' + name)


birth_year = input('enter your birth year: ')
age = 2024 - int(birth_year)
print(age)

#my code
first_num = input('enter first number: ')
second_num = input('enter second number: ')
sum = float(first_num) + float(second_num)
print('sum: ', sum)


weight_num = input('Weight: ')
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
     times = float(weight_num) * 0.45359237
     print("Weight in Kg: ", times)
elif unit.upper() == "L":
    times2 = float(weight_num) * 2.2046
    print("Weight in Lbs: ", times2)
else:
    print("NO")

#my own func lol
def reverse_input():
    word = input("Type a word to see it backwards: ")
    reversed_word = word[::-1]
    return reversed_word

reversed_input = reverse_input()
print(reversed_input)

def reverse_sentence():
    sentence = input("Type a sentence to see it backwards: ")
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_str = ' '.join(reversed_words)
    return reversed_str

reversed_sentence = reverse_sentence()
print(reversed_sentence)


#numbers
import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 11)
    
    while True:
        try:
            # Ask the user to guess the number
            guess = int(input("Guess the number (between 1 and 10): "))
            
            # Check if the guess is correct
            if guess == secret_number:
                print("Congratulations! You guessed the number!")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Call the function to play the game
guess_the_number()

import random

def guess_the_animal():
    options = ["fish", "dog", "cat", "bird", "cow"]
    secret_animal = random.choice(options)
    
    while True:
        try: 
            guess = input("Guess the animal, here are your options: dog, cat, bird, fish, cow: ")

            if guess == secret_animal:
                print("Good job! You got it.")
                break
            else:
                print("Nope, try again.")
        except ValueError:
            print("Not an option.")

guess_the_animal()



