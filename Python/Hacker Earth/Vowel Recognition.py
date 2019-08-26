t=int(input())
v=['a','e','i','o','u','A','E','I','O','U']
for i in range(t):
    a=input()
    vowel=[]
    count=0
    for i in range(len(a)):
        if(a[i] in v):
            count=count+((len(a)-i)*(i+1))
    print(count)
