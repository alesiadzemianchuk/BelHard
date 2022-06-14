from time import sleep

def print_counter():
    counter = 0
    while True:
        print(counter)
        yield
        counter += 1

def print_hi():
    counter = 0
    while True:
        if counter % 3 == 0:
            print('Hi')
        counter += 1
        yield


def main(queue):
    while True:
        gen = queue.pop(0)
        next(gen)
        queue.append(gen)
        sleep(0.5)

if __name__ == '__main__':
    gen1 = print_counter()
    gen2 = print_hi()
    gen_queue = [gen1, gen2]
    main(gen_queue)



