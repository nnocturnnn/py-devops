
def byu_milk(money=0):
    milk = "[milk]"
    price = 25
    count = money // price
    if count == 0:
        print("None")
    else:
        for i in range(count):
            print(milk,end="")
    print()



def buy_bread(money=0):
    bread = "[bread]"
    price = 19
    count = money // price
    if count == 0:
        print("None")
    elif count > 3:
        count = 3
        for i in range(count):
            print(bread,end="")
    print()
