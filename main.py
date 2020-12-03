import random
num = random.randint(1,101)
died = 34
wint = 34
def lose(died):
  died = int(input("You lost! Press 1 to retry and 0 to exit:"))
  if died > 1:
    print ("Press 1 to retry or 0 to exit")
    lose(died)
  elif died < 0:
    print("Press 1 to retry or 0 to exit")
    lose(died)
  elif died == 1:
    rpsgame()
  elif died == 0:
    exit()
def win(wint):
  wint = int(input("You win! Press 1 to retry and 0 to exit:"))
  if wint < 0:
    print("Press 1 to retry or 0 to exit.")
    win(wint)
  elif wint > 1:
    print("Press 1 to retry or 0 to exit.")
    win(wint)
  elif wint == 1:
      rpsgame()
  elif wint == 0:
    exit()
def rpsgame():
  com = random.randint(1,4)
  pla = int(input("Enter 1 for rock, 2 for scissors, or 3 for paper."))
  if pla == 1 and com == 3:
    lose(died)
  elif pla == 2 and com == 1:
    lose(died)
  elif pla == 3 and com == 2:
    lose(died)
  elif pla == 0:
    print("NO")
    rpsgame()
  elif pla > 3:
    print("NO")
    rpsgame()
  elif pla < 0:
    print("NO")
    rpsgame()
  elif pla == com:
    print("Tie! Try Again.")
    rpsgame()
  else:
    win(wint)
def numgame(num):
      nui = int(input("Enter number:"))
      if nui < 1:
        print("That is not 1-100")
        numgame(num)
      elif nui > 100:
        print("That is not 1-100")
        numgame(num)
      elif nui == num:
        numex = int(input("Congratulations! You correctly guessed the number! Press 1 to retry or 0 to exit."))
        if numex == 1:
          numgame(num = random.randint(1,101))
          rand()
        elif numex == 0:
          exit()
        elif numex > 1:
          print("PRESS 1 TO RETRY OR 0 TO EXIT.")
          numex = int(input("Congratulations! You correctly guessed the number! Press 1 to retry or 0 to exit."))
          if numex == 1:
            num = random.randint(1,101)
            numgame(num)
          elif numex == 0:
            exit()
          elif numex < 0:
            print("PRESS 1 TO RETRY OR 0 TO EXIT.")
            numex = int(input("Congratulations! You correctly guessed the number! Press 1 to retry or 0 to exit."))
            if numex == 1:
              num = random.randint(1,101)
              numgame(num)
            elif numex == 0:
              exit()
        elif numex < 0:
          print("PRESS 1 TO RETRY OR 0 TO EXIT.")
          numex = int(input("Congratulations! You correctly guessed the number! Press 1 to retry or 0 to exit."))
          if numex == 1:
            num = random.randint(1,101)
            numgame(num = random.randint(1,101))
            num = random.randint(1,101)
          elif numex == 0:
            exit()
          elif numex > 1:
            print("PRESS 1 TO RETRY OR 0 TO EXIT.")
            numex = int(input("Congratulations! You correctly guessed the number! Press 1 to retry or 0 to exit."))
            if numex == 1:
              num = random.randint(1,101)
              numgame(num)
            elif numex == 0:
              exit()
      elif nui > num:
        print("Too high!")
        numgame(num)
      elif nui < num:
        print("Too low!")
        numgame(num)
      print(num)
def menust():
  print("Welcome to my Game!\nType 1 to play Guess the Number, or 2 to play Rock, Paper, Scissors.\nPress 0 to exit")
  menu = int(input("Enter Choice:"))
  if menu == 0:
    exit()
  elif menu == 1:
      print("Welcome to my Guess the Number game!\nGuess a number from 1-100 and the game will tell you if the number is lower or higher!")
      numgame(num)
  elif menu == 2:
    print("Welcome to my Rock, Paper, Scissors game!")
    while True:
      rpsgame()
  elif menu > 2:
    print("That isn't a choice. Try Again.")
    menust()
  elif menu < 0:
    print("That isn't a choice. Try Again.")
    menust()
menust()
