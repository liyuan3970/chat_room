import threading
import os
def load_and_regist():
	os.system('python server_r@l.py')

def ftp_server():
	os.system('python server_ftp.py')

def send_server():
	os.system('python server_send.py')
t1 = threading.Thread(target=load_and_regist)
t2 = threading.Thread(target=ftp_server)
t3 = threading.Thread(target=send_server)
t1.start()
t2.start()
t3.start()