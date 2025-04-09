s=input()
cnt1=0
cnt2=0
for i in s:
    if i.islower():
        cnt1+=1
    if i.isupper():
        cnt2+=1
if cnt1 >= cnt2:
    print(s.lower())
else:
    print(s.upper())