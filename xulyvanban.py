import re
doc=''
while True:
    try: doc+=input()
    except:break
sentence=re.split('[.?!]',doc)
for cau in sentence:
    if len(cau)==0:
        continue
    cau=cau.lower().split()
    cau[0]=cau[0][:1].upper()+cau[0][1:]
    print(' '.join(cau))  