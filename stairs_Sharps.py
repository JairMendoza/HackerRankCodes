n = int(input())

for x in range(n):
    sharps = ''
    for i in range(n , 0 , -1):
        if i <= x + 1:
            sharps += '#' 
        else:
            sharps += ' '
    print(sharps)

#A better way to do
for i in range(1,n+1):
        print(' '*(n-i)+'#'*(i))