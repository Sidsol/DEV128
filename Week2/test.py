s1 = set('curious')
s2 = set('Marvelous')
print(s1)  # {'c', 'i', 'o', 'r', 's', 'u'}
print(s2)  # {'a', 'e', 'l', 'm', 'o', 'r', 's', 'u', 'v'}
s3 = s1 ^ s2

print(s3)  # {'a', 'c', 'e', 'i', 'l', 'm', 'o', 'r', 's', 'u'}