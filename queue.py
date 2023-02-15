from time import sleep
from threading import Thread


one_queue = list()
multi_queue = list()


def client_queue(name):
    queue = eval(input('how many bread do you want?'))
    counter = 0
    if queue == 1:
        counter +=1
        one_queue.append(counter)
        print(f"{name} is starting... , you are in one queue please wait ..... {counter} person in queue.")
        sleep(10)
        print(f"your {queue} bread is ready .")
    elif queue > 1:
        counter +=1
        multi_queue.append(counter)
        print(f"{name} is starting... , you are in multi queue please wait ..... {counter} person in queue.")
        sleep(10)
        print(f"your {queue} bread is ready .")


class DoThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        client_queue(self.name)


thread_one = DoThread('first thread')
thread_two = DoThread('second thread')
thread_one.start()
thread_two.start()
thread_one.join()
thread_two.join()
