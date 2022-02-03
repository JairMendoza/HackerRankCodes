from itertools import count


def birthday(s, d, m):
    # Write your code here
    possible = 0
    aux = []
    if len(s) == 1 and s[0] == d and m == 1:
        possible = 1
    else:
        for i in range((len(s)-m)+1):
            aux = []
            for x in range(i,i + m):
                aux.append(s[x])
            if sum(aux) == d:
                possible +=1
         
    return possible 


if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')

