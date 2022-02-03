def minion_game(string):
    # your code goes here
    vocales = ['A','E','I','O','U']
    stuart = 0
    kevin = 0
    for i in range(len(s)):
        if s[i] in vocales:
            kevin += (len(s)-i)
        else:
            stuart += (len(s)-i)
    if kevin > stuart:
        print("Kevin {}".format(kevin))
    elif stuart > kevin:
        print("Stuart {}".format(stuart))
    else:
        print("Draw")
                

if __name__ == '__main__':
    s = input()
    minion_game(s)