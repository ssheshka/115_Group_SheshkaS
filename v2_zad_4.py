# зад.4 Написать функцию и сделать так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
# Написать функцию и сделать так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

def timer(sec):
    day = sec // (24 * 60 * 60)
    sec = sec - day * (24 * 60 * 60)
    hours = sec // (60 * 60)
    sec = sec - hours * (60 * 60)
    min = sec // 60
    sec = sec - min * 60
    print(f'{day}:{hours}:{min}:{sec}')

timer(int(input('Введите число секунд = ')))
