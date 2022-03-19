import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='postgres',
    user='postgres',
    password='Makeawebapp@7',
    port=5432
)
cur = conn.cursor()
create_script = '''CREATE TABLE IF NOT EXISTS patient(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(30) NOT NULL,
                    birthday VARCHAR(30) NOT NULL,
                    gender VARCHAR(15) NOT NULL,
                    spot INT)
                    '''
# cur.execute("SELECT spot FROM patient WHERE name='arshad';")
# current_spot = cur.fetchone()
#
# print(current_spot)
cur.execute(create_script)

conn.commit()
print('Database modified!')
