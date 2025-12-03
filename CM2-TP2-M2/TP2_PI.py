#approx pi

n = 1
div = 0
pi = 0

for i in range(0,n+1):
    div+=((-1)**i)/(2*i+1)
    
pi = 4*div
print(pi)