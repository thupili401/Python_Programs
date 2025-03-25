"""a=[1,2,6,4,12,2,3]
for i  in  range(len(a)):
    print(a[i])
a=[6,2,9,3,4,6,7,7,3,2,2,2,3,4]
print(a)
a[2]=3
print(a)
a.append(4)
print(a)
a.insert(2,5)
print(a)
a.pop(2)
print(a.pop())
print(a)
a.reverse()
print(a)
a.sort()
print(a)
print(a.index(6))
print(a.count(2))
print(max(a))
print(min(a))
print(sum(a))
print(type(a))
print(a)
del a
print(a)"""
x=[1,2,3,4]
y=[5,6,7,8]
#z=x+y
#print(z)
x.extend(y )
print(x)