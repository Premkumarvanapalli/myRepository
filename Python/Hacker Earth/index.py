def find(x):
     i=0
     index=1
     while(i+index<=x):
          i=i+index
          index+=1
     return i

n=int(input())
li=list(map(int,input().split()))
for i in range(len(li)-2,0,-1):
     li[i]=li[i]+li[i+1]
print(*li)
