
def get_anonymous(books):
    new_books = []
    for i in books:
        if i.find(" by ") == -1:
            new_books.append(i)
    return new_books
