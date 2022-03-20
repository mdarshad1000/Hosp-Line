import psycopg2
from db import Actions, config

execute = Actions(config)

with open('auth.json') as r:
    config = json.load(r)
    
conn = psycopg2.connect(
    host=config['HOST'],
    dbname=config['DB'],
    user=config['USER'],
    password=config['PASS'],
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
