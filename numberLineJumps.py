def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 < x2 and v1 > v2:
        diference = str((x2 - x1) / (v1 - v2))
        if diference[diference.index('.') + 1] != '0':
            return('NO')
        else:
            return('YES')
    else:
        return('NO')
    
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result + '\n')

    
