
def breakingRecords(scores):
    # Write your code here\
    mini = scores[0]
    maxi = scores[0]
    counterMini = 0
    counterMaxi = 0
    for i in range(len(scores)):
        if mini > scores[i]:
            counterMini += 1
            mini = scores[i]
        elif maxi < scores[i]:
            counterMaxi +=1
            maxi = scores[i]
    return (counterMaxi , counterMini)

         


    

n = int(input().strip())
scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)

print(' '.join(map(str, result)))
print('\n')

