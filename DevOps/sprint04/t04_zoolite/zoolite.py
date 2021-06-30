import sys
import json
import sqlite3


def connect(data):
    try:
        conn = sqlite3.connect(data['database'])
        return conn
    except sqlite3.Error as e:
        print(e)
        return


def create_table_cursor(data, conn):
    crt_tbl = f"CREATE TABLE IF NOT EXISTS {data['table']} (species TEXT, name TEXT, age INTEGER);"
    try:
        c = conn.cursor()
        c.execute(crt_tbl)
        return c
    except sqlite3.Error as e:
        print(e)
        return


def mark_unique(curs, conn, data):
    try:
        curs.execute(
            f"CREATE UNIQUE INDEX USER ON {data['table']} (species, name)")
        conn.commit()
    except sqlite3.Error as e:
        print(e)
        return


def born(curs, conn, data, news):
    try:
        query = f'INSERT INTO {data["table"]} (species, name, age) VALUES ("{news["species"]}", "{news["name"]}", 0)'
        curs.execute(query)
        if curs is not None:
            print(
                f"Inserted {news['species']} {news['name']} in table {data['table']} of {data['database']}.")
        conn.commit()
    except Exception as e:
        print(f"Failed to process event: {news}. Error: {e}")


def died(curs, conn, data, news):
    curs.execute(
        f'DELETE FROM {data["table"]}  WHERE species = "{news["species"]}" AND name = "{news["name"]}"')
    conn.commit()
    print(
        f'Deleted {news["species"]} {news["name"]} in table {data["table"]} of {data["database"]}.')


def birthday(curs, conn, data, news):
    curs.execute(
        f'SELECT age FROM animals WHERE species = "{news["species"]}" and name = "{news["name"]}"')
    age = curs.fetchone()
    if age:
        curs.execute(
            f'UPDATE {data["table"]} SET age = {age[0] + 1} WHERE species = "{news["species"]}" and name = "{news["name"]}"')
        conn.commit()
        print(
            f'Updated {news["species"]} {news["name"]} in table {data["table"]} of {data["database"]}.')


def update_zoo(data):
    conn = connect(data)
    c = create_table_cursor(data, conn)
    mark_unique(c, conn, data)
    # print len of rows in db table
    c.execute(f"SELECT * FROM {data['table']}")
    print(f"*** BEFORE: {len(c.fetchall())} {data['table']} int the zoo")
    for news in data['news']:
        if news["event"] == "born":
            born(c, conn, data, news)
        elif news['event'] == "died":
            died(c, conn, data, news)
        elif news['event'] == "birthday":
            birthday(c, conn, data, news)
    c.execute(f"SELECT * FROM {data['table']}")
    print(f"*** AFTER: {len(c.fetchall())} {data['table']} in the zoo.")