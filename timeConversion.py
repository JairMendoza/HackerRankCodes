from errno import ESTALE


def timeConversion(s):
    # Write your code here
    if s[len(s)-2] == 'P':
        if s[0:2] == '12':
            s = s[0:len(s)-2]
        else:
            hora = int(s[0:2]) + 12
            s = s.replace(s[0:2],str(hora))
            s = s[0:len(s)-2] 
    else:
        if s[0:2] == '12':
            s = s.replace(s[0:2], '00')
            s = s[0:len(s)-2]
        else:
            s = s[0:len(s)-2] 
    return s 


if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result + '\n')
