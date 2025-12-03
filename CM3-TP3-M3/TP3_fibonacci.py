#suite de Fibonacci

def fibonacci(n):
    """
    pré : n, le terme de la suite de fibonacci recherché
    post : revoye le n ième terme de la suite de fibonacci
    """
    if n == 0:
        return l
    l=[0]
    terme = 1
    for i in range(n):
        terme+=l[i-1]
        l.append(terme)
    return terme