print("sreekanth is good boy")
try:
    a=10/0
except ZeroDivisionError as z:
    print("Exception Handled : ",z)
except TypeError as y:
    print("Exception handled : ",y)
except NameError as x:
    print("Exception handled :",x)
print("end of the program")