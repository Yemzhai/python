# list1 = [1,2,3]
# list2 = [i*2 for i in list1];
# print(list2)
# -------------------------------------
# import math
# def isPrime(x):
#     if(x == 1): return false
#     for i in range(2, int(math.sqrt(x)+1)):
#         if(x % i == 0): return False
#     return True

# list1 = list(range(1,20))

# list2 = [i for i in list1 if isPrime(i)]
# print(list2)
# ------------------------------
# lst1 = [3,46,7]
# lst2 = [1, 1, 1]
# lst3 = zip(lst1, lst2);
# for i in lst3:
#     print(i)
# -------------------------------
# iterator
# lst1 = [2, 4, 5, 6, 1]
# it = iter(lst1)

# print(next(it))
# -------------------------------
# generator
# def gen():
#     n = 1
#     print('first')
#     yield n

#     n = 2
#     print('second')
#     yield n

#     n = 3
#     print('third')
#     yield n

# a = gen() #a->iterator
# print(next(a))
# print(next(a))
# print(next(a))
# //////////////
# def fib():
#     a = 1
#     b = 2
#     while True:
#         yield a, b
#         a, b = b, a+b

# it_fib = fib();
# print(next(it_fib))
# print(next(it_fib))
# print(next(it_fib))
# print(next(it_fib))
# //////////////////
# import math
# def isPrime(x):
#     if(x == 1): return False
#     for i in range(2, int(math.sqrt(x))+1):
#         if(x % i == 0): return False
#     return True

# def next_prime():
#     n = 2
#     while True:
#         while not isPrime(n):
#             n += 1
#         yield n
#         n += 1

# prime = next_prime()
# for i in range(0, 10):
#     print(next(prime))
# -------------------------------
# CLASS
class Student:
    def __init__(self, name, surname, gpa):
        self.name = name;
        self.surname = surname
        self.gpa = gpa

    def calc_gpa(self):
        return self/2
a = Student("Isa", "Yemzhai", 3)
b = Student("Nu", "Ne", 3)
print(a.name, a.surname, a.gpa)
print(b.name, b.surname, b.gpa)
print(a.calc_gpa())