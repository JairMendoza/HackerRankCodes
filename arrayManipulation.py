from re import A


def arrayManipulation(n, queries,):
    # Write your code here
    arra = [0 for i in range(n)]
    for x in range(len(queries)):
        for p in range((queries[x][0] - 1), (queries[x][1])):
            arra[p] += queries[x][2]
    return max(arra) 




if __name__ == '__main__':
    

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')

