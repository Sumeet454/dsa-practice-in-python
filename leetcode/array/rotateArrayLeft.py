# without using slicing
# def rotateArrayLeft(arr):
#     temp= arr[0]
#     for i in range(1,len(arr)):
#         arr[i-1] = arr[i]
#     arr[len(arr)-1] = temp
#     return arr
# arr = [1,2,3,9,5,6]
# print(rotateArrayLeft(arr))

def rotateArrayLeftByKPosition(arr, k):
    k=k%len(arr)
    temp= arr[0:k]
    for i in range(k,len(arr)):
        arr[i-k]=arr[i]
    j=0
    for i in range(len(arr)-k,len(arr)):
        arr[i]=temp[i-(len(arr)-k)]
        j=j+1
    return arr
arr = [1,2,3,9,5,6]
print(rotateArrayLeftByKPosition(arr, 3))



