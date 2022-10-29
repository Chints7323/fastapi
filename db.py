# db.py
import os
import pymysql
from flask import jsonify



db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user,
                                   password=db_password,
                                   unix_socket=unix_socket,
                                   db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        return e
    return conn


def get():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM footsteps_db.path;')
        path = cursor.fetchall()
        if result > 0:
            got_path = jsonify(path)
        else:
            got_path = 'No path in DB'
        return got_path


def create(path):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO footsteps_db.path (path_id, story_id, latitude, longitude, timestamp) VALUES(%s, %s, %s, %s, %s)',
                       (path["path_id"], path["story_id"], path["latitude"], path["longitude"], path["timestamp"]))
    conn.commit()
    conn.close()