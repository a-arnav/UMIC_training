n=int(input())
arr=[]

inp = input()
arr  = inp.split()
    
arr2=arr.copy()
arr2.sort()
profit=int(arr2[n-1])-int(arr2[0])
print(profit)
print(int(arr.index(arr2[0]))+1)
