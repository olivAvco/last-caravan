import random
import time

money = 100
travelCost = 8
hotelCost = 1
inventory = 20
day = 1

    # preços do dia
buyPrice = round(random.uniform(3.80, 4.20), 2)
sellPrice = round(random.uniform(4.00, 4.60), 2)

print(f"\nBuy price: R${buyPrice}")
print(f"Sell price: R${sellPrice}")

    # cálculo do lucro
totalBuy = buyPrice * inventory
totalSell = sellPrice * inventory

profit = totalSell - totalBuy - travelCost

print(f"Possible profit: R${profit:.2f}")

    
money -= hotelCost