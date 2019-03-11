
准备工作
mysql -uroot -p123456
creat database chat;
use chat;
create table user(name varchar(32),passwd varchar(32));




使用方法：
运行服务器
1.python server.py
运行客户端
2.python client.py

说明：
file 为服务器缓存文件夹
needfile 为客户端下载缓存文件夹
注：上传和下载尽量用英文文件，避免不必要的错误，程序设计每次只能下载一个文件。

补充：
可以给登录和注册界面增加背景图片美化软件。

