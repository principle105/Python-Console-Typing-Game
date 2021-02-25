import random
import sys
import time
from getkey import getkey

reset = "\033[0m"
underline = "\033[4m"
red = "\033[1;91m"
green = "\033[1;32m"

quotes = [
  "They don't know that we know they know we know",
  "power power power power power power power power power power",
  "hello world!!!",
  "This is a simple typing program made in python"
 ]

def clear():
  sys.stdout.write("\033[2J\033[H")

ready = input(f"Python Typing Game\n\n{reset}Press Enter to start")

play = "y"

while play == "y":
  string = random.choice(quotes)

  for i in range(3,0,-1):
    clear()
    print(string)
    print(i)
    time.sleep(0.5)

  complete = False
  current_letter = 0
  wrong = 0
  end_time = time.time()
  while not complete:
    if current_letter > 0:
      doneString = reset + green + string[:current_letter]
    current = underline + green + string[current_letter]
    afterCurrent = reset + string[current_letter+1:]
    
    clear()
    if current_letter == 0:
      print(current + afterCurrent)
    else:
      print(doneString + current + afterCurrent)
    
    theinput = getkey()
    while theinput != string[current_letter]:
      wrong += 1
      current = underline + red + string[current_letter]
      clear()
      if current_letter == 0:
        print(current + afterCurrent)
      else:
        print(doneString + current + afterCurrent)

      theinput = getkey()

    if current_letter >= len(string)-1:
      complete = True

    current_letter += 1

  clear()
  totaltime = (time.time()-end_time)/60
  wpm = round((len(string)/5)/totaltime)
  accuracy = round(100-((wrong/(len(string) + wrong)) * 100))
  text = f"{reset}Wpm: {green}{wpm}{reset}\nAccuracy: {green}{accuracy}%"
  print(text)

  while True:
    play = input(f"{reset}Do you want to play again? (y/n)").lower()
    clear()
    if play in ["y","n"]:
      break

print(f"{reset}Have a good day")