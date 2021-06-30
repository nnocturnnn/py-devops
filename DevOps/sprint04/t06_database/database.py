import yaml
import mysql.connector
import sys

def connector(config):
    try:
        c = mysql.connector.connect(host=config['settings']['host'],
                                    user=config['settings']['user'],
                                    password=config['settings']['password'])
        try:
            print(f"Connected to MySQL server (version {c.get_server_info()}), database {config['settings']['database']}.")
        except KeyError:
            print(f"Connected to MySQL server (version {c.get_server_info()}), database None.")
        return c
    except mysql.connector.Error as err:
        print(err)

def make_dict_config():
    with open('cfg.yaml', 'r') as f:
        return yaml.full_load(f)

def do_connect(config):
    conn = connector(config)
    return conn

def close_conn(conn):
    conn.close()
    print("MySQL connection is closed.")

def databases(cursor):
    try:
        database = ("show databases")
        cursor.execute(database)
        print('Database list:')
        for (databases) in cursor:
            print('\t' * 2 + f'- {databases[0]}')
    except mysql.connector.Error as e:
        print(e)

def print_tables(cursor):
    tables_list = [c for c in cursor]
    if len(tables_list) > 0:
        print('Table list:')
        for tables in tables_list:
            print('\t' * 2 + f'- {tables[0]}')
    else:
        print('No tables.')

def tables(cursor, config):
    try:
        try:
            cursor.execute(f"USE {config['settings']['database']}")
            table = ("SHOW TABLES")
            cursor.execute(table)
            print_tables(cursor)
        except mysql.connector.Error as e:
            print(e)
    except KeyError:
        print('Error: not connected to a database.')

def create_db(cursor, db_name):
    try:
        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f"Database '{db_name}' is created.")
    except mysql.connector.Error as e:
        print(f'MySQL connection error {e}')

def drop_db(cursor, db_name):
    try:
        cursor.execute(f"DROP DATABASE {db_name}")
        print(f"Database '{db_name}' is dropped.")
    except mysql.connector.Error as e:
        print(f'MySQL connection error {e}')

def validation(argv):
    commands = ['databases', 'tables', 'create', 'drop']

    if len(argv) >= 2 and argv[1] in commands:
        return True
    else:
        return False

if __name__ == '__main__':
    if validation(sys.argv):
        config = make_dict_config()
        conn = do_connect(config)
        cursor = conn.cursor()
        if len(sys.argv) == 2:
            if sys.argv[1] == 'databases':
                databases(cursor)
            elif sys.argv[1] == 'tables':
                tables(cursor, config)
        elif len(sys.argv) == 3:
            if sys.argv[1] == 'create':
                create_db(cursor, sys.argv[2])
            elif sys.argv[1] == 'drop':
                drop_db(cursor, sys.argv[2])
        close_conn(conn)
    else:
        print('Error: command-line arguments are invalid.')
