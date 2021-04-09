
def buy_milk(money=0):
    milk = "[milk]"
    price = 25
    count = money // price
    return_str = ""
    if count == 0:
        return 
    else:
        for i in range(count):
            return_str += milk
    return return_str



def buy_bread(money=0):
    bread = "[bread]"
    return_str = ""
    price = 19
    count = money // price
    if count == 0:
        return 
    elif count > 3:
        count = 3
    for i in range(count):
        return_str += bread 
    return return_str
