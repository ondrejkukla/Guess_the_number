import random
logo = """_____                       _   _                                  _               
|  __ \                     | | | |                                | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                    
 """
      
#  inputs
print(logo)
print("Welcome to the game 'Guess the number'.")
print(f"I am thinking of number in range 1 - 100.")
difficulty = ""
number = random.choice(range(1, 101))
game_over = False
number_guessed = False
print(number)

#  start of the code
while not difficulty == "easy" and not difficulty == "hard":
  print("Try again")
  difficulty = input ("Choose a difficulty. 'easy' or 'hard': ").lower()
  print(difficulty)

attempts = 0
if difficulty == "easy":
  attempts = 10
else:
  attempts = 5
print(f"You have {attempts} attempts remaining to guess the number.")

def counting():
  global guess_again, game_over, number_guessed, attempts
  while game_over == False and number_guessed == False:
    if int(guess_again) == number:
      number_guessed = True
    else:
      attempts -= 1
      if attempts == 0:
        game_over = True
      else:
        if int(guess_again) > number:
          print(f"Too high. You have {attempts} attempts left.")
          guess_again = input("Try again: ")
          counting()
        elif int(guess_again) < number:
          print(f"Too low. You have {attempts} attempts left.")
          guess_again = input("Try again: ")
          counting()

guess = int(input("Guess the number: "))
if guess == number:
  number_guessed = True
else:
  attempts -= 1
  if guess > number:
    print(f"Too high. You have {attempts} attempts left.")
    guess_again = int(input("Try again: "))
    counting()
  elif guess < number:
    print(f"Too low. You have {attempts} attempts left.")
    guess_again = int(input("Try again: "))
    counting()

counting()

if number_guessed == True:
  print ("You have guessed the number. You win.")
if game_over == True:
  print(f"You are out of guesses. Game over. The number is {number}")