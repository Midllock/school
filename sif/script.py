import sqlite3

# připojení k databázi
conn = sqlite3.connect("fotbal.db")

# kurzor
cursor = conn.cursor()

# vytvoření tabulky klubů
cursor.execute("""
CREATE TABLE IF NOT EXISTS klub (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nazev TEXT NOT NULL,
    mesto TEXT NOT NULL
)
""")

# vytvoření tabulky hráčů
cursor.execute("""
CREATE TABLE IF NOT EXISTS hrac (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    jmeno TEXT NOT NULL,
    prijmeni TEXT NOT NULL,
    pozice TEXT,
    klub_id INTEGER,
    FOREIGN KEY (klub_id) REFERENCES klub(id)
)
""")

# vložení klubů
cursor.execute("""
INSERT INTO klub (nazev, mesto)
VALUES
('Sparta Praha', 'Praha'),
('Slavia Praha', 'Praha')
""")

# vložení hráčů
cursor.execute("""
INSERT INTO hrac (jmeno, prijmeni, pozice, klub_id)
VALUES
('Lukáš', 'Haraslín', 'Útočník', 1),
('Jan', 'Kuchta', 'Útočník', 1),
('Veljko', 'Birmančević', 'Záložník', 1),

('Tomáš', 'Chorý', 'Útočník', 2),
('Ivan', 'Schranz', 'Útočník', 2),
('David', 'Douděra', 'Obránce', 2)
""")

# uložení změn
conn.commit()

print("Databáze byla vytvořena.")

# výpis klubů
print("\nKLUBY:")
cursor.execute("SELECT * FROM klub")

for klub in cursor.fetchall():
    print(klub)

# výpis hráčů
print("\nHRÁČI:")
cursor.execute("SELECT * FROM hrac")

for hrac in cursor.fetchall():
    print(hrac)

# spojení tabulek pomocí JOIN
print("\nHRÁČI A JEJICH KLUBY:")

cursor.execute("""
SELECT
    hrac.jmeno,
    hrac.prijmeni,
    hrac.pozice,
    klub.nazev
FROM hrac
JOIN klub
ON hrac.klub_id = klub.id
""")

for row in cursor.fetchall():
    print(row)

# uzavření databáze
conn.close()