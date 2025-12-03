#approx ln(2)

n = 3
ln2 = 0

for i in range(1,n+1):
    ln2+=((-1)**(i+1))/(i)
    
print(ln2)