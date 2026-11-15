import os
from neo4j import GraphDatabase

with open('/run/secrets/neo4j_admin_password') as f:
    pw = f.read().strip()

driver = GraphDatabase.driver('bolt://neo4j:7687', auth=('neo4j', pw))
with driver.session() as s:
    q = "MATCH (u:UnresolvedCall {repo_id: '12fac9bd-0ebb-4844-a239-e518e812b6bb'}) RETURN u.call_expression as expr, u.callee_name as callee, u.file_path as file, u.line_number as line"
    res = s.run(q)
    print("Unresolved calls for 12fac9bd:")
    for r in res:
        print(" ", dict(r))
driver.close()
