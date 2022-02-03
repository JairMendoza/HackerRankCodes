def cutTheSticks(arr):
    # Write your code here
    pick = []
    while len(arr) != 0:
        pick.append(len(arr))
        mini = min(arr)
        while min(arr) == mini:
            arr.remove(mini)
            if(len(arr) == 0):
                break
        for i in range(len(arr)):
            arr[i] -= mini
            
    return pick
            
        
        
        

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print(result)