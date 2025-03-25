"""""table= int(input("Enter the Table which you want :"))
i=1
while i<=10:
    result=table*i
    print(result)
    i+=1

table= int(input("Enter the Table which you want :"))
for i in range(1,11):
    result= i*table
    #print(str(table)+"*"+str(i)+"="+str(result))
    print(table, "*",i,"=" ,i*table)"""

table= int(input("Enter the Table which you want :"))
for i in range(10,0,-1):
    result= i*table
    print(table, "*",i,"=" ,i*table)