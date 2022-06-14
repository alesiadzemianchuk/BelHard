from threading import Thread, Event

event = Event()

def worker(name: str):
    event.wait()
    print(f'\n Worker: {name}')


event.clear()
workers = [Thread(target=worker, args=(f'wrk {i}', )) for i in range(5)]
for w in workers:
    w.start()
print('Main')
event.set()
print(event.is_set())
