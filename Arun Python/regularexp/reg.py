import re
pattern="sreekanth"
pattern="[Ss]reekanth"

print("Enter the text")
text=input()

if re.search(pattern,text):
    print("pattern is matched")
else:
    print("Pattern not matched")