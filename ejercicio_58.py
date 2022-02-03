from typing import Counter


def acmTeam(topic):
    # Write your code here
    confirm = ''
    confirm2 = ''
    confirm3 = []
    maxim = 0
    teams = 0
    for i in range(len(topic)):
        for u in range(i+1 , len(topic)):
            confirm = topic[i] + topic[u]
            confirm2 = ''
            for y in range(int(len(confirm)/2)):
                confirm2 += max(confirm[y],confirm[y+5])
            
            if confirm2.count('1') >= maxim:
                maxim = confirm2.count('1')
                confirm3.append(confirm2)
    teams = confirm3.count(confirm3[len(confirm3)-1])
    return maxim , teams

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print(result)
