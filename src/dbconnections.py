#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
import json
import mysql.connector

project_path = os.path.dirname(os.path.dirname(__file__))

def db_connection():
    dbdata = load_db_config()
    
    mydb = mysql.connector.connect(
    database=dbdata[0],
    host=dbdata[1],
    user=dbdata[2],
    password=dbdata[3]
    )

    return mydb

def load_db_config():
    global DB, HOST, USER, PSWD
    database_config = project_path+"/.config/database.json"
    f = open(database_config)
    data = json.load(f)
    
    connection=[]
    for i in data:
        connection.append(i['database'])
        connection.append(i['host'])
        connection.append(i['user'])
        connection.append(i['password'])
    
    return connection

def db_selectallmaps():
    connection = db_connection()
    mycursor = connection.cursor()
    
    mycursor.execute("SELECT * FROM maps")
    query = mycursor.fetchall()

    return query