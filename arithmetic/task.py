def score(tem, th):

    count = 0
    for i in tem:
        if i >= th:
            count += 1
    return count



threshold = 25
temperatures = [20, 25, 27, 22, 30, 28, 24]
result = score(temperatures, threshold)
print(f'Количество элементов выше порога {result}')