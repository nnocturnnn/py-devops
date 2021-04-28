


def read_file(arg_str):
    try:
        with open(arg_str, "r") as file_handler:
            var = file_handler.read()
            print(f"File {arg_str} has the following message:\n{var}")
    except :
        print(f"Failed to read file {arg_str}.")
    
