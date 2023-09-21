#START OF LESSON 1
'''
#Names of variables and constants are 'identifiers'
BaseHealth = 100 #Variables are CamelCase
GRID_SIZE = 7 #Constants are capitalised, this is SNAKE_CASE

#Data types in Python:
#Integer
Height = 6
#Float: number with decimal fraction
Weight = 12.5

Base = 4

Area = int(Base*Height/2)
print(Area) #outputting information

#String
PlayerName = "Dave"
print(PlayerName)

#Inputting information
input("press enter to continue")
Player2Name = input("please enter a name:\n")
print("your name is: " + Player2Name)

Age = int(input("Please enter your age:\n"))

#Boolean 
IsGameOver = bool(input("True or False"))

#Selection statement

if IsGameOver == True:
  print(color.BOLD + color.RED + "GAMEOVER" + color.END)
else:
  print(color.BOLD + color.GREEN + "THE GAME IS ON" + color.END)


#Long form selection statements
HowManyHoursOfHomework = int(input("How much homework do you do per night?\n"))
if HowManyHoursOfHomework <= 1:
  print(color.RED + color.UNDERLINE + "DO MORE" + color.END)
elif HowManyHoursOfHomework <= 2:
  print(color.CYAN + "do a bit more please" + color.END)
elif HowManyHoursOfHomework <=3:
  print(color.GREEN + "Good job!!" + color.END)
else:
  print(color.YELLOW + ":nerd:" + color.END)

#iterations - loops - for loops
for count in range(10):
  print(count)
input("\n")
for count1 in range(1,11):
  print(count1)
input("\n")
for count2 in range(2,21,2):
  print(count2)

'''
#END OF LESSON 1

#START OF LESSON 2

# - A "for" loop has a set amount of times to run
# - However, a while loop does not, it is indefinite...

#iterations - loops - while loops

GameOver = False
while GameOver == False:
  print("Game is still running.")
  UserChoice = input("Do you want to continue?")
  if UserChoice.lower() == "n":
    GameOver = True
    print ("End of Game")

#subroutines - chunks of code that can be called from the program at any time.
