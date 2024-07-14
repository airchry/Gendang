import random
from replit import clear
from art import logo


def play_game():

  is_game_over = False

  number = []
  for list_of_num in range(1, 101):
    number.append(list_of_num)
  
  print(logo)
  
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  
  chosen_number = random.choice(number)
  
  # print(f"Pssst, the correct answer is {chosen_number}")
  
  wrong_dif = False
  while not wrong_dif:
    difficulty = input("Choose a difficutly. Type 'easy' or 'hard': ").lower()
    
    if difficulty == "easy":
      wrong_dif = True
      attempt = 10
    elif difficulty == "hard":
      wrong_dif = True
      attempt = 5
    else:
      print("Please input the correct difficulty.")
    
  while not is_game_over:  
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if attempt == 1:
      attempt -= 1
      is_game_over = True
      print(f"You have run out of guesses. You Lose.\nThe correct answer is {chosen_number}")
    elif guess == chosen_number:
      is_game_over = True
      print(f"You got it! The answer was {chosen_number}.")
    elif guess > chosen_number:
      attempt -= 1
      print("Too high\nGuess again.")
    elif guess < chosen_number:
      attempt -= 1
      print("Too low\nGuess again.")
    

while input("Do you want to play a game of 'Guess the Number'? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
