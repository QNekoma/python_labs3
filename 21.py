def calculate_recursion(i):
    if i == 1:
        return 1
    elif i == 2:
        return -1/8
    else:
        return ((i-1)*calculate_recursion(i-1))/3 + ((i-2)*calculate_recursion(i-2))/4

# Пример использования для i = 3
result_recursion = calculate_recursion(3)
print(result_recursion)