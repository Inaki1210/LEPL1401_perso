# indice max d'une liste

def maximum_index(lst):
    max_val = lst[0]
    max_pos = 0
    for i in range(len(lst)):
        if lst[i] >= max_val:
            max_val = lst[i]
            max_pos = i
    return max_pos

print(maximum_index([24,4,-70,-64,-69,78,3]))