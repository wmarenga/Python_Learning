"""
Docs: https://cx-oracle.readthedocs.io/en/latest/user_guide/introduction.html

python -m pip install cx_Oracle --upgrade
"""
import cx_Oracle

# Establish the database connection
user = "my_user"
password = "my_password"
dsn = "my_data_source_name"

conn = cx_Oracle.connect(user, password, dsn)

# Obtain a cursor
cur = conn.cursor()  # creates a cursor object

# Execute the query

# Simple:
# query = "SELECT * FROM TABLE_NAME"
# r = cur.execute(query)

# Multiple queries
query = "'select ISAMM_CRD.VW_FCT_EUROSTAT_INDICATOR from isammdctst2 where INDICATOR_CODE = 'C14' "
r = cur.executemany(query)

# if you want to load to memory just a random row from the table
# row = r.fetchone()
# print(row)

# if you want to load to memory the complete query result
rows = r.fetchall()
print(rows)

cur.close()  # close the cursor
conn.close()  # close the connection
