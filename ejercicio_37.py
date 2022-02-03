'''def utopianTree(n):
    # Write your code here
    height = 1
    for i in range(n + 1):
        if i % 2 == 0 and i != 0:
            height += 1
        elif i != 0:
            height = height * 2
    return height
 
t = int(input().strip())  

for t_itr in range(t):
    n = int(input().strip())

    result = utopianTree(n)
    print(result)'''
def odd(n):
    return ((n % 2) == 1);

def even(n):
    return ((n % 2) == 0);

def utopia(n):
    if n == 0:
        return 1;
    elif odd(n):
        return 2 * utopia(n-1);
    elif even(n):
        return 1 + utopia(n-1);
    

t = int(input())

for i in range(0, t):
    n = int(input())
    print(utopia(n))