dizi = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
dizi_new = []
def flatten(n):
    for i in n:
        if isinstance(i, list): 
            flatten(i)
        else:
            dizi_new.append(i)

flatten(dizi)
print(dizi_new)
