def chocolateFeast(n, c, m):
    # Write your code here
    nChocolates = n // c
    env = nChocolates
    while True: 
        if env >= m:
            nChocolates += env // m
            cambios = env // m
            env -= m * (env//m)
            env += cambios
        else:
            return nChocolates
            break    

        



if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        print(str(result) + '\n')

