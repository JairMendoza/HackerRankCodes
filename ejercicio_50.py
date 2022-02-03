'''from collections import defaultdict
n , m = map(int, input().split())
groupN = defaultdict(list)
groupM = defaultdict(list)

for i in range(n):
    groupN[i].append(input())
for i in range(m):
    groupM[i].append(input()) 


print(groupM[])
print(groupN)'''
from collections import defaultdict
d = defaultdict(list)
list1=[]
n, m = map(int,input().split())
for i in range(1, n+1):
    d[input()].append(str(i))


for i in range(m):
    b = input()
    if b in d: print(' '.join(d[b]))
    else: print(-1)


