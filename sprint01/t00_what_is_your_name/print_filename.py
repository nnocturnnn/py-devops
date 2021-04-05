import os

def print_filename():
    print(os.path.basename(__file__))

if __name__ == "__main__":
    print_filename()