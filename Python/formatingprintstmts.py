name="Sreekant T"
Working="Embibe"
Experience=10
Location="Banglore."

#print("My name is "+name+". I am working in "+Working+" from last "+Experience+" years"" and i am stying in "+Location)
print("My name is  {}  I am working in  {} from last  {} years and i am stying in {}".format(name,Working,Experience,Location))
print("My name is  {2}  I am working in  {0} from last  {3} years and i am stying in {1}".format(Working,Location,name,Experience))
print("My name is  %s  I am working in  %s from last  %d years and i am stying in %s"%(name,Working,Experience,Location))
