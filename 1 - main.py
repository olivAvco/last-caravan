import time

dayCounter = 1
money = 100.00
roundedMoney = round(money,2)
debt = None
maxDays = None
cityName = "Littletown"



def dialogTime():
        time.sleep(3.5)

def startGame():
    while True:
        startButton = input("Ready to start the game? (Y/N): ").upper()
        if startButton == "Y":
            print("Great! Let's start right now! ")
            break
        elif startButton == "N":
            print("Okay, until next time!")
        else:
            print("Please, choose a valid option.")

gameBeaten = False

def gameDificulty():
    while True:
        print("""1 - New Game
2 - End Game (LOCKED) """)
        dificultyButton = input("Choose the game dificulty ( 1 / 2 ): ")

        if dificultyButton == "1":
            print("Game dificulty defined to 'Normal'. Have fun!\n ")
            return "normal"
        elif dificultyButton == "2":
            if gameBeaten == False:
                print("You didn't beat the game yet! Try after that.")
            elif gameBeaten == True:
                print("Game dificulty defined to 'End Game'. Have fun!\n ")
                return "endgame"
            else:
                print("Please, choose a valid option.")

startGame()
gameMode = gameDificulty()

if gameMode == "normal":
    debt = 5000.00
    roundedDebt = round(debt,2)
    maxDays = 100

elif gameMode == "endgame":
    debt = 10000.00
    roundedDebt = round(debt,2)
    maxDays = 50

while True:
    name = input("Hi, my name is Ross. What is your name? : ")
    print("You are a merchant, right? I was a friend of your parents before they...died.")
    dialogTime()
    print("I came to tell you that they left a debt to you after passed away, and it is...big.")
    dialogTime()
    print(f"The debt is R${roundedDebt}. I know, it is big, but i know you can pay it, right?")
    dialogTime()
    print(f"Anyways, i have to go now, good luck, {name}.\n")
    dialogTime()
    print("You are in a new city called Littletown, the city is still in its early construction stage.") 
    dialogTime()
    print("Here, the people working need iron, maybe you can make some money knowing that.\n")
    dialogTime()
    break

menuUI1 = [
    f"Name: {name}",
    f"City: {cityName}",
    f"Day: {dayCounter}",
    f"Debt: {roundedDebt}",
    "",
    "1 - Travel",
    "2 - Inventory",
    "3 - Leave Game"
]

menuUI2 = [
    f"Name: {name}",
    f"City: {cityName}",
    f"Day: {dayCounter}",
    f"Debt: {roundedDebt}",
    "",
    "1 - Travel",
    "2 - Inventory",
    "3 - Shop",
    "4 - Leave Game"
]

while True:
    print("\n".join(menuUI1))
    actionButton = input("\nWhat do you want to do now?: ")