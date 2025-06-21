import random
def options(user_choice):
    switch = {
        1: "rock",
        2: "paper",
        3: "scissor",
    }
    return switch.get(user_choice)

def computer():
    computer_choice = random.randint(1,3)
    return computer_choice

def evaluator(user_choice,computer):
    rules = {
        "rock":"scissor",
        "paper":"rock",
        "scissor":"paper",
    }
    if user_choice==computer:
        return "It is a Tie"
    elif rules.get(user_choice)==computer:
        return "You win"
    else:
        return "You lose"
    
print('''   The name of the game is Rock-Paper-Scissor, in this game you 
      are supposed to choose an option. The options are Rock, Paper and Scissor
      
      Here is the logic of the game:
      Rock beats scissors, scissors beat paper, and paper beats rock.
      
      Options:
      1. Rock
      2. Paper
      3. Scissor\n''')

while True:
    user = int(input("Enter your choice: "))
    while user not in [1,2,3]:
        print("Invalid Input")
        user = int(input("Enter your choice: "))
    user_choice = options(user)
    comp = computer()
    computer_choice = options(comp)
    print('Your choice: {0} , Computer choice: {1}'.format(user_choice,computer_choice))
    print(evaluator(user_choice,computer_choice))
    option = input("Do you want to continue (Y/N)?")
    if (option.lower()=='y'):
        pass
    else:
        break
