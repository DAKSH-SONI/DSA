num = [22,56,45,86,31,46,78,90,34,56]
# largest = num[0]
# for i in num:
#     if i > largest:
#         largest = i
# print(largest)
# def largest_element(num):
#     largest = num[0]
#     while num:
#         i = num.pop()
#         if i > largest:
#             largest = i
#     return largest

# print(largest_element(num))
def largest_element(num):
    if not num:
        return None
    largest = num[0]
    for i in num:
        if i > largest:
            largest = i
    return largest
print(largest_element(num))