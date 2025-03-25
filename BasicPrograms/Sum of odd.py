start=int(input("Enter starting number"))
end= int(input("Enter the ending number"))
result=0

for i in range(start,end):
     if (i%2==0):
         result=result+i

print("sum of even number is ",result)