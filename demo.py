pos = -1

def search(lst, n):
    for i in range(len(lst)):
        if lst[i] == n:
            globals()['pos'] = i
            return True
    return False

lst = [5, 8, 4, 6, 9, 2]
n = 9

if search(lst, n):
    print("Found at", pos)
else:
    print("Not found")
