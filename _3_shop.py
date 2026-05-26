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

    "1 - Buy",
    "2 - Leave Shop"
]

shopIronvalle = [
     "===== IRONVALLE SHOP =====",

    "",

    "BUY:",
    "- Iron",
    "- Medicine",

    "",

    "SELL:",
    "- Medicine",

    "",

    "1 - Buy",
    "2 - Sell",
    "3 - Leave Shop"
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
    "2 - Sell",
    "3 - Leave Shop"
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
    "2 - Sell",
    "3 - Leave Shop"
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
    "2 - Sell",
    "3 - Leave Shop"
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