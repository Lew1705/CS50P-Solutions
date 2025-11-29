amount_due = 50
while amount_due > 0:
    print(f"Amount due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in [25,10,5]:
        amount_due -=coin

if amount_due < 0:
        change = amount_due + coin
        print(f"Change owe {change}")
