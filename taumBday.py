from calendar import c


def taumBday(b, w, bc, wc, z):
    # Write your code here
    if z + min(bc , wc) >= max(bc , wc):
        return (b * bc) + (w * wc)
    else:
        if b * wc + z < b * bc:
            return b * wc + (b*z) + w * wc
        else:
            return w * bc + (w*z) + b * bc

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        print(str(result) + '\n')


