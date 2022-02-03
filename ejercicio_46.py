def merge_the_tools(string, k):
    # your code goes here
    strings= []
    for i in range(1,len(string)+1):
        if i % k == 0:
            strings.append(string[(i)-k:i])
    for i in range(len(strings)):
        strings[i] = "".join(dict.fromkeys(strings[i]))
        print(strings[i])
    
             
        
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)