s='a1b2c3d4e5'
letters=[]
numbers=[]
for i in s:
    if i.isalpha():
        letters.append(i)
    elif i.isdigit():
        numbers.append(i)
letters.sort()
numbers.sort()
result=''.join(letters)+''.join(numbers)
print(result)

