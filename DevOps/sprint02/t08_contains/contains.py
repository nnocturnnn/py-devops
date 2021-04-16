




def contains(string,list_str):
    new_list = []
    string = string.lower()
    for i in list_str:
        if string.find(i.lower()) > -1:
            new_list.append(i)
        if string == i.lower():
            new_list.append(i)
    return new_list
