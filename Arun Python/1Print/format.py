Name="Sreekanth"
Age=35
Designation="Product Engineer"
print("My name is "+Name+"My age is "+str(Age)+" and my designation is "+Designation)
print("My name is ",Name ,"My age is",Age,"and my designation is ",Designation)# if we use , no need to typecast the variable
print("My name is {},my age is {} and my designation is {}".format(Name,Age,Designation))
print("My name is {2},my age is {1} and my designation is {0}".format(Designation,Age,Name))
print("My name is %s, my age is %d, and my designation is %s" %(Name,Age,Designation))#%g is used to remove floating point
print(f"My name is {Name},my age is {Age} and my designation is {Designation}")
