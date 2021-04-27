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

#all maps in db
def db_selectallmaps():
    connection = db_connection()
    mycursor = connection.cursor()
    
    mycursor.execute("SELECT * FROM maps")
    query = mycursor.fetchall()

    return query

#get nomod maps
def db_get_maps_nm(quant):
    connection = db_connection()
    mycursor = connection.cursor()
    
    final=[]

    for i in range(0,quant):
        try:
            tmp = "SELECT link FROM maps WHERE type='NM"+str(i+1)+"' ORDER BY RAND() LIMIT 1"
            mycursor.execute(tmp)
            query = mycursor.fetchall()
            final.append(query[0])
        except:
            print("Not enough maps in the database...")

    return final

#get hidden maps
def db_get_maps_hd(quant):
    connection = db_connection()
    mycursor = connection.cursor()
    
    final=[]

    for i in range(0,quant):
        try:
            tmp = "SELECT link FROM maps WHERE type='HD"+str(i+1)+"' ORDER BY RAND() LIMIT 1"
            mycursor.execute(tmp)
            query = mycursor.fetchall()
            final.append(query[0])
        except:
            print("Not enough maps in the database...")

    return final

#get hardrock maps
def db_get_maps_hr(quant):
    connection = db_connection()
    mycursor = connection.cursor()
    
    final=[]

    for i in range(0,quant):
        if i != 0:
            try:
                tmp = "SELECT link FROM maps WHERE type='HR"+str(i+1)+"' ORDER BY RAND() LIMIT 1"
                mycursor.execute(tmp)
                query = mycursor.fetchall()
                final.append(query[0])
            except:
                print("Not enough maps in the database...")

    return final

#get doubletime maps
def db_get_maps_dt(quant):
    connection = db_connection()
    mycursor = connection.cursor()
    
    final=[]

    for i in range(0,quant):
        if i != 0:
            try:
                tmp = "SELECT link FROM maps WHERE type='DT"+str(i+1)+"' ORDER BY RAND() LIMIT 1"
                mycursor.execute(tmp)
                query = mycursor.fetchall()
                final.append(query[0])
            except:
                print("Not enough maps in the database...")

    return final

#get free mod maps
def db_get_maps_fm(quant):
    connection = db_connection()
    mycursor = connection.cursor()
    
    final=[]

    for i in range(0,quant):
        if i != 0:
            try:
                tmp = "SELECT link FROM maps WHERE type='FM"+str(i+1)+"' ORDER BY RAND() LIMIT 1"
                mycursor.execute(tmp)
                query = mycursor.fetchall()
                final.append(query[0])
            except:
                print("Not enough maps in the database...")

    return final

#get tiebraker maps
def db_get_maps_tb(quant):
    connection = db_connection()
    mycursor = connection.cursor()
    
    final=[]

    for i in range(0,quant):
        #if i != 0:
        try:
            tmp = "SELECT link FROM maps WHERE type='TB"+str(i+1)+"' ORDER BY RAND() LIMIT 1"
            mycursor.execute(tmp)
            query = mycursor.fetchall()
            final.append(query[0])
        except:
            print("Not enough maps in the database...")

    return final