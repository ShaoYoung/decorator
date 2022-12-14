# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]
# 1.1 (**) с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)

# импортируем декораторы
import decorators as dec


@dec.logger
# @dec.prec_timer
@dec.cacher
def seq(n):
    seq_list = [(1 + i) ** i for i in range(0, n + 1)]
    return seq_list


def main():
    print(seq(3))
    print(seq(8))
    print(seq(12))
    print(seq(18))
    print(seq(50))
    print(seq(3))
    print(seq(8))
    print(seq(12))
    print(seq(50))


# Это стандартный код, который защищает пользователей от случайного вызова сценария, когда они не собирались этого делать,
# и его применение является хорошей практикой.
# код в if выполнится только при запуске файла main.py
# Если файл импортируется в качестве модуля, то код в if не выполнится, т.к. переменной __name__ будет присвоено другое имя
# быстрый вызов ctrl+j (Windows)
if __name__ == '__main__':
    main()
