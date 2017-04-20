# Peuyeum Framework
Geospatial Web Application Framework

1. **Kebutuhan :**

- Virtualenv
- Uwsgi
- Pymongo
- Pycrypto
- Redis
- MySql

Disini saya akan menjelaskan secara singkat kegunaan dari setiap kebutuhan yang diperlukan.

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

1. **Instalation :**

Pada tahap instalasi, kita tentunya harus memenuhi kebutuhan-kebutuhan yang mendukung jalannya program aplikasi yang kita buat.Selain itu, kita juga harus menyesuaikan setiap kebutuhan yang cocok untuk  spesifikasi sistem yang kita gunakan untuk menghindari banyaknya ketidakcocokan pada saat menjalankan aplikasi tersebut. Tahap-tahap instalasi yang dilakukan adalah sebagai berikut:

- **Centos 6**

| yum --enablerepo=extras install centos-release-SCL
yum install python27# cd /etc/yum.repos.d/ 
wget https://copr.fedorainfracloud.org/coprs/pypa/pypa/repo/epel-6/pypa-pypa-epel-6.repo
yum clean all
yum install python-backports
rpm -ivh ftp://rpmfind.net/linux/centos/6.8/os/x86\_64/Packages/python-backports-ssl\_match\_hostname-3.4.0.2-2.el6.noarch.rpm
yum install python-pip# pip install virtualenv# pip install uwsgi# pip install pymongo
pip install pycrypto
pip install redis  |
| --- |

Bagaimana menginstal dan menjalankan program pada centos 6

 Instalasi:

| # Yum groupinstall &quot;Alat Pengembangan&quot;
# Yum install python 
# Yum install python-pip python-devel     
# Pip pasang uwsgi 
# Pip install pymongo
# Pip pasang pycrypto 
# Pip install MySQL-python |
| --- |

- Instal MySQL  pada runlevel mana yang akan dimulai:

**# Yum install mysql-server**

Kemudian untuk memulai server MySQL:

**# Service mysqld mulai**

Jalankan skrip mysql\_secure\_installation untuk mengatasi beberapa masalah keamanan di instalasi MySQL default.

**# Mysql\_secure\_installation**

Untuk login ke MySQL sebagai Root User:

**# Mysql -u root -p**

Saat diminta, masukkan kata sandi root yang Anda tetapkan saat skrip mysql\_secure\_installation dijalankan.

Anda kemudian akan disajikan dengan layar monitor MySQL:

**--Selamat datang di monitor MySQL--.**

        Perintah diakhiri dengan; Atau \ g.

        Id koneksi MySQL anda adalah 1

        Versi server: 5.1.73 Sumber distribusi

        Hak Cipta (c) 2000, 2013, Oracle dan / atau afiliasinya. Seluruh hak cipta.

**        Oracle**

        Oracle adalah merek dagang terdaftar dari Oracle Corporation dan / atau    afiliasinya.

        Nama lain mungkin merupakan merek dagang dari pemiliknya masing-masing.

        Ketik &#39;bantuan;&#39; Atau &#39;\ h&#39; untuk bantuan. Ketik &#39;\ c&#39; untuk menghapus pernyataan

    masukan saat ini.

-
  - Mysql membuat database kelasc;
  - Mysql&gt; keluar
  - Impor database ke database tujuan Anda di MySQL.

| # Cd tugas / docs
# Mysql -u root -p \*\*\*\*\*\* kelasc &lt;mysql.sql
# Cd .. |
| --- |

-
  - Kemudian, edit file peuyeum.ini. &lt;br&gt;
  - Untuk mengedit file pada baris perintah, Anda bisa menggunakan editor seperti vi.

| # Vi peuyeum.ini |
| --- |

        [Uwsgi]

        Modul = peuyeum: aplikasi

        Check-static = ./public

| Master = benar
Proses = 5
Http = 0.0.0.0:8080
#uid = peuyeum#socket = ../run/peuyeum.sock
# Chown-socket = peuyeum: peuyeum
# Chmod-socket = 660
#vacuum = true |
| --- |

-
  - Die-on-term = true
  - Setelah itu, edit file config.py:

| # Cd lib# Vi config.py |
| --- |

-
  - py
  - Atur paramater dari server anda

        &quot;&quot; &quot;

        ### Menu

        Keyuri = &quot;URI&quot;

        Tokenuri = &quot;TKN&quot;

        ### Database

        Mongohost = &quot;lokal&quot;

        Mongoport = 27017

        Mysqlhost = &quot;localhost&quot;

        Mysqldb = &quot;kelasc&quot;

        Mysqluser = &quot;root&quot;

        Mysqlpassword = &quot;kata sandi anda&quot;

        ### Modul keamanan

        Kunci = &quot;kunci Anda 16 char&quot;

        Iv = &quot;your iv 16 char&quot;

        Tokenurl = &quot;https://www.googleapis.com/oauth2/v3/tokeninfo?id\_token=&quot;

        Iss = &quot;accounts.google.com&quot;

        Aud = &quot;WEB\_CLIENT\_ID&quot;

        Domainacl = &quot;poltekpos.ac.id&quot;

        Urltimeout = 3600

        ### mapserver

        WMTS = &quot;http://peta.peuyeum.com/wmts/sampeu/ragi/{z}/{x}/{y}.png&quot;

- Terakhir , jalankan uwsgi di centos 6:

        # Cd ..

        # Uwsgi peuyeum.ini