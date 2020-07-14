a=1
while a<100:
    a+=1
    if a%7==0:
        continue
    if a%10==7:
        continue
    if a//10==7:
        continue
    print(a)
