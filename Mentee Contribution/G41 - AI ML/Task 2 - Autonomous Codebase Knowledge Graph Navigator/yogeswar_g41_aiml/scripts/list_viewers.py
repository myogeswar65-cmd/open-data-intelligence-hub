import sqlite3

conn = sqlite3.connect('data/app_state.db')
cursor = conn.cursor()
users = cursor.execute("SELECT user_id, username, role, is_active FROM users WHERE role='viewer'").fetchall()
print("Viewer users:")
for u in users:
    print(" ", u)
conn.close()
