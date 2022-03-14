import sqlite3

import random

conn = sqlite3.connect('practica1.db')
# создаем базу данных
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, t1col_1 TEXT)''')
# создаем таблицу tab_1 с 1-м целочисленным полем t1col_1
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, t2col_1 INTEGER)''')
# создаем таблицу tab_2 с 1-мя строковым полем t2col_1

list1 = ['привет', 123, 'какдела', 4, 'старт', 23, 'стоп']
nechetnoe = 'не четное'
for i in list1:
    if type(i) is str:
        len1 = len(i)
        cursor.execute('''INSERT INTO tab_1(t1col_1) VALUES (?)''', (i,))
        cursor.execute('''INSERT INTO tab_2(t2col_1) VALUES (?)''', (len1,))
    else:
        if (i % 2) == 0:
            cursor.execute('''INSERT INTO tab_2(t2col_1) VALUES (?)''', (i,))
        else:
            cursor.execute('''INSERT INTO tab_1(t1col_1) VALUES (?)''', (nechetnoe,))
conn.commit()

# # Выведем таблицу1 на экран
cursor.execute('''SELECT t1col_1 FROM tab_1''')
k = cursor.fetchall()
print(k)
cursor.execute('''SELECT t2col_1 FROM tab_2''')
n = cursor.fetchall()
print(n)

if len(k) > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
else:
    cursor.execute('''UPDATE tab_1 SET t1col_1='hello' WHERE id=1''')
conn.commit()

cursor.execute('''SELECT t1col_1 FROM tab_1''')
k = cursor.fetchall()
print(k)
