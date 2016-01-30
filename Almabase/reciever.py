from multiprocessing.connection import Client
from array import array
from Queue import Queue
import threading
import time

workQueue = Queue()
address = ('localhost', 7001)

class myThread(threading.Thread):
    def __init__(self, threadID, name,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def process_data2(self,q):
		conn = Client(address, authkey='secret password')
		message=""
		while True:
			message=conn.recv() 
			print "received", message 
			q.put(message)

    def run(self):
        print "Starting " + self.name
        self.process_data2(self.q)
        print "Exiting " + self.name

class myThread2(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def process_data(self,threadName, q):
		while True:
		    if not q.empty():
		        data = q.get()
		        q.task_done()
		        print "%s processing %s" % (threadName, data)
		    time.sleep(1)

    def run(self):
        print "Starting " + self.name
        self.process_data(self.name, self.q)
        print "Exiting " + self.name



thread = myThread(1, "Reciever",workQueue)
thread.start()
thread = myThread2(2, "Getter", workQueue)
thread.start()