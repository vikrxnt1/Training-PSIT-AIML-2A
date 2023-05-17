n=5
def f(i=0):
    if i==5:
        return
    else:
        print(n-1-i+1)
        f(i+1)
f()
		
