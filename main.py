# Это программа на Python
# Импортируем модуль sqlite3
import sqlite3

# Создаем соединение с базой данных
conn = sqlite3.connect('example.db')

# Создаем курсор для выполнения операций с базой данных
cur = conn.cursor()

# Создаем таблицу
cur.execute("CREATE TABLE IF NOT EXISTS sums (a INTEGER, b INTEGER, c INTEGER, a_cubed INTEGER, b_cubed INTEGER, c_cubed INTEGER, sum INTEGER, half_sum REAL, Begin INTEGER, End INTEGER)")

# Задаем диапазон значений для a, b и c
Begin = 1
End = 20001

# Вставляем данные в таблицу
for a in range(Begin,End):
    for b in range(Begin,End):
        for c in range(Begin,End):
            if((a**3 + b**3) / 2 == (c**3) / 2):
                a_cubed = a**3
                b_cubed = b**3
                c_cubed = c**3
                sum_ab = a_cubed + b_cubed
                half_sum_ab = sum_ab / 2
                # Выводим решение
                print (a, b, c)

                # Если да, то вставляем решение и пределы в таблицу sums
                cur.execute("INSERT INTO sums VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (a, b, c, a_cubed, b_cubed, c_cubed, sum_ab, half_sum_ab, Begin, End))

# Сохраняем изменения
conn.commit()

# Закрываем соединение с базой данных
conn.close()