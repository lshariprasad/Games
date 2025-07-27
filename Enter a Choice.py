import random

def get_choices():
    player_choice= input("Enter a Choice (rock , paper , scissor) : ")
    options = ["rock","paper","scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice,"computer":computer_choice}
    return choices



def check_win(player,computer):
    print(f"You Chose {player}, Computer Chose  {computer}" ) # using  f-strings
    if player == computer :
        return "Its a Tie !"
    elif player == "rock":
      if computer == "scissor":
        return "Rock Smashes Scissor! You Win!"
      else:
        return "Paper covers rock! You Lose. "
    elif player == "paper":
       if computer == "rock":
          return "Paper cover Rock! You Win!"
       else:
          return "Scissors cuts paper! You Lose."
    elif player == "scissor":
       if computer == "paper":
          return "Scissors cuts paper! You Win!"
       else:
          return "rock smasher scissors! You lose."
          

choices = get_choices()
result = check_win(choices["player"],choices["computer"])


print(result)