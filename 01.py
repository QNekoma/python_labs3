def count_rcursive(lst):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_recursive(item)
        else:
            count += 1
    return count

print(count_recursive([]))
print(count_recursive([1, 2, 3]))
print(count_recursive(["x", "y", ["z"]]))
print(count_recursive([1, 2, [3, 4, [5]]]))
