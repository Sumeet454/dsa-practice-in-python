def moveZeroesEnd(arr):
    n=len(arr)
    j=-1
    for i in range(n):
        if arr[i]==0:
            j=i
            break
    for i in range(j+1,n):
        if arr[i]!=0:
            arr[i],arr[j] = arr[j],arr[i]
            j=j+1
    return arr


arr = [1,2,0,0,5,6,7]
print(moveZeroesEnd(arr))