a=[1,2,3,4,5]
y=[2,4,5,1,5,0,9,8,3,5,7,3,6,2,9,9,3,]
for i in range(len(y)):
    print(y[i])
print("-----------")
for i in y:
    print(i)
print("-----------")

i=0
while i<len(y):
    print(y[i])
    i+=1
print("-----------")

a=[9,3,5,8,45,23,23,56,2,7]
a.append(6)  # to add 6 in the last of list
print(a)
a.insert(2,9) #adding 9 at index 2
print(a)
a.remove(5)
print(a)
a.pop(2) #will remove index 2 element of the list
print(a)
a.pop()#will remove last
print(a)
a.reverse() #will reverse the list
print(a)
a.sort()
print(a)
b=[2,[3,4,5,6],7,8] #nested index
print(b[1])
print(b[1][2])

x=[9,4,2,4,1,8,3,6,5,7]
print(x[1:5])
print(x[0:3])
print(x[1:])
print(x[:])

y=[2,4,5,1,5,0,9,8,3,5,7,3,6,2,9,9,3,]
print(y.count(9))
print(5 in y)
x.extend(y)
print(x)