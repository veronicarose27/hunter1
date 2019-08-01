m,n=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in l:
    if i in m:
        print("YES")
        break
else:
    print("NO")
