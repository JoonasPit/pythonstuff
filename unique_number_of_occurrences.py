def uniqueOccurrences(arr) -> bool:
    newarray = []
    for i in set(arr):
        newarray.append(arr.count(i))

    if len(set(newarray)) == len(newarray):
        return True
    else:
        return False
