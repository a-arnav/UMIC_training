import sys
def palindromeplus(a):
    for i in range(a+1,sys.maxsize):
        if str(i)==str(i) [::-1]:
            return i
    
a=int(input())
print(f'{palindromeplus(a)}')