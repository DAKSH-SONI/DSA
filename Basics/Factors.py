num = int(input("Enter a number: ")) # find factors of a number
factors = []
# for i in range(1, num+1):
#     if num % i == 0:
#         factors.append(i)
# print(f"Factors of {num}: {factors}")

#"optimal solution"

for i in range(1 , int(num**0.5) + 1):
    if num % i == 0:
        factors.append(i)
        # Avoid adding duplicate factors when num is a perfect square
        if i != num // i: # 6  is divide by 36 and 6*6 = 36 so we need to avoid adding 6 twice
            factors.append(num // i)
factors.sort()
print(f"Factors of {num} : {factors}")
