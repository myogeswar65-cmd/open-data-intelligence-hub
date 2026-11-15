import os
from neo4j import GraphDatabase

with open('/run/secrets/neo4j_admin_password') as f:
    pw = f.read().strip()

driver = GraphDatabase.driver('bolt://neo4j:7687', auth=('neo4j', pw))
with driver.session() as s:
    q = "MATCH (n:Entity {repo_id: '12fac9bd-0ebb-4844-a239-e518e812b6bb'}) RETURN n.name as name, n.file_path as file, n.line_start as lstart, labels(n) as lbls"
    res = s.run(q)
    print("Entities in 12fac9bd:")
    for r in res:
        print(" ", r["name"], r["file"], r["lstart"], r["lbls"])
driver.close()
