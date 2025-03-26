def seq_arr(st):
    letters=[]
    numbers=[]
    for i in st:
        if i.isalpha():
            letters.append(i)
        elif i.isdigit():
            numbers.append(i)
    letters.sort()
    numbers.sort()
    print(' '.join(letters)+ ' '.join(numbers))
st=input('Enter the alphanuamric : ')
seq_arr(st)