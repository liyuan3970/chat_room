import socket
import threading
from threading import Thread 
import time
import os
import os.path
import json
#from socket import *
from select import *

#flna=os.listdir('file')
#print(flna)


################################################################
def pictureServer():
    IP = '127.0.0.1'
    PORT = 50009    # 再开一个端口运行此图片缓存服务器
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    s.bind( (IP, PORT) )
    s.listen(5)
    

    def tcp_connect2(conn, addr):    
        data = conn.recv(1024)
        data = data.decode()
        print('Received message from {0}: {1}'.format(addr, data))
        order = data.split()[0]  # 获取动作
        print(order)
        recv_func2(order, data)        
        conn.close()
        print('---')
    folder = 'file/'    # 图片的保存文件夹
    # 发送文件函数
    def sendFile2(message):
        #请求文件列表
        needfile=message.split()[1]
        folder = 'file/'
        filepath=folder + needfile
        print("begin to send file")
        with open(filepath, 'rb') as f:
            while True:
                a = f.read(1024)
                if not a:
                    break
                conn.send(a)
        time.sleep(0.1)

        #conn.close()


    # 保存上传的文件到当前工作目录
    def recvFile2(message):
        print(message)
        name = message.split()[1] #获取文件名
        fileName = folder + name   # 将文件夹和图片名连接起来
        print('开始保存!')
        with open(fileName, 'wb') as f:
            while True:
                data = conn.recv(1024)
                if data == 'EOF'.encode():
                    print('保存成功!')
                    break
                f.write(data)
    #flash the server file list
    def flashFile2(message):
        flna=os.listdir('file')
        filename=json.dumps(flna)
        conn.send(filename.encode())
        print("filename send ok")
        #conn.close()
    # 判断输入的命令并执行对应的函数
    def recv_func2(order, message):
        if order == 'get':
            return sendFile2(message)
        elif order == 'put':
            return recvFile2(message)
        elif order == 'request':
            return flashFile2(message)


    #创建epoll对象
    p = epoll() 
    #建立查找字典
    fdmap = {s.fileno():s}
    #注册关注IO
    p.register(s,EPOLLIN|EPOLLERR)
    print('开始运行...')
    while True:
        events = p.poll()  #监控IO
        for fd,event in events:
            if fd == s.fileno():
                conn,addr = fdmap[fd].accept()
                p.register(conn,EPOLLIN|EPOLLHUP|EPOLLET)
                fdmap[conn.fileno()] = conn
                #tcp_connect2(conn,addr)
            elif event & EPOLLIN:
                tcp_connect2(conn,addr)
    s.close()    


serv3 = threading.Thread(target=pictureServer)
serv3.start()

