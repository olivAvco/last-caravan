import random
import _2_inventory

# MATERIALS PRICES

ironPrice = round(random.uniform(3.80, 4.20), 2)
sellIronPrice = round(random.uniform(4.00, 4.60), 2)

fabricPrice = round(random.uniform(5.20, 5.60), 2)
sellFabricPrice = round(random.uniform(5.40, 6.00), 2)

medicinePrice = round(random.uniform(8.50, 9.00), 2)
sellMedicinePrice = round(random.uniform(9.00, 10.00), 2)

robotPrice = round(random.uniform(15.00, 20.00), 2)
sellRobotPrice = round(random.uniform(20.00, 25.00), 2)

# SHOPs MENU

shopLittletown = [
   "===== LITTLETOWN SHOP =====",

    "",
    
    "BUY:",
    "- Nothing",

    "",

    "SELL:",
    "- Iron",
    "- Fabric",

    "",

    "1 - Buy"
]

shopIronvalle = [
     "===== IRONVALLE SHOP =====",

    "",

    "BUY:",
    "- Iron",

    "",

    "SELL:",
    "- Medicine",

    "",

    "1 - Buy",
    "2 - Sell"
]

shopLumaria = [
     "===== LUMARIA SHOP =====",

    "",

    "BUY:",
    "- Fabric",

    "",

    "SELL:",
    "- Nothing",

    "",

    "1 - Buy",
    "2 - Sell"
]

shopUnitown = [
    "===== UNITOWN SHOP =====",

    "",

    "BUY:",
    "- Medicine",

    "",

    "SELL:",
    "- Robots",

    "",

    "1 - Buy",
    "2 - Sell"
]

shopAcademy = [
        "===== ACADEMY SHOP =====",

    "",

    "BUY:",
    "- Robots",

    "",

    "SELL:",
    "- Nothing",

    "",

    "1 - Buy",
    "2 - Sell"
]

# SHOP FUNCTIONS

def showShop(city):

    if city == "Littletown":
        print("\n".join(shopLittletown))
    elif city == "Ironvalle":
        print("\n".join(shopIronvalle))
    elif city == "Lumaria":
        print("\n".join(shopLumaria))
    elif city == "Unitown":
        print("\n".join(shopUnitown))
    else:
        print("\n".join(shopAcademy))

# SELLING FUNCTIONS

def showSellOptions(city):

    if city == "Littletown":
        sellButton = input("\nWe buy Iron and Fabric. Do you want to sell any of those?")
        if sellButton == "y":
            print("\nWhat do you want to sell?")
            print("1 - Iron")
            print("2 - Fabric")
            
            try:
                itemChoice = int(input("Type the number of the item you want to sell: "))
                if itemChoice == 1:
                    if _2_inventory.hasItem("Iron"):
                        print("\nYou have {amount} units of Iron. How many do you want to sell?").format(amount=_2_inventory.getItemCount("Iron"))
                        try:
                            sellAmount = int(input("Type the amount: "))
                            if sellAmount > _2_inventory.getItemCount("Iron"):
                                print("\nYou don't have that much Iron to sell.")
                            else:
                                totalEarnings = sellAmount * sellIronPrice
                                print(f"\nYou sold {sellAmount} units of Iron for {totalEarnings} coins.")
                                money += totalEarnings
                                roundedMoney = round(money, 2)
                                for _ in range(sellAmount):
                                    _2_inventory.removeItem("Iron")
                        except ValueError:
                            print("\nInvalid input. Please enter a valid number.")
                        roundedMoney = round(money, 2)
                        _2_inventory.removeItem("Iron")
                    else:
                        print("\nYou don't have any Iron to sell.")
                elif itemChoice == 2:
                    if _2_inventory.hasItem("Fabric"):
                        print("\nYou have {amount} units of Fabric. How many do you want to sell?").format(amount=_2_inventory.getItemCount("Fabric"))
                        try:
                            sellAmount = int(input("Type the amount: "))
                            if sellAmount > _2_inventory.getItemCount("Fabric"):
                                print("\nYou don't have that much Fabric to sell.")
                            else:
                                totalEarnings = sellAmount * sellFabricPrice
                                print(f"\nYou sold {sellAmount} units of Fabric for {totalEarnings} coins.")
                                money += totalEarnings
                                roundedMoney = round(money, 2)
                                for _ in range(sellAmount):
                                    _2_inventory.removeItem("Fabric")
                        except ValueError:
                            print("\nInvalid input. Please enter a valid number.")
                        roundedMoney = round(money, 2)
                        _2_inventory.removeItem("Fabric")
                    else:
                        print("\nYou don't have any Fabric to sell.")
                elif itemChoice == 2:
                    print("\nYou don't have any Fabric to sell.")

            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

    elif city == "Ironvalle":

        if _2_inventory.hasItem("Medicine"):
                        print("\nYou have {amount} units of Medicine. How many do you want to sell?").format(amount=_2_inventory.getItemCount("Medicine"))
                        try:
                            sellAmount = int(input("Type the amount: "))
                            if sellAmount > _2_inventory.getItemCount("Medicine"):
                                print("\nYou don't have that much Medicine to sell.")
                            else:
                                totalEarnings = sellAmount * sellMedicinePrice
                                print(f"\nYou sold {sellAmount} units of Medicine for {totalEarnings} coins.")
                                money += totalEarnings
                                roundedMoney = round(money, 2)
                                for _ in range(sellAmount):
                                    _2_inventory.removeItem("Medicine")
                        except ValueError:
                            print("\nInvalid input. Please enter a valid number.")
                        roundedMoney = round(money, 2)
                        _2_inventory.removeItem("Medicine")
        else:
            print("\nYou don't have any Medicine to sell.")

    elif city == "Lumaria":

        print("\nYou can't sell anything in Lumaria.")

    elif city == "Unitown":
        
        if _2_inventory.hasItem("Robots"):
                        print("\nYou have {amount} units of Robots. How many do you want to sell?").format(amount=_2_inventory.getItemCount("Robots"))
                        try:
                            sellAmount = int(input("Type the amount: "))
                            if sellAmount > _2_inventory.getItemCount("Robots"):
                                print("\nYou don't have that much Robots to sell.")
                            else:
                                totalEarnings = sellAmount * sellRobotPrice
                                print(f"\nYou sold {sellAmount} units of Robots for {totalEarnings} coins.")
                                money += totalEarnings
                                roundedMoney = round(money, 2)
                                for _ in range(sellAmount):
                                    _2_inventory.removeItem("Robots")
                        except ValueError:
                            print("\nInvalid input. Please enter a valid number.")
                        roundedMoney = round(money, 2)
                        _2_inventory.removeItem("Robots")
        else:
            print("\nYou don't have any Robots to sell.")

    else:
        print("\nYou can't sell anything in Academy.")

