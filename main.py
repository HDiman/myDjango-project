


# def find_lonely(lst):
#     alone_num = [n for n in lst if n + 1 not in lst and n - 1 not in lst and lst.count(n) < 2]
#     return sorted(alone_num)
#
# lst = [16, 30, 5, 5, 5, 3, -1, 0]
# print(find_lonely(lst))

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    profession: str

user1 = User('Alice', 36, 'doctor')
user2 = User('Bob', 24, 'developer')

print (user1, user2)
