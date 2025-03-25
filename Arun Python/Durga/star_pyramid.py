def star_pyramid(num):
    for i in range(1,num+1):
        print(" "*(num-i),end="")
        print("*"*i)
num=int(input("enter the number : "))
star_pyramid(num)