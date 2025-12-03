#approximation de pi avec factorielles

def factorial(n):
    sum=1
    if n <= 1:
        return 1
    else:
    	for i in range(1,n+1):
        	sum*=i
        return(sum)
    
def approx_sin(n):
    sin = 0
    i = 0
    while i <= n:
        num = (-1)**i
        denom = factorial(2*i+1)
        sin+=num/denom
        i+=1
    return sin

print(approx_sin(3))
        