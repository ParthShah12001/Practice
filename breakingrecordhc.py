a =int(input())
c=0
d=0
rec = list(input().strip().split(' '))
max = int(rec[0])
min = int(rec[0])
for i in range(1,len(rec)):
    if int(rec[i])>int(max):
        max = rec[i]
        c+=1
    if int(rec[i])<int(min):
        min = rec[i]
        d+=1
print(c,d)
