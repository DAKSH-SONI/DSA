# def func(n):
#     if n == 1:
#         return 1
#     return n + func(n-1)
# x =int(input("Enter a number: "))
# print(func(x))

def func(n):
    if n == 0:
        return 1
    return n * func(n-1)
x =int(input("Enter a number: "))
print(func(x))