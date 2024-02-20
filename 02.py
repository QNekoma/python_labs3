def calc_series(j):
    x1 = 1
    x2 = -1/8
    if j == 1:
        return x1
    elif j == 2:
        return x2
    else:
        x_prev_1 = x1
        x_prev_2 = x2
        x = 0
        for i in range(3, j+1):
            x = ((i-1) * x_prev_1) / 3 + ((i-2) * x_prev_2) / 4
            x_prev_2 = x_prev_1
            x_prev_1 = x
        return x

print(calc_series(1))
print(calc_series(2))
