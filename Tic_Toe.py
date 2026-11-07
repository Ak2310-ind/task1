import random
game = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
score= 0
def win_check():
  if game[0][0]==game[0][1]and game[0][1]==game[0][2]:
    if game[0][0]=="X" :
      print("Congratulations!\nWinner! Winner!\nChicken Dinner!"+user)
      return 1
    elif game[0][0] == "O":
      print("Well Played!\n" +user )
      print("Better luck next time!")
      return 1
  if game[1][0]==game[1][1]and game[1][1]==game[1][2]:
      if game[1][0]=="X" :
        print("Congratulations!\nWinner! Winner!\nChicken Dinner!"+user)
        return 1
      elif game[1][0] == "O":
        print("Well Played!\n" +user )
        print("Better luck next time!")
        return 1
  if game[2][0]==game[2][1]and game[2][1]==game[2][2]:
      if game[2][0]=="X" :
        print("Congratulations!\nWinner! Winner!\nChicken Dinner!"+user)
        return 1
      elif game[2][0] == "O":
        print("Well Played!\n" +user )
        print("Better luck next time!")
        return 1
  if game[0][0]==game[1][0]and game[1][0]==game[2][0]:
     if game[0][0]=="X" :
       print("Congratulations!\nWinner! Winner!\nChicken Dinner!"+user)
       return 1
     elif game[0][0] == "O":
       print("Well Played!\n" +user )
       print("Better luck next time!")
       return 1
  if game[0][1]==game[1][1]and game[1][1]==game[2][1]:
      if game[0][1]=="X" :
        print("Congratulations!\nWinner! Winner!\nChicken Dinner!"+user)
        return 1
      elif game[0][1] == "O":
        print("Well Played!\n" +user )
        print("Better luck next time!")
        return 1
  if game[0][2]==game[1][2]and game[1][2]==game[2][2]:
      if game[0][2]=="X" :
        print("Congratulations!\nWinner! Winner!\nChicken Dinner!"+user)
        return 1
      elif game[0][2] == "O":
        print("Well Played!\n" +user )
        print("Better luck next time!")
        return 1
  if game[0][0]==game[1][1]and game[1][1]==game[2][2]:
      if game[0][0]=="X" :
        print("Congratulations!\nWinner! Winner!\nChicken Dinner!"+user)
        return 1
      elif game[0][0] == "O":
        print("Well Played!\n" +user )
        print("Better luck next time!")
        return 1
  if game[0][2]==game[1][1]and game[1][1]==game[2][0]:
      if game[0][2]=="X" :
        print("Congratulations!\nWinner! Winner!\nChicken Dinner!"+user)
        return 1
      elif game[0][2] == "O":
        print("Well Played!\n" +user )
        print("Better luck next time!")
        return 1
print("Welcome to the Tic-Tac-Toe!")
print("Rules of the game.")
print("You have to enter the row no and coordinates as input.")
print("Similar to Coordinates system.")
print("Please enter the row and column number between 1 and 3 both included.")
user=input("Enter your name:")
print("(1,1)|(1,2)|(1,3)")
print("(2,1)|(2,2)|(2,3)")
print("(3,1)|(3,2)|(3,3)")
print("Game Begins!")
print("You are :'X'")
move_count =1
while move_count<=5 and score!=1 :
 print("Your turn! "+user)
 player_row = int(input("Enter the row no:"))-1
 player_col = int(input("Enter the cloumn no:")) -1
 if player_row<3 and player_row >=0 and player_col<3 and player_col>=0 and score!=1:
  if game[player_row][player_col]!="X" and game[player_row][player_col]!="O" and score!=1:
   game[player_row][player_col]="X"
   row=0
   while row<3  :
       col=0
       while col<3:
        if col<2 :
         print(game[row][col],end=" |")
        if col ==2:
         print(game[row][col],end=" ")
        col +=1
       print()
       row+=1
   score = win_check()
   if move_count<5 and score!=1:
     print("My turn!")
   while True and score!=1:
    comp_row = random.randint(1,3)-1
    comp_col = random.randint(1,3)-1
    if game[comp_row][comp_col]!="X" and game[comp_row][comp_col]!="O" and score!=1:
     game[comp_row][comp_col]="O"
     row=0
     while row<3  :
           col=0
           while col<3:
            if col<2 :
             print(game[row][col],end=" |")
            if col ==2:
             print(game[row][col],end=" ")
            col +=1
           print()
           row+=1
     score = win_check()
     break
    else:
      continue 
   move_count+=1
  else:
    print("The space you have choosed is already filled!\nChoose other one") 
 else:
    print("You are cheating!\nPlease follow the rules of game.")
if score==0:
  print("Match draw!\n Thanks for playing"+user)