
input()
ranked = list(map(int,input().split()))
input()
player = list(map(int,input().split()))



# Write your code here
playerRank = []
pranck = []
for o in range(len(player)):
    ranked.append(player[o])
    playerRank = list(set(ranked))
    playerRank.sort(reverse = True)
    print(playerRank.index(player[o]) + 1)
