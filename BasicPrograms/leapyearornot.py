a=int(input("Enter the year: "))
if (a%4==0 and a%100!=0)or (a%400==0):
    print(a,"is leap Year")
else:
    print(a,"is not leap year")