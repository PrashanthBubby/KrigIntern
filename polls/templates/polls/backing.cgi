import os
import cgi, cgitb
import MySQLdb
db = MySQLdb.connect("localhost","root","bubby@5524","sakila" )
cursor=db.cursor()
form=cgi.FieldStorage()
L_ID=form.getvalue('username')
P_WORD=form.getvalue('password')

cursor.execute('INSERT INTO REGISTER VALUES("%s","%s")' % \
(L_ID,P_WORD))
db.commit()
db.close()
print("SIGNEDUP SUCCESSFULLY")