# BUYING FUNCTIONS

def buyFunc(city):
    global money
    global roundedMoney

    if city == "Littletown":

        print("\nYou can't buy anything in Littletown.")
        
    elif city == "Ironvalle":

        print(f"The price of Iron is {ironPrice} coins per unit.")
        buyButton = input("Do you want to buy Iron? (y/n) ").lower()
        
        if buyButton == "y":
            print("How much Iron do you want to buy?")
            try:
                amount = int(input("Type the amount: "))
                totalCost = amount * ironPrice
                print(f"\nThe total cost is {totalCost} coins.")
                confirmButton = input("Do you want to confirm the purchase? (y/n) ").lower()

                if confirmButton == "y":
                    print(f"\nYou bought {amount} units of Iron for {totalCost} coins.")
                    money -= totalCost
                    roundedMoney = round(money, 2)
                    for _ in range(amount):
                        _2_inventory.addItem("Iron")
                elif confirmButton == "n":
                    print("\nYou can sell something we need instead!")
                    
                else:
                    print("\nPurchase cancelled.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")


        print(f"\nYou bought Iron for {roundedMoney} coins.")
        money -= roundedMoney
        roundedMoney = round(money, 2)
        _2_inventory.addItem(f"Iron x{amount}")


    elif city == "Lumaria":

        print(f"The price of Fabric is {fabricPrice} coins per unit.")
        buyButton = input("Do you want to buy Fabric? (y/n) ").lower()
        
        if buyButton == "y":
            print("How much Fabric do you want to buy?")
            try:
                amount = int(input("Type the amount: "))
                totalCost = amount * fabricPrice
                print(f"\nThe total cost is {totalCost} coins.")
                confirmButton = input("Do you want to confirm the purchase? (y/n) ").lower()

                if confirmButton == "y":
                    print(f"\nYou bought {amount} units of Fabric for {totalCost} coins.")
                    money -= totalCost
                    roundedMoney = round(money, 2)
                    for _ in range(amount):
                        _2_inventory.addItem("Fabric")
                else:
                    print("\nPurchase cancelled.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

        print(f"\nYou bought Fabric for {roundedMoney} coins.")
        money -= roundedMoney
        roundedMoney = round(money, 2)
        _2_inventory.addItem("Fabric")

    elif city == "Unitown":
        
        print(f"The price of Medicine is {medicinePrice} coins per unit.")
        buyButton = input("Do you want to buy Medicine? (y/n) ").lower()
        
        if buyButton == "y":
            print("How much Medicine do you want to buy?")
            try:
                amount = int(input("Type the amount: "))
                totalCost = amount * medicinePrice
                print(f"\nThe total cost is {totalCost} coins.")
                confirmButton = input("Do you want to confirm the purchase? (y/n) ").lower()

                if confirmButton == "y":
                    print(f"\nYou bought {amount} units of Medicine for {totalCost} coins.")
                    money -= totalCost
                    roundedMoney = round(money, 2)
                    for _ in range(amount):
                        _2_inventory.addItem("Medicine")
                elif confirmButton == "n":
                    print("\nYou can sell something we need instead!")
                    
                else:
                    print("\nPurchase cancelled.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")


        print(f"\nYou bought Medicine for {roundedMoney} coins.")
        money -= roundedMoney
        roundedMoney = round(money, 2)
        _2_inventory.addItem(f"Medicine x{amount}")

    else:
        print(f"The price of Robots is {robotPrice} coins per unit.")
        buyButton = input("Do you want to buy Robots? (y/n) ").lower()
        
        if buyButton == "y":
            print("How much Robots do you want to buy?")
            try:
                amount = int(input("Type the amount: "))
                totalCost = amount * robotPrice
                print(f"\nThe total cost is {totalCost} coins.")
                confirmButton = input("Do you want to confirm the purchase? (y/n) ").lower()

                if confirmButton == "y":
                    print(f"\nYou bought {amount} units of Robots for {totalCost} coins.")
                    money -= totalCost
                    roundedMoney = round(money, 2)
                    for _ in range(amount):
                        _2_inventory.addItem("Robots")
                elif confirmButton == "n":
                    print("\nYou can sell something we need instead!")
                    
                else:
                    print("\nPurchase cancelled.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")


        print(f"\nYou bought Robots for {roundedMoney} coins.")
        money -= roundedMoney
        roundedMoney = round(money, 2)
        _2_inventory.addItem(f"Robots x{amount}")