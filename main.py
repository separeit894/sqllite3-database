import sqlite3

# Создаем базу данных
db = sqlite3.connect("data_base.db")

# Создаем курсор, чтобы написать команды для создания, ввода и т. п.
c = db.cursor()

# Вводим execute, чтобы создать таблицу articles с её значениями
c.execute("""CREATE TABLE articles (
    title text,
    full_text text,
    views integer,
    avtor text
)""")

# Вводим значения в таблицу
c.execute("INSERT INTO articles VALUES ('Youtube', 'Youtube замедляют на 70%', 100, 'News')")

# c.execute("SELECT rowid, title FROM articles")
# c.execute("DELETE FROM articles WHERE rowid > 1")

# Здесь мы выводим информацию из таблицы
c.execute("SELECT * FROM articles")
# Выводим информацию через print
print(c.fetchall())
# Обновляем базу данных
db.commit()

# Закрываем базу данных
db.close()

