print("Welcome at the game. The program creates a random number from 0-20 you have to guess. Good luck!")

import random 
random_number = random.randint(1,100)

own_number=int(input("Enter a number:"))

tries=1

while own_number != random_number:
  tries += 1
  if own_number > random_number:
    print("Your number is too high. Try again!")
    own_number=int(input("Enter a number:"))
  elif own_number < random_number: 
    print("Your number is too low. Try again!")
    own_number=int(input("Enter a number:"))

print(f"Congratulations! Youve guessed the right number in {tries} tries.")


       


