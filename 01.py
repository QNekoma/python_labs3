def count(lst):
    if not lst:
        return 0
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += count(element)
        total += 1
    return total

print(count([]))  # 0
print(count([1, 2, 3]))  # 3
print(count(["x", "y", ["z"]]))  # 4
print(count([1, 2, [3, 4, [5]]]))  # 7

