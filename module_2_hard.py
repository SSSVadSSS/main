def ranges(a, n=1):  # Функция кратности по степеням 10 (для сдвига результата)
    while a >= 10 ** n:
        n += 1
        continue
    a = n
    return a


print('Введите целое число больше 2: ')
n = int(input())
if n > 2:
    parol = list()  # Список пар для контроля за повторами
    code = int(0)
    for i in range(1, n):
        for j in range(2, n):
            k = i + j
            if k <= n and i != j and n % k == 0:  # проверяем условие кратности для текущей пары
                if [j, i] in parol:
                    continue
                else:
                    parol.append([i, j])  # добавляем в список пару удовлетворяющую условиям
                    ri = ranges(i)
                    rj = ranges(j)
                    code = code * (10 ** (ri + rj)) + i * (10 ** rj) + j  # рассчитываем результат
    print('result = ', code)
else:
    print('Введено неправильное число')
