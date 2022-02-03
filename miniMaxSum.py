def miniMaxSum(arr):
    # Write your code here
    mini = sum(arr) - max(arr)
    maxi = sum(arr) - min(arr)
    print('{} {}'.format(mini,maxi))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
