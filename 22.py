def compute_without_recursion(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1/8
    else:
        x_1, x_2 = 1, -1/8
        for i in range(3, n+1):
            x_i = ((i-1) * x_2) / 3 + ((i-2) * x_1) / 4
            x_1, x_2 = x_2, x_i
        return x_1, x_2

# Пример использования для n = 3
result_x1, result_x2 = compute_without_recursion(3)
print("x_1:", result_x1)
print("x_2:", result_x2)
