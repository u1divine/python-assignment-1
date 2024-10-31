def machine():
    total=0
    coins= [5,10,25]
    cost=50
    while total<cost:
        coin= int(input("Insert a coin between 5,10 and 15: "))
        if coin in coins:
            total += coin
        else:
            print("Please enter 5,10 or 25")
    change = total-cost
    if change >0:
        print (f"change is {change} cents")
    else:
        print ("No change owed")
machine()