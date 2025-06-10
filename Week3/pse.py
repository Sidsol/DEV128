# list = [1, 2, 4, 5] 
# list = [1, 1, 1, 1] 
# list = [97, 51, 49, 35, 3, 65] 
list = [1 , 5, 7, -1, 5] 

target = 6 
# target = 2
# target = 100

# Create a set
my_set = {}

print(my_set)

count = 0
# for i in list:
#     lookup = target - i
#     print(f"Looking for {lookup} to pair with {i}.")
#     if i in my_set:
#         my_set[i].append(lookup)
#         count += 1
#         # Print the pair found
#         print(f"Pair found: {i}, {lookup}")
#     else:
#         my_set[lookup] = [lookup]
#         # Print the set after each addition
#         print(f"Adding {i} to the set.")
#     print(my_set)
    
    
for i in list:
    # lookup = 100 - 97 = 3
    lookup = target - i
    
    # Check if the complement exists in the dictionary
    if lookup in my_set:
        count += my_set[lookup]
        # Print the pairs found
    
    # Add the current number to the dictionary or update its count
    if i in my_set:
        my_set[i] += 1
    else:
        my_set[i] = 1
        
    print(my_set)
    print(count)

print(count)


