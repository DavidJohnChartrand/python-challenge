def sum(arry):
    _sum = 0

    for i in arry:
        _sum = _sum + i
    
    return(_sum)

def mean(arr):
    mean_ = sum(arr)/len(arr)

    return(mean_)

# to get the difference between values in an array you need to make a new array
# then you need to take the first number and subtract the second
# def Dif(array_):
    

Ar=[1, 2, 3]
ArDiff=[]
for i in range(len(Ar)-1):
        ArDiff.append(Ar[i+1] - Ar[i])
    
print(Ar[1])
print(sum(Ar))
print(mean(Ar))
print(ArDiff)