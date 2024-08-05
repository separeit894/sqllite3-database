import sqlite3

db = sqlite3.connect("separeit.db")

c = db.cursor()

# c.execute("""CREATE TABLE articles (
#     title text,
#     full_text text,
#     views integer,
#     avtor text
# )""")

# c.execute("INSERT INTO articles VALUES ('stopgame and youtube', 'стопгейм заблокируют сегодня', 100, 'Admib')")
# c.execute("INSERT INTO articles VALUES ('youty block', 'qer', 100, 'sdfa'")
# c.execute("""
#     INSERT INTO articles VALUES (
#     'youtube block',
#     'youtube really block',
#     100,
#     'separeit'
#     )""")

# c.execute("SELECT rowid, title FROM articles")
# c.execute("DELETE FROM articles WHERE rowid > 1")
c.execute("SELECT * FROM articles")
print(c.fetchall())
db.commit()

db.close()