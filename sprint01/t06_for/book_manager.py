
def get_anonymous(books):
    for i in books:
        list_word = i.split()
        if "by" in list_word:
            books.remove(i)
        else:
            continue
    return books
