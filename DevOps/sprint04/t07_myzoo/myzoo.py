import yaml
import mysql.connector

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


def update_zoo(data):
    config = make_dict_config()
    conn = do_connect(config)
    cursor = conn.cursor()
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {data["database"]}')
    cursor.execute(f'USE {data["database"]}')
    print(f"Using database '{data['database']}'")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS `{data['table']}` (`species` VARCHAR(100) PRIMARY KEY NOT NULL), (`name` VARCHAR(100) PRIMARY KEY NOT NULL), (`age` INTEGER CHECK(`age` >= 0 AND `age` <= 100) DEFAULT 0)")

