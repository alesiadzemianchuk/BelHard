from threading import Thread, BoundedSemaphore
from time import sleep, time


ticket_office = BoundedSemaphore(value=2)


def ticket_buyer(number):
    start_service = time()
    with ticket_office:
        sleep(5)
        print(f'client {number}, service time: {time()-start_service} \n')


buyer = [Thread(target=ticket_buyer, args=(i,)) for i in range(6)]
for b in buyer:
    b.start()
