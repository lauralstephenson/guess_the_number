from random import randint
from art import logo

#Set level constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  #Player wins or gets high or low direction on guess
  if guess > answer:
    print("Too high!")
    return turns - 1
  elif guess < answer:
    print("Too low!")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")


#Function to set difficutly
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  #Player choses a difficulty
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def game():
  #Logo
  print(logo)
  #Welcome Messages
  print("Welcome to the Number Guessing Game!")
  print("I’m thinking of a number between 1-100. Can you guess it?")
  #Computer picks a random number
  answer = randint(1, 100)
  #Use to test code; comment out when game is working
  #print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  guess = 0
  #Repeat the guessing functionality if they get it wrong.
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the answer.")

    #let the user guess a number:
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses! You lose!")
      return
    elif guess != answer:
      print("Guess again.")


game()
