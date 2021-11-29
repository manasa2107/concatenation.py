l=list(map(str,input().split(',')))
s=0
l2=''
m=l.index('5')
t=l.index('8')
for i in range(m):
    s+=int(l[i])
for i in range(t+1,len(l)):
    s+=int(l[i])
#print(s)
for i in range(m,t+1):
    l2+=l[i]
print(int(l2)+s)
    