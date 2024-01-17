import random
userChoice = input("Enter stone, paper or scissors: ").lower()
randomNum = random.randint(1,3)
array = ["stone", "paper", "scissors"]
computerChoice = array[randomNum - 1]

if userChoice == computerChoice:
  print("Draw")
elif (
(userChoice == "stone" and computerChoice == "scissors") or
(userChoice == "paper" and computerChoice == "stone") or
(userChoice == "scissors" and computerChoice == "paper")):
  print("You win")
else:
  print("You lose")