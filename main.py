import random
import time

def rnd_num():
    r = random.randint(1, 10)
    return r

while True:
    time.sleep(5)
    print(rnd_num())


