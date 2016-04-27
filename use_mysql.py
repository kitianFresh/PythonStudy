#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mysql.connector
conn = mysql.connector.connect(user='root', password='777', database='select_exercise')
cursor = conn.cursor()
cursor.execute('select * from student')
records = cursor.fetchall()
for row in records:
	print(row)
cursor.close()
conn.close()