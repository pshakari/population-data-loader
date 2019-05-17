import psycopg2
from os import environ


class DatabaseLoader:
    # main function
    def __init__(self):
        self.server = environ.get("SERVER")
        self.user = environ.get("USER")
        self.password = environ.get("PASSWORD")
        self.dbname = environ.get("DBNAME")

    # takes the csv and inserts it into the db
    def setup_db(self):
        conn = psycopg2.connect(host=self.server,
                                port=5432,
                                dbname=self.dbname,
                                user=self.user,
                                password=self.password)

        cur = conn.cursor()

        # does table exist
        tb_exists = "select exists(" \
                    "select relname from pg_class where relname='"\
                    + "population" + "')"
        cur.execute(tb_exists)
        if cur.fetchone()[0] is False:
            # make table
            cur.execute(
                'create table population('
                'country VARCHAR, '
		'continent VARCHAR,'
		'population INT);')
            conn.commit()
        # copy csv
        f = open(r'population.csv', 'r')
        cur.copy_from(f, "population", sep=',')
        conn.commit()
        f.close()

if __name__ == '__main__':
    dbl = DatabaseLoader()
    dbl.setup_db()
