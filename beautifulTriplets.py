
def beautifulTriplets(d, arr):
    # Write your code here
    b = 0
    count = 0
    for i in range(len(arr), 0, -1):
        for x in range(i-1, 0, -1):
            if arr[i-1] - arr[x-1] == d:
                b = arr[x-1]
                for y in range(x-1, 0, -1):
                    if b - arr[y-1] == d:
                        count += 1
            elif arr[i-1] - arr[x-1] > d:
                break
    return count


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(str(result) + '\n')
