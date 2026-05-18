import sqlite3

def init_db():
    print("=== GAME DATABASE SYSTEM ===")
    print("Booting SQLite core...")
    
    # Připojení k databázi (vytvoří soubor games.db, pokud neexistuje)
    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()

    # Zapnutí podpory cizích klíčů (v SQLite defaultně vypnuto)
    cursor.execute("PRAGMA foreign_keys = ON;")

    # --- PHASE 1: DB BOOTSTRAP ---
    
    # Vytvoření tabulky kategorií
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Vytvoření tabulky her s cizím klíčem
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            release_year INTEGER,
            rating REAL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )
    ''')

    # --- PHASE 2: SEED DATA ---
    
    # Vložení kategorií (pouze pokud je tabulka prázdná)
    cursor.execute("SELECT COUNT(*) FROM categories")
    if cursor.fetchone()[0] == 0:
        categories = [
            ('RPG',),
            ('Action',),
            ('Strategy',),
            ('Simulation',),
            ('Sport',)
        ]
        cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)

        # Vložení her
        games = [
            ('The Witcher 3', 2015, 9.8, 1),
            ('Elden Ring', 2022, 9.6, 1),
            ('Cyberpunk 2077', 2020, 8.5, 1),
            ('Doom Eternal', 2020, 9.0, 2),
            ('GTA V', 2013, 9.5, 2),
            ('Starcraft II', 2010, 9.2, 3),
            ('Civilization VI', 2016, 8.8, 3),
            ('Microsoft Flight Simulator', 2020, 9.1, 4),
            ('The Sims 4', 2014, 7.5, 4),
            ('FIFA 23', 2022, 7.2, 5)
        ]
        # Použití parametrizovaného dotazu (Security mode ON)
        cursor.executemany(
            "INSERT INTO games (title, release_year, rating, category_id) VALUES (?, ?, ?, ?)", 
            games
        )
        
    conn.commit()
    print("Ready.\n")
    return conn

def show_games(conn):
    # --- PHASE 3: QUERY MODE ---
    cursor = conn.cursor()
    
    query = """
        SELECT g.title, g.release_year, g.rating, c.name
        FROM games g
        JOIN categories c ON g.category_id = c.id
        ORDER BY g.rating DESC
    """
    
    cursor.execute(query)
    results = cursor.fetchall()

    print(f"{'NÁZEV HRY':<30} | {'ROK':<5} | {'HODNOCENÍ':<5} | {'KATEGORIE'}")
    print("-" * 65)
    
    for row in results:
        title, year, rating, cat_name = row
        print(f"{title:<30} | {year:<5} | {rating:<9} | {cat_name}")

if __name__ == "__main__":
    connection = init_db()
    show_games(connection)
    connection.close()