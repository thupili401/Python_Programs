My_first="sreekanth reddy"
My_last=str("Thupili")
print(My_last)
print(My_first)
for i in My_first:
    print(i)
for k in range(len(My_last)):
    print(My_last[k])
print("sree" in My_first)
print("Thu"  not in My_last)

print(My_last[1:3])
print(My_first.lower())
print(My_first.upper())
print(My_first.strip()) # to remove leading  and trailing spaces not space btwn two words
print(My_first.replace("e","i"))

name="My Name Is Thupili Sreekanth Reddy"
k=name.split(" ")
for i in k:
    print(i)
print(My_first.capitalize()) #first letter of the word will capitilise
print(My_first.title())# capital first letter of every word

title= "my name is sreekanth i am working in embibe. embibe is good company."
print(title.count("embibe"))

name1="sree"  ##comparing two strings
name2="Sree"
name3="kanth"
print(name1==name2)
print(name1.__eq__(name3))
print(name1.casefold()==name2.casefold())