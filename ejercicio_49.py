'''def store(y,p):
    earn = 0
    for i in range(len(p)):
        if p[i][0] in y:
            earn += p[i][1]
            ind = y.index(p[i][0])
            y.pop(ind)
    return earn



x = int(input())
y = list(map(int, input().split()))
n = int(input())
p = []
for i in range(n):
    p.append( list(map(int, input().split())))
print(store(y,p))'''
import collections

numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numCust = int(input())

income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print (income)
    