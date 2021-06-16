import time
from multiprocessing import Process, Queue
from queue import Empty


# leave class Ball as is, don't edit it
class Ball:
    def __init__(self, name, n_bounces):
        self.name = name
        self.n_bounces = n_bounces

    def __str__(self):
        return f'{self.name} ({self.n_bounces})'


# edit the function as described in comments
def bounce(name, delay, task_queue, done_queue):
    while True:
        time.sleep(delay)

        # write you code here
        # required actions:
        # - stop if done_queue is full

        try:
            pass  # replace with your code
            # required actions:
            # - get a ball from task_queue (wait for it max 1 second)
        except Empty:
            print(f'queue.Empty exception.')
        else:
            pass  # replace with your code
            # required actions:
            # - update the ball's counter
            # - put ball either back to the task_queue, or to the done_queue
            print('replace me')  # edit contents of the message


# edit the contents of this function in the allowed section
def run_processes(balls, args):
    processes = []
    task_queue = Queue()
    done_queue = Queue()  # edit to make done_queue limited to the correct size

    # write your code here
    # required actions:
    # - create and start processes for each item of args
    # - put all the balls into the task_queue

    for p in processes:
        p.join()
