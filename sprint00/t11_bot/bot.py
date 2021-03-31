

command_list = ['find', 'concat', 'beatbox']
f_str = input("Enter your first string: ")
s_str = input("Enter your second string: ")
if not f_str or not s_str:
    print("One of the strings is empty.")
else:
    command = input("Enter your command: ")
    if command in command_list:
        if command == "find":
            print(f"{bool(s_str in f_str)}")
        elif command == "concat":
            print(f_str + " " + s_str)
        else:
            f_bit = int(input("Enter your first beatbox number: "))
            s_bit = int(input("Enter your second beatbox number: "))
            for i in range(f_bit):
                print(f_str, end="")
            for k in range(s_bit):
                print(s_str, end="")
            print("")
    else:
        print("usage: command find | concat | beatbox")