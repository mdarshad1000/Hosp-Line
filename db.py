import psycopg2
import json
import os

with open('auth.json') as r:
    config = json.load(r)

DATABASE_URL = os.environ.get('DATABASE_URL')


class Actions:
    def __init__(self, config):
        # From json File
        self.host = config['HOST']
        self.dbname = config['DB']
        self.user = config['USER']
        self.password = config['PASS']
        self.port = 5432
        self.conn = None

    def connect(self):
        if self.conn is None:
            # self.conn = psycopg2.connect(
            #     host=self.host,
            #     dbname=self.dbname,
            #     user=self.user,
            #     password=self.password,
            #     port=self.port
            # )
            self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
            print('Database connected successfully!')

    # def create_table(self):
    #     self.connect()
    #     cur = self.conn.cursor()
    #     create_script = ''''CREATE TABLE IF NOT EXISTS patient(
    #                 spot SERIAL PRIMARY KEY,
    #                 name VARCHAR(30) NOT NULL,
    #                 birthday VARCHAR(30) NOT NULL,
    #                 gender VARCHAR(15) NOT NULL,
    #                 spot INT)
    #                 '''
    #     cur.execute(create_script)
    #     self.conn.commit()
    #     cur.close()

    def new_entry(self, name, birthday, gender, spot):
        self.connect()
        cur = self.conn.cursor()
        cur.execute("INSERT INTO patient(name,birthday,gender,spot)"
                    f"VALUES ('{name}', '{birthday}', '{gender}', {spot});")
        self.conn.commit()
        cur.close()

        print("Patient joined the queue")

    def new_spot(self):
        self.connect()
        cur = self.conn.cursor()
        cur.execute("SELECT MAX(spot)"
                    f"FROM patient")
        maximum = cur.fetchone()
        if maximum[0] is None:
            maximum = 1
        else:
            maximum = maximum[0] + 1
        cur.close()
        print("New patient joined the queue", maximum)
        return maximum

    def get_spot(self, name):
        self.connect()
        cur = self.conn.cursor()
        cur.execute("SELECT spot FROM patient "
                    f"WHERE name = '{name}';")
        spot = cur.fetchone()
        cur.close()
        return spot

    def total_infront(self, name):
        self.connect()
        cur = self.conn.cursor()
        cur.execute("SELECT spot FROM patient "
                    f" WHERE name = '{name}';")
        current_spot = cur.fetchone()
        if current_spot is not None:
            cur.execute("SELECT * FROM patient "
                        f"WHERE spot < {current_spot[0]};")
            total_list = list(cur.fetchall())
            total = len(total_list)
            cur.close()
            print(total, "total")
            return total
        return 0

    def leave(self, name, spot):
        self.connect()
        cur = self.conn.cursor()
        cur.execute("DELETE FROM patient "
                    f"WHERE name='{name}';")
        self.conn.commit()
        cur.close()
        print(name, "left")

#  ----EXPLANATION----
# def get_spot()
# That command basically selects the maximum element from the "spot" row and stores it into 'max' row.
# If the "spot" list is empty then the first element of the "spot" row will become 1
# If the "spot" list is not empty then there will be only one element, and in that case max will get assigned the next value i.e max[0] + 1


# total_infront() fetches the tuple of 'spot' using fetchone()
# Then if it is not None then it selects all values which are less than the first value in the tuple i.e the spot.
# then it converts it into a list and stores the no.of elements in the list
