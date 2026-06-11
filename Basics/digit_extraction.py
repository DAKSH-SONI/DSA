# # n = 5873   #REverse a numbe
# # rev = 0
# # while n > 0:
# #     rem = n % 10
# #     rev = rev * 10 + rem
# #     n = n // 10
# # print(rev)

# n = 5873      # count the number of digits in a number
# count = 0
# while n>0:
#     rem = n % 10
#     count += 1
#     n = n // 10
# print(count)    

# from math import *  # log10() function is used to calculate the logarithm of a number to the base 10. It returns the exponent to which the base 10 must be raised to produce the given number. For example, log10(100) would return 2, because 10 raised to the power of 2 equals 100. In the context of counting digits, log10(n) gives us the number of digits in n minus one, so we add 1 to get the total count of digits.
# def count_num_digits(n):
#     if n == 0:
#         return 1
#     return int(log10(n)) + 1
# print(count_num_digits(5873))

# n = 1234  # sum of digits in a number  check lenght and plandrome
# sum = 0
# num = n
# result = 0
# while num!= 0:
#     rem = num % 10
#     result = result * 10 + rem
#     num = num // 10
# if result == n:
#     palandrom = True
#     print("The number is a palandrom")
# else:
#     palandrom = False
#     print("The number is not a palandrom")    

n = 153 # armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example, 153 is an armstrong number because it has 3 digits and 1^3 + 5^3 + 3^3 = 153.
num  = n
nod = 0
result = 0
while num != 0:
    last_digit = num % 10
    nod = nod + 1
    num = num // 10
num = n
while num != 0:
    last_digit = num % 10
    result = result + last_digit ** nod
    num = num // 10
if result == n:
    print("The number is an armstrong number")
else:    
    print("The number is not an armstrong number")    
