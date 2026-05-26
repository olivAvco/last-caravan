import _2_inventory


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
    "- Robots",

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
    "- Nothing",

    "",

    "SELL:",
    "- Nothing",

    "",

    "1 - Buy",
    "2 - Sell"
]

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


def showSellOptions(city):

    if city == "Littletown":
        print("\nWe buy Iron and Fabric. Do you want to sell any of those?")
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
                                totalEarnings = sellAmount * 
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
                        print("\nYou sold Fabric for 25 coins.")
                        money += 25
                        roundedMoney = round(money, 2)
                        _2_inventory.removeItem("Fabric")
                    else:
                        print("\nYou don't have any Fabric to sell.")
                else:
                    print("\nInvalid choice. Please select a valid item number.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

    elif city == "Ironvalle":
        print("\nYou can sell Medicine in Ironvalle.")
    elif city == "Lumaria":
        print("\nYou can't sell anything in Lumaria.")
    elif city == "Unitown":
        print("\nYou can sell Robots in Unitown.")
    else:
        print("\nYou can't sell anything in Academy.")

def buyFunc(city):
    global money
    global roundedMoney

    if city == "Littletown":

        print("\nYou can't buy anything in Littletown.")
        
    elif city == "Ironvalle":

        print(f"The price of Iron is {roundedMoney} coins per unit.")
        buyButton = input("Do you want to buy Iron? (y/n) ").lower
        
        if buyButton == "y":
            print("How much Iron do you want to buy?")
            try:
                amount = int(input("Type the amount: "))
                totalCost = amount * roundedMoney
                print(f"\nThe total cost is {totalCost} coins.")
                confirmButton = input("Do you want to confirm the purchase? (y/n) ").lower()

                if confirmButton == "y":
                    print(f"\nYou bought {amount} units of Iron for {totalCost} coins.")
                    money -= totalCost
                    roundedMoney = round(money, 2)
                    for _ in range(amount):
                        _2_inventory.addItem("Iron")
                elif confirmButton == "n":
                    print("\nYou can sell instead!")
                    
                
                else:
                    print("\nPurchase cancelled.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")


        print(f"\nYou bought Iron for {roundedMoney} coins.")
        money -= roundedMoney
        roundedMoney = round(money, 2)
        _2_inventory.addItem(f"Iron x{amount}")


    elif city == "Lumaria":

        print(f"The price of Fabric is {roundedMoney} coins per unit.")
        buyButton = input("Do you want to buy Fabric? (y/n) ").lower()
        
        if buyButton == "y":
            print("How much Fabric do you want to buy?")
            try:
                amount = int(input("Type the amount: "))
                totalCost = amount * roundedMoney
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
        
    else:
