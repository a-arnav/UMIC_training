
def prime(b):
    global arr
    arr=[2]
    for i in range(2,b):
        for j in range(2,i):
            if i%j==0:
                 break
            elif j==i-1 and i%j != 0:
                arr.append(i)
    print(f'{arr}')
def twinprime():
    twinarr=[]
    a=1
    while True:
        if arr[a]-arr[a-1] <= 2:
            #b=a-1
            #print(f'({arr[b]} and {arr[a]})') 
            twinarr.append(a)
        if a== len(arr)-1:
            break
        a += 1
    with open('myFirstFile.txt','w') as f:
        for i in twinarr:
            f.write(f'{arr[i-1]} {arr[i]}')
            f.write('\n')  
        
a=int(input())
b=10**a -1        
prime(b)
twinprime()