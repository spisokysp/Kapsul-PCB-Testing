import sqlite3
import socket

database="kapsul.db"
table= "validation"

TCP_IP="192.168.137.1"
TCP_PORT = 5005
BUFFER_SIZE = 20

conn = sqlite3.connect(database)
c = conn.cursor()

sql = 'create table if not exists ' + table + ' (mac text, status integer )'
c.execute(sql)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn_net, addr = s.accept()
print('Connection address:', addr)
try:
    while 1:
        data = conn_net.recv(BUFFER_SIZE)
        temp = data.decode('utf-8').split('|')
        for x in temp:
            if len(x)==12:
                mac=x
            else:
                try:
                    int(x)
                    sql = "INSERT INTO "+table+" VALUES ('"+mac+"',"+x+")"
                    print("Received Mac:",mac,",State:",x)
                    c.execute(sql)
                except ValueError:
                    continue
finally:
    conn_net.close()
    conn.commit()
    c.close()
    conn.close