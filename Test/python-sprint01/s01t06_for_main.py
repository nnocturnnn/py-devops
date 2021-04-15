# s01t06_for_main.py
from book_manager import get_anonymous

if __name__ == '__main__':
    books = ['The Canterbury Tales by Geoffrey Chaucer',
             'A Separate Peace by John Knowles',
             'Mythology by Edith Hamilton',
             'Moby-Dick or, the Whale',
             'The Awakening by Kate Chopin',
             'Frankenstein',
             'Much Ado About Nothing by William Shakespeare',
             'Oliver Twist by Charles Dickens',
             'The Arabian Nights',
             'The Dream of the Red Chamber'
             ]
    print(*get_anonymous(books), '***', sep='\n')
    # test cases for error management
    print(*get_anonymous([
        'The Crucible by Arthur Miller',
        'The Crucible byby Arthur Miller',  # error: no space after 'by'
        'The Crucible by by Arthur Miller',
        'The Crucible byArthur Miller',  # error: no space after 'by'
        'The Crucibleby Arthur Miller',  # error: no space before 'by'
        'The Crucible     by     Arthur Miller',
        'The Crucible by Arthur Miller by Arthur Miller',
        'by Arthur Miller The Crucible',  # error: no space before 'by'
        ' by Arthur Miller The Crucible',
        ' by '
    ]), sep='\n')
