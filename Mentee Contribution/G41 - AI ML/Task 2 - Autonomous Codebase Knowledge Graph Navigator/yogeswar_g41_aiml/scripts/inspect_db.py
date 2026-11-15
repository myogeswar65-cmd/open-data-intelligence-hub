import sqlite3

conn = sqlite3.connect('data/app_state.db')
cursor = conn.cursor()
tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print('Tables in app_state.db:')
for t in tables:
    print('  -', t[0])

print('\nCheck snapshots/commits:')
for t in tables:
    tname = t[0]
    if 'snap' in tname or 'commit' in tname or 'repo' in tname or 'job' in tname:
        count = cursor.execute(f"SELECT count(*) FROM {tname}").fetchone()[0]
        print(f"Table {tname}: {count} rows")
        sample = cursor.execute(f"SELECT * FROM {tname} LIMIT 3").fetchall()
        print("Sample:", sample)

conn.close()
