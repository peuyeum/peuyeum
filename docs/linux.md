# Peuyeum Framework
Geospatial Web Application Framework

## Kebutuhan

- Virtualenv
- Uwsgi
- Pymongo
- Pycrypto
- Redis
- MySql

Disini dijelaskan secara singkat kegunaan dari setiap kebutuhan yang diperlukan.

- Virtualenv

Virtualenv adalah sebuah software (berbasis python) yang mana bertujuan untuk membuat sebuah lingkungan python yang terisolasi dari lingkunagan python global, jadi program python apapun yang anda jalankan di dalamnya maka tidak akan terpengaruh oleh lingkungan python global, atau program yang sudah terinstall di lingkungan Python global.

- Uwsgi

Uwsgi adalah sebuah aplikasi yang digunakan untuk menggambarkan beberapa prosedur installation, menggunakan pip, pengelola python.

- Pymongo

Pymongo adalah driver yang digunakan python untuk melakukan koneksi ke mongodb.

- Pycrypto

Pycrypto adalah Sebuah Bahasa pemrograman yang digunakan untuk rancang bangun aplikasi yang dapat berbetuk File Secure.

- Redis

Redis adalah Open Source yang digunakan untuk menyimpan struktur data pada memori, biasanya digunakan sebgaia database cache dan message broker.

- MySQL

MySQL adalah database yang digunakan untuk menyimpan data pada pembuatan program.

## Instalasi

Pada tahap instalasi, kita tentunya harus memenuhi kebutuhan-kebutuhan yang mendukung jalannya program aplikasi yang kita buat. Selain itu, kita juga harus menyesuaikan setiap kebutuhan yang cocok untuk spesifikasi sistem yang kita gunakan untuk menghindari banyaknya ketidakcocokan pada saat menjalankan aplikasi tersebut. Tahap-tahap instalasi yang dilakukan adalah sebagai berikut:

~~~
# yum groupinstall "Development Tools"
# yum install python
# yum install python-pip python-devel
# pip install uwsgi
# pip install pymongo
# pip install pycrypto
# pip install MySQL-python
~~~

Install MySQL pada runlevel mana yang akan dimulai:

~~~
# yum install mysql-server
~~~

Kemudian untuk memulai server MySQL:

~~~
# service mysqld start
~~~

Jalankan skrip mysql_secure_installation untuk mengatasi beberapa masalah keamanan di instalasi MySQL default.

~~~
# mysql_secure_installation
~~~

Untuk login ke MySQL sebagai Root User:

~~~
# mysql -u root -p
~~~

Saat diminta, masukkan kata sandi root yang Anda tetapkan saat skrip mysql_secure_installation dijalankan.<br>
Anda kemudian akan disajikan dengan layar monitor MySQL:

~~~
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1
Server version: 5.1.73 Source distribution

Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its affiliates. 
Other names may be trademarks of their respective owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database kelasc;
mysql> exit
~~~

Import database ke database tujuan di MySQL.

~~~
# cd tugas/docs
# mysql -u root -p ****** kelasc < mysql.sql
# cd ..
~~~

Kemudian, edit file peuyeum.ini. <br>
Untuk mengedit file pada baris perintah, Anda bisa menggunakan editor seperti vi.

~~~
# vi peuyeum.ini
~~~
~~~
[uwsgi]
module = peuyeum:application
check-static = ./public

master = true
processes = 5
http = 0.0.0.0:8080
#uid = peuyeum
#socket = ../run/peuyeum.sock
#chown-socket = peuyeum:peuyeum
#chmod-socket = 660
#vacuum = true

die-on-term = true
~~~

Setelah itu, edit file config.py:
~~~
# cd lib
# vi config.py
~~~
~~~
config.py 
set paramater of your server
"""
### Menus
keyuri = "URI"
tokenuri = "TKN"

### Database
mongohost = "localhost"
mongoport = 27017
mysqlhost = "localhost"
mysqldb = "kelasc"
mysqluser = "root"
mysqlpassword = "your password"

### Security module
key = "your key 16 char"
iv = "your iv 16 char"
tokenurl = "https://www.googleapis.com/oauth2/v3/tokeninfo?id_token="
iss = "accounts.google.com"
aud = "WEB_CLIENT_ID"
domainacl = "poltekpos.ac.id"
urltimeout = 3600

### mapserver
WMTS="http://peta.peuyeum.com/wmts/sampeu/ragi/{z}/{x}/{y}.png"
~~~

Terakhir , jalankan uwsgi di centos 6:
~~~
# cd ..
# uwsgi peuyeum.ini
~~~