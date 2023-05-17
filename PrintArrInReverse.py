arr=[2,3,4,5,6]
n=len(arr)
def f(arr,n):
    if n==0:
        return
    else:
        print(arr[n-1])
        f(arr,n-1)
f(arr,n)
