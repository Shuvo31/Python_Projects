import random
                                                                    
player_score = []
computer_choice = ["R","P","S"]

message = '''Welcome to Rock Paper Scissor game.
The game has 5 rounds.
Whover with maximum number wins.
Enjoy!
'''

print(message)

for i in range(5):
  player_choice = input("Press R for Rock, press P for paper and S for scissor: ")
  computer = computer_choice[random.randint(0,2)]
  print("Player\'s choice: ", player_choice)
  print("Computer\'s choice: ",computer)

  if (player_choice == computer):
      player_score.append(0)

  elif (player_choice == "R" and computer == "P"):
      player_score.append(0)

  elif (player_choice == "P" and computer == "S"):
      player_score.append(0)

  elif (player_choice == "S" and computer == "R"):
      player_score.append(0)

  else:
      player_score.append(1)

if (sum(player_score)>= 3):
  print("You won in {} out of 5 rounds! You are the winner :-)".format(sum(player_score)))

else:
  print("Computer won in {} out of 5 rounds! Computer is the winner, better luck next time :-)".format(5 - sum(player_score)))
