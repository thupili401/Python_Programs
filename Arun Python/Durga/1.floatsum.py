numbers=input('enter the three numbers : ')
float_numbers = [float(num) for num in numbers.replace(",", " ").split()]
total=sum(float_numbers)
print(total)