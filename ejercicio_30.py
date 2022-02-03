import string 
def print_rangoli(size): 
    alphabets = string.ascii_uppercase
    for i in range(1, 2 * size): 
        first = "-".join(sorted(alphabets[abs(size - i) : size], reverse=True))           
        last = first[-2::-1] 
        print((first + last).center((4 * size) - 3, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)