import time
import _2_inventory
import _3_shop

# =========================
# GAME VARIABLES
# =========================

dayCounter = 1

money = 100.00
roundedMoney = round(money, 2)

debt = None
maxDays = None

cityName = "Littletown"


# =========================
# CITY CONNECTIONS
# =========================

citiesDic = {

    "Littletown": ["Ironvalle"],

    "Ironvalle": [
        "Littletown",
        "Lumaria"
    ],

    "Lumaria": [
        "Ironvalle",
        "Unitown"
    ],

    "Unitown": [
        "Lumaria",
        "Academy"
    ],

    "Academy": [
        "Unitown"
    ]
}


# =========================
# TRAVEL COSTS
# =========================

travelCosts = {

    ("Littletown", "Ironvalle"): 15,
    ("Ironvalle", "Littletown"): 15,

    ("Ironvalle", "Lumaria"): 40,
    ("Lumaria", "Ironvalle"): 40,

    ("Lumaria", "Unitown"): 75,
    ("Unitown", "Lumaria"): 75,

    ("Unitown", "Academy"): 120,
    ("Academy", "Unitown"): 120
}


# =========================
# TRAVEL FUNCTION
# =========================

def travelFunc(city):

    global dayCounter
    global money
    global roundedMoney

    print("\nWhere do you want to go?")

    if city in citiesDic:

        print("You can go to:")

        for connectedCity in citiesDic[city]:
            print(f"- {connectedCity}")

    else:
        print("City not found.")
        return city

    goto = input("\nType the city: ").capitalize()

    # Check if route exists
    if goto in citiesDic[city]:

        # Creates route tuple
        route = (city, goto)

        # Gets travel cost from dictionary
        travelPrice = travelCosts[route]

        print(f"\nTravel cost: R${travelPrice}")

        # Checks if player has enough money
        if money >= travelPrice:

            print(f"Traveling to {goto}...")
            time.sleep(4.5)

            # Remove travel price
            money -= travelPrice

            # Update rounded money
            roundedMoney = round(money, 2)

            # Advance one day
            dayCounter += 1

            return goto

        else:

            print("\nYou don't have enough money to travel.")
            return city

    else:

        print("\nYou can't go there.")
        return city


# =========================
# DIALOG PAUSE
# =========================

def dialogTime():
    time.sleep(3.5)


# =========================
# START GAME
# =========================

def startGame():

    while True:

        startButton = input(
            "Ready to start the game? (Y/N): "
        ).upper()

        if startButton == "Y":

            print("Great! Let's start right now!")
            break

        elif startButton == "N":

            print("Okay, until next time!")
            exit()

        else:

            print("Please, choose a valid option.")


# =========================
# GAME DIFFICULTY
# =========================

gameBeaten = False


def gameDificulty():

    while True:

        print("""1 - New Game
2 - End Game (LOCKED)""")

        dificultyButton = input(
            "Choose the game dificulty (1 / 2): "
        )

        if dificultyButton == "1":

            print(
                "Game dificulty defined to 'Normal'. Have fun!\n"
            )

            return "normal"

        elif dificultyButton == "2":

            if gameBeaten == False:

                print(
                    "You didn't beat the game yet! Try after that."
                )

            elif gameBeaten == True:

                print(
                    "Game dificulty defined to 'End Game'. Have fun!\n"
                )

                return "endgame"

        else:

            print("Please, choose a valid option.")


# =========================
# GAME INITIALIZATION
# =========================

startGame()

gameMode = gameDificulty()


if gameMode == "normal":

    debt = 5000.00
    roundedDebt = round(debt, 2)

    maxDays = 100


elif gameMode == "endgame":

    debt = 10000.00
    roundedDebt = round(debt, 2)

    maxDays = 50


# =========================
# INTRODUCTION
# =========================

while True:

    name = input(
        "Hi, my name is Ross. What is your name?: "
    )

    print(
        "You are a merchant, right? "
        "I was a friend of your parents before they...died."
    )

    dialogTime()

    print(
        "I came to tell you that they left a debt "
        "to you after passed away, and it is...big."
    )

    dialogTime()

    print(
        f"The debt is R${roundedDebt}. "
        "I know it is big, but I know you can pay it."
    )

    dialogTime()

    print(
        f"Anyways, I have to go now, good luck, {name}.\n"
    )

    dialogTime()

    print(
        "You are in a new city called Littletown."
    )

    dialogTime()

    print(
        "The city is still in its early construction stage."
    )

    dialogTime()

    print(
        "People working here need iron."
    )

    dialogTime()

    break


# =========================
# MAIN GAME LOOP
# =========================

while True:

    menuUI = [

        f"Name: {name}",
        f"City: {cityName}",
        f"Day: {dayCounter}",
        f"Money: R${roundedMoney}",
        f"Debt: R${roundedDebt}",

        "",

        "1 - Travel",
        "2 - Inventory",
        "3 - Shop",
        "4 - Leave Game"
    ]

    print("\n" + "=" * 25)
    print("\n".join(menuUI))

    actionButton = input(
        "\nWhat do you want to do now?: \n"
    )

    if actionButton == "1":

        cityName = travelFunc(cityName)

    elif actionButton == "2":

        _2_inventory.showInventory()
        input("\nPress any key to leave the inventory...")

    elif actionButton == "3":

        _3_shop.showShop(cityName)
        actionButton = input("Do you want to buy something? (Y/N): ").upper()
        if actionButton == "Y":
            _3_shop.buyItem(cityName)
            input("\nPress any key to leave the shop...")

        elif actionButton == "N":
            print("\nLeaving shop...")
            time.sleep(2.5)

        else:
            print("Please, choose a valid option.")


    elif actionButton == "4":

        print("\nLeaving game...")
        break

    else:

        print("Please, choose a valid option.")