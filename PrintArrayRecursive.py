arr=[2,3,4,5,6]
n=len(arr)
def f(arr,i=0):
    if i==n:
        return
    else:
        print(arr[i])
        f(arr,i+1)
f(arr,0)
		
