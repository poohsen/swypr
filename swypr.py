#!/usr/bin/python

import socket
from servo import HS475HB 

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

servo = HS475HB()

print "Setting servo to neutral"
servo.neutral()

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        print buf
        if buf == 'swype_left':
            servo.neutral_right()
            servo.neutral()

        if buf == 'swype_right':
            
	        servo.neutral_left()
	        servo.neutral()
