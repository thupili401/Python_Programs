n1=int(input("ENter the number the 1st number: "))
n2=int(input("ENter the number the 2nd number: "))
n3=int(input("ENter the number the 3rd number: "))
if n1>n2 and n1>n3:
    print("The biggest number is :",n1)
elif  n2>n1 and n2>n3:
    print("The biggest number is :",n2)
elif  n3>n1 and n3>n2:
    print("The biggest number is :",n3)
else:
    print("Enter valid number")