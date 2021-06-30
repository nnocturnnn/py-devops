


def write_file(filename,arg_str="None"):
    if not filename.endswith(".txt"):
        print('Please enter the filename in the format "filename.txt".')
        print(f'Failed to write to file "{filename}".')
    else:
        with open(filename, "w") as file_handler:
            file_handler.write(arg_str)
        with open(filename, "r") as file_handler:
            var = file_handler.read()
            if var is None or var != arg_str:
                print("Something went wrong...")
            else:
                print(f'Your message has been written to file "{filename}".')
                print(f'File "{filename}" now contains the following text:\n{arg_str}')
    