# def find_lonely(lst):
#     alone_num = [n for n in lst if n + 1 not in lst and n - 1 not in lst and lst.count(n) < 2]
#     return sorted(alone_num)
#
# lst = [16, 30, 5, 5, 5, 3, -1, 0]
# print(find_lonely(lst))

# from dataclasses import dataclass
#
# @dataclass
# class User:
#     name: str
#     age: int
#     profession: str
#
# user1 = User('Alice', 36, 'doctor')
# user2 = User('Bob', 24, 'developer')
#
# print(user1, user2)
# print(user1.name)


# # == Taichi module
# import taichi as ti
# ti.init()
#
# @ti.func
# def is_prime(n: int):
#     result = True
#     for k in range(2, int(n ** 0.5) + 1):
#         if n % k == 0:
#             result = False
#             break
#     return result
#
# @ti.kernel
# def count_primes(n: int) -> int:
#     count = 0
#     for k in range(2, n):
#         if is_prime(k):
#             count += 1
#     return count
#
#
# print(count_primes(10000000))

# lst = [1, 8, 4, 10, 5]
# lst1 = tuple(i**2 for i in lst)

# for ind, num in enumerate(lst1):
#     # lst1.append(num ** 2)
#     # lst1 = lst1 + (num ** 2)
#     print(type(num))
#     print(type(lst1))


# print(sorted(lst))
# print(sorted(lst1, reverse=True))


# lst = [1, 8, 4, 10, 5]
# lst1 = tuple(i**2 for i in lst)
# print(sorted(lst1, reverse=True))
#
# for ind, num in enumerate(lst1):
#     print(lst1[ind])


# my_set = set('hello world')
# # print(type(my_set))
# print(sorted(my_set, reverse=True))


import random
import time

all_try = 0
sum_all = 0
num = 0
sum_num = 5000
# print(sum_num)

def rnd_num():
    rnd_ = random.randint(1, 10)
    return rnd_

while True:
    all_try += 1
    sum_all += num
    if all_try == 100:
        avr = sum_all / all_try
        print(avr)
        break

    while True:
        rnd = rnd_num()
        # print(rnd)

        # time.sleep(0.1)
        if sum_num > 50000:
            print(num, end=" | ")
            print(sum_num)
            break
        elif rnd == 10:
            sum_num += 1000
        else:
            sum_num -= 100
        num += 1
        # print(sum_num)





