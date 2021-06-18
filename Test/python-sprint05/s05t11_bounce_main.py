from bounce import run_processes, Ball


if __name__ == '__main__':
    balls_for_queue = [Ball('Red ball', 3),
                       Ball('Blue ball', 1),
                       Ball('Yellow ball', 2),
                       Ball('Green ball', 3)]
    process_args = [('Bob', 3), ('Lexa', 1), ('Mike', 5)]
    run_processes(balls_for_queue, process_args)
    print('---')
    # run with only one process
    run_processes(balls_for_queue, [('Bob', 1)])
    print('---')
    # run with only one ball
    run_processes([Ball('Red ball', 5)], process_args)
