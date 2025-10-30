from random import randint

def line():
  print("-"*50)

def get_move():
  print("Chose from Rock(1) Paper(2) Scissors(3)")
  line()
  choise = int(input("===>> "))
  if choise in {1,2,3}:
    return choise
  else:
    print("invalid move please try again!!!")
    get_move()

def generate_move():
  return randint(1,3)

def deside(players_move, sys_move):
  win_condition= {
    1:3,
    2:1,
    3:2
  }
  return win_condition[players_move] == sys_move

def announce_record(winer, winer_list):
  if winer:
    line()
    print("You WIN this round")
  else:
    line()
    print("You LOSE this round")
  winer_list.append("p" if winer else "s")

def main():
  print("There will be 5 rounds of Rock, Paper, Scissors")
  print("Who ever wines 3 or more rounds wines the Game")
  winer_list = []
  for _ in range(0,5):
    players_move = get_move()
    sys_move = generate_move()
    winer = deside(players_move, sys_move)
    announce_record(winer, winer_list)
  p_wins = winer_list.count("p")
  s_wins = winer_list.count("s")
  if p_wins > s_wins:
    line()
    print(f"You WIN the Game! Player: {p_wins} System: {s_wins} :> yeeeeee!!")
  else:
    line()
    print(f"You LOSE the Game! Player: {p_wins} System: {s_wins} :<")
if __name__ == "__main__":
  main()
