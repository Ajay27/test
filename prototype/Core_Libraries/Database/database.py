
import pymysql as mariadb
import VBO_Objects.properties

def db_connect():
    # Open database connection
    db = mariadb.connect(VBO_Objects.properties.dbhost, VBO_Objects.properties.dbuser,
                         VBO_Objects.properties.dbpassword, VBO_Objects.properties.db)
    return db

def execute(sql):
    db = db_connect()
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data

def deletesql(sql):
    db = db_connect()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()