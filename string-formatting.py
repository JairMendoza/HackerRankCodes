def print_formatted(number):
    # your code goes here
    length = len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(length),oct(i)[2:].rjust(length),hex(i)[2:].rjust(length).upper(),bin(i)[2:].rjust(length))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)