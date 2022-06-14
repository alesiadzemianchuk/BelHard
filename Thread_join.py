from threading import Thread
from time import sleep


def func():
    for i in range(5):
        print(f'from {i}')
        sleep(0.5)



th = Thread(target=func)
th.start()
for i in range(5):
    print(f'from main {i}')
    sleep(1)

th1 = Thread(target=func)
th2 = Thread(target=func)
th1.start()
th2.start()
th1.join()
th2.join()
print('Stop')
