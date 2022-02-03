def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(len(ar)):
        for x in range(i+1 , len(ar)):
            if (ar[i] + ar[x]) % k == 0:
                count += 1
    return count
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(str(result) + '\n')

 