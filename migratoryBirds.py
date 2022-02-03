from itertools import count


def migratoryBirds(arr):
    # Write your code here
    types = list(set(arr))
    maxTypes = []
    maxi = 0
    for i in range(len(types)):
        if maxi <= arr.count(types[i]):
            maxi = arr.count(types[i])
    for i in range(len(types)):
        if arr.count(types[i]) >= maxi:
            maxTypes.append(types[i])
    return min(maxTypes)


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result) + '\n')
