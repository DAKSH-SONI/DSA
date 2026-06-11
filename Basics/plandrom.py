str = "abcddca"
# l = 0
# r = len(str) - 1
# while l < r:
#     if str[l] != str[r]:
#         print("It's not a palindrome")
#         break
#     l += 1
#     r -= 1
# else:
#     print("It's a palindrome")

def is_palindrome(s,l,r):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return is_palindrome(s,l+1,r-1)
print(is_palindrome(str,0,len(str)-1))