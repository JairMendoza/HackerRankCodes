def birthday(s, d, m):
    # Write your code here
    possible = 0
    aux = 0 
    if len(s) == 1:
        if s[0] == d:
            possible = 1        
    else:
        for i in range(len(s)-1):
            aux = 0
            itera2 = 0
            if i + m <= len(s):
                for itera in range(i , m + i):
                    itera2 += 1
                    if i + 1 < len(s):
                        if aux + s[itera] > d:
                            break
                        else:
                            aux += s[itera]  
                            if aux == d and itera2 == m:
                                possible += 1
    print(possible)

s = [6,3,8,6,3,2,8,0]
d = 10
m = 3
birthday(s , d , m )
