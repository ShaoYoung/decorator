# Декораторы
import datetime
import time
from functools import wraps


# Точный таймер. с использованием time.perf_counter_ns() возвращает [результат выполнения функции, время выполнения функции]
# - Можно добавить к результату работы декорируемой функции или в будущем использовать отдельно от логера
def prec_timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        res = func(*args, **kwargs)
        finish = time.perf_counter_ns()
        run_time = (finish - start) / 10 ** 6
        # print(f'Время выполнения: {(finish - start) / 10 ** 6} ms')
        return [res, run_time]

    return wrapper


# Грубый таймер. В Windows время.time () имеет точность ~ 16 миллисекунд, т.е. разница меньше 16 ms -> 0
def rough_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        # print(start)
        res = func(*args, **kwargs)
        time.sleep(0.000001)
        finish = (time.time_ns())
        # print(finish)
        # время выполнения
        run_time = (finish - start - 1000) / 10 ** 6
        print(f'Время выполнения {run_time} ms')
        # print(f'Время выполнения {finish - start} ns')
        return res

    return wrapper


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        wraps docs - логгер (с замером времени выполнения функции)
        :param args:
        :param kwargs:
        :return:
        """
        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        log_msg += f'Функция: {func.__name__}\t'
        log_msg += f"Параметры: {', '.join(map(str, args))}\t"
        start = time.perf_counter_ns()
        res = func(*args, **kwargs)
        finish = time.perf_counter_ns()
        run_time = (finish - start) / 10 ** 6
        # print(res)
        log_msg += f'Результат: {res}\t'
        log_msg += f'Время выполнения: {run_time} ms\n'
        with open('log_file.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        return res

    return wrapper


def cacher(func):
    """
    Кэширование значений функции. Вычисленные ранее значения хранятся в словаре cach
    :param func:
    :return:
    """
    cach = {}

    @wraps(func)
    def wrapper(*args):
        # ключ словаря - кортеж
        key = args
        # print(type(key))
        if key not in cach:
            cach[key] = func(*args)
        # print(cach)
        return cach[key]

    return wrapper
