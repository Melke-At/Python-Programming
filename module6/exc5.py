def even_no(y):
    lists = []
    for i in y:
        if i%2 == 0:
            lists.append(i)
    return lists
y = [1,2,3,4,5,6,7]
print(even_no(y))