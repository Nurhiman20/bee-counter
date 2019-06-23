import serial
import time
import MySQLdb as mdb

con = mdb.connect('localhost','pi','linggarestu123','mydb');

with con:
	cursor = con.cursor()
	cursor.execute("INSERT INTO tes_db (id, warna, waktu) VALUES (NULL,'kuning',now());")
	con.commit()
	cursor.close()