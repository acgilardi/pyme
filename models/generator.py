import random


def lottery():
    for i in xrange(6):
        yield random.randint(1, 40)

    yield random.randint(1, 15)
