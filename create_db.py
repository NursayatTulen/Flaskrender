import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE,
                    phone TEXT UNIQUE,
                    password TEXT NOT NULL,
                    role TEXT NOT NULL
                )''')  # <-- Қате осы жерде болуы мүмкін
    c.execute('''CREATE TABLE IF NOT EXISTS quizzes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT NOT NULL,
                    uploaded_by TEXT NOT NULL
                )''')  # <-- Бұл жерді де тексеріңіз
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("✅ Дерекқор жасалды!")
