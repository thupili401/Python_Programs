str='Sreekanth'
for i in range(len(str)-1,-1,-1):
    print(str[i],end='')
# len(str) - 1: This gives the index of the last character in the string. len(str) is 7, so len(str) - 1 is 6.
# -1: This is the stopping point (exclusive). The loop will stop before reaching -1.
# -1: This is the step, meaning the loop will count down by 1 each time.

str='Sreekanth Reddy'
reversed_string=str[::-1]
print(reversed_string)
#This line uses Python's slicing feature to reverse the string:

# str[start:end:step] is the general form for slicing.
# start is the starting index (optional, defaults to the beginning of the string if not specified).
# end is the ending index (optional, defaults to the end of the string if not specified).
# step is the step value, which determines the stride to take while slicing. Here, -1 means that the slice will go backwards, effectively reversing the string.
# So, str[::-1] creates a new string that is the reverse of str