from tkinter import *
import tkinter as tk
from socket import *
import json
import time 
import os
import sys
def download():
    sockfdow = socket()

    #发起连接请求
    server_addr = ('127.0.0.1',50009)
    sockfdow.connect(server_addr)

    #发送请求服务器文件列表
    request='request '+'just_test'
    sockfdow.send(request.encode())
    fl = sockfdow.recv(1024)
    filelist=json.loads(fl.decode())
    sockfdow.close()
    print(filelist)



    root = tk.Toplevel() 
    theLB = Listbox(root,height=11)#height=11设置listbox组件的高度，默认是10行。
    theLB.pack()






    #接收到文件列表后生成listbox
    for item in filelist:
        theLB.insert(END,item)  #END表示每插入一个都是在最后一个位置
    
    #定义下载按钮，向服务器发送下载请求
    def select_file(event):
        sockevent=socket()
        #server_addr = ('127.0.0.1',50009)
        sockevent.connect(server_addr)


        print("entry the downlaod file func")
        a=theLB.get(theLB.curselection())  #a是选中的文件名称
        print(a)
        message='get '+a
        sockevent.send(message.encode())

        filepath = 'needfile/'
        with open(filepath+a, 'wb') as f:
            while True:
                data = sockevent.recv(1024)
                if not data:
                    print("save finshed")
                    break
                f.write(data)
                time.sleep(0.1)
        sockevent.close()
        root.destroy()


    theLB.bind('<ButtonRelease-1>',select_file)