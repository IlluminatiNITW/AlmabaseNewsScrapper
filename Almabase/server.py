from multiprocessing.connection import Listener
from array import array
import requests

address = ('localhost', 7001)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey='secret password')

conn = listener.accept()
print 'connection accepted from', listener.last_accepted
line=[]
while True:
	message=raw_input("Enter url: ")
	r=requests.get(message)
	if message == 'quit':
		break
	conn.send([message,r.content])

conn.close()
listener.close()