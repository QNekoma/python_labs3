def count(lst):
    total = 0
    number = list(lst)
    while number:
        element = number.pop()
        if isinstance(element, list):
            number.extend(element)
        total += 1
    return total

print(count([])) # 0
print(count([1, 2, 3])) # 3
print(count(["x", "y", ["z"]])) # 4
print(count([1, 2, [3, 4, [5]]])) # 7
