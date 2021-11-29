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

 #  or using slicing 
    
l= list(map(int,input().split(",")))
n1= sum(l[:l.index(5)]) + sum(l[l.index(8) + 1:])
l =l[l.index(5):l.index(8) + 1]
n2= ""
for i in l:
   n2 += str(i)
print(int(n2)+n1)

    
