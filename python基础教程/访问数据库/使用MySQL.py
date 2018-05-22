# coding=utf-8
import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='mytest')
cursor = conn.cursor()
cursor.execute('create table user ')
