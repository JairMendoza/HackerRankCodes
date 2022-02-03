def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 < x2 and v2 > v1:
        print('NO')
    elif x1 == x2 and v1 != v2:
        print('NO')
    elif x1 < x2 and v1 > v2:
        direfencia = str((x2 - x1) / (v1 - v2))
        cont = 0
        print(direfencia)
        for i in range(0 , len(direfencia)):
            if direfencia[i] == '.':
                 cont = i 
        if  len(direfencia) >= 3 and direfencia[cont + 1] != '0':
            print('NO')
            print(direfencia)
        else:
            print('YES')
    elif v1 == v2 and x1 != x2:
        print('NO')
    
x1 = int(input())
v1 = int(input())
x2 = int(input())
v2 = int(input())
kangaroo(x1 , v1, x2 , v2)

