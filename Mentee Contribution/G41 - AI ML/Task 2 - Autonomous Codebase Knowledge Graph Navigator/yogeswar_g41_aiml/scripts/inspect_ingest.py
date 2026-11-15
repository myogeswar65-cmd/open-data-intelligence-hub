import sqlite3

conn = sqlite3.connect('data/app_state.db')
cursor = conn.cursor()
print('Completed INGEST jobs:')
for row in cursor.execute("SELECT repo_id, commit_sha, log_output FROM jobs WHERE job_type='INGEST' AND status='COMPLETED'").fetchall():
    print(f"Repo: {row[0]} | Commit: {row[1]} | Result: {row[2]}")
conn.close()
