list_1 = [1,1,2,23,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
# frequency = {}
# for i in list_1:
#     if i in frequency:
#         frequency[i] += 1 # if the element is already in the frequency dictionary, increment its count by 1
#     else:
#         frequency[i] = 1 # if the element is not in the frequency dictionary, add it with a count of 1
# print(frequency)  

hash_map = {}
for i in range(0,len(list_1)):
    hash_map[list_1[i]] = hash_map.get(list_1[i],0) + 1 # using the get method to retrieve the current count of the element, and incrementing it by 1
print(hash_map)