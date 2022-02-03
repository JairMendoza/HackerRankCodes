height,wide = map(int, input().rstrip().split())
c = '-'
'''for i in range(wide):
    print((c*i).rjust(wide-1)+c+(c*i).ljust(wide-1))'''
for i in range(wide):
    print('-')