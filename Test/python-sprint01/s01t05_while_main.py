# s01t05_while_main.py
from bookshelf import add_to_bookshelf


def print_bookshelf(shelf, updated):
    print(f'* Bookshelf. Updated: {updated} *', *shelf, '***\n', sep='\n')


if __name__ == '__main__':
    bookshelf = ['To Kill a Mockingbird', 'Little Women', '1984',
                 '---', 'Sense and Sensibility', '---', 'Lord of the Flies']
    print_bookshelf(bookshelf, False)

    was_updated = add_to_bookshelf('The Stranger', bookshelf)
    print_bookshelf(bookshelf, was_updated)

    was_updated = add_to_bookshelf('Dracula', bookshelf)
    print_bookshelf(bookshelf, was_updated)

    # adding a book to a full bookshelf
    was_updated = add_to_bookshelf('The Raven', bookshelf)
    print_bookshelf(bookshelf, was_updated)
