# Peuyeum Framework
Geospatial Web Application Framework

## peuyeum.ini
~~~
[uwsgi]
module = peuyeum:application
check-static = ./public

master = true
processes = 5
#http = 127.0.0.1:8181
uid = peuyeum
socket = ../run/peuyeum.sock
chown-socket = peuyeum:peuyeum
chmod-socket = 660
vacuum = true

die-on-term = true
~~~
### Penjelasan
~~~
[uwsgi]
~~~

Code tersebut maksudnya adalaah menetapkan bagian yang disebut [uwsgi]. Bagian ini adalah di mana semua item konfigurasi kita akan hidup. yang akan dimulai dengan mengidentifikasi aplikasi kita.  uWSGI server perlu tahu di mana callable aplikasi tersebut.<p>
uWSGI adalah open source, multiplatform, dan baris perintah software diimplementasikan dalam bahasa C sehingga Anda perlu kompiler C (seperti gcc atau dentang) dan header pengembangan Python dan dirancang dari bawah ke atas sebagai alat mandiri untuk mengembangkan stack penuh untuk menghasilkan atau membangun layanan hosting.<p>

~~~
module = peuyeum:application
~~~

Selanjutnya  source code tersebut mengkonfigurasi uWSGI sehingga menangani identifikasi aplikasi kita dengan benar, dengan menunjukkan lingkungan virtual untuk aplikasi tersebut. Dengan menetapkan modul, agar dapat menunjukkan dengan tepat bagaimana cara untuk  dapat berinteraksi dengan aplikasi tersebut (dengan mengimpor "application" callable dari file peuyeum.py dalam direktori proyek). <p>
~~~
check-static = ./public
~~~

Source code diatas dimaksudkan untuk memeriksa kebenaran dari berbagai kendala program dapat dianggap sebagai bentuk diperpanjang untuk  memeriksa jenis, hal  dilakukan secara otomatis pada waktu kompilasi, bersifat public<p>

~~~
master = true
processes = 5
~~~

sourcode diatas dimaksudkan dengan menciptakan sebuah proses master dengan 5 pekerja dari proses tersebut.<br>
Selanjutnya maksud source code tersebut adalah menandai proses uwsgi awal sebagai master dan kemudian menelurkan sejumlah proses pekerja.<p>

~~~
#http = 127.0.0.1:8181
uid = peuyeum
~~~

Selanjtunya mengubah protokol yang menggunakan uWSGI untuk berbicara dengan dunia luar. Ketika menguji aplikasi tersebut, kita ditentukan -protocol = http sehingga kita bisa melihatnya dari web browser. Karena kita akan mengkonfigurasi Nginx sebagai reverse proxy di depan uWSGI, kita dapat mengubah ini. Nginx menerapkan mekanisme uwsgi proxy, yang merupakan protokol biner cepat yang uWSGI dapat digunakan untuk berbicara dengan server lain. Protokol uwsgi sebenarnya default protokol uWSGI, sehingga hanya dengan menghilangkan spesifikasi protokol, itu akan jatuh kembali ke uwsgi.<p>

~~~
socket = ../run/peuyeum.sock
chown-socket = peuyeum:peuyeum
chmod-socket = 660
~~~

Selanjutnya source code tersebut berfungsi untuk merancang konfigurasi untuk digunakan dengan Nginx, dan juga akan mengubah penggunaan port jaringan dan menggunakan soket Unix sebagai gantinya. Ini lebih aman dan lebih cepat. soket akan dibuat dalam direktori saat ini jika kita menggunakan path relatif. Misalnya pada source code tersebut adalah ../run/peuyeum.sock.  selanjutnya mengubah hak akses untuk "660" sehingga Nginx dapat mengakses nya (untuk itu akan dimulai uWSGI dengan kelompok www-data yang menggunakan Nginx.<p> 
~~~
die-on-term = true
~~~

Source code tersebut maksudnya ditambahkan sebagai sebuah opsi sehingga uWSGI akan membunuh proses bukan reload yang terjadi, hal ini perlu karena akan terciptanya file Upstart untuk memulai aplikasi saat boot. Upstart dan uWSGI memiliki ide yang berbeda tentangyang sinyal SIGTERM harus lakukan terhadapsebuah aplikasi. Untuk memilah perbedaan ini sehingga proses dapat ditangani seperti yang diharapkan dengan Upstart.<p>
## peuyeum.py
~~~
#!/usr/bin/env python

from cgi import parse_qs
from lib import basreng,cilok,sampeu

def application(environ, start_response):
	## passing environ uwsgi PARAM
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH', 0))
	except (ValueError):
		request_body_size = 0
	origin = environ['REQUEST_URI']
	request_body = environ['wsgi.input'].read(request_body_size)
	post = parse_qs(request_body)
	## Menu Logic
	url=cilok.urlDecode16(origin[1:])
	uri=url.split('%')
	if sampeu.getMenu(uri[0])=="key":
		mod = 'apps.controllers.'+uri[1]
		func = uri[2]
		a = __import__(mod,fromlist=['Controller'])
		b = getattr(a,'Controller')()
		rep=getattr(b,func)(uri[3])
		text = sampeu.getHtml(uri[1])
		
		result = basreng.dictView(rep,text)

		hbegin = sampeu.getHtmlBegin()
		hend = sampeu.getHtmlEnd()

		respon = hbegin + result + hend
	elif sampeu.getMenu(uri[0])=="token":
		mod = 'apps.api.'+uri[1]
		func = uri[2]
		a = __import__(mod,fromlist=['Api'])
		b = getattr(a,'Api')()
		respon = getattr(b,func)(uri[3],post)
	else:
		respon = """
		<html>
		<head><title>403 Porbidden</title></head>
		<body bgcolor="white">
		<center><h1>403 Porbidden</h1></center>
		<hr><center>peuyeum/bdg</center>
		</body>
		</html>
		"""
	## Passing HTML to client
	start_response('200 OK', [('Content-Type', 'text/html'),('Content-Length', str(len(respon)))])
	return [respon]
~~~
## Penjelasan

~~~
from cgi import parse_qs
~~~

source code  tersebut berfungsi untuk memanggil function parse_gs yang terdapat didalam module cgi<p>

~~~
def application(environ, start_response):
~~~

Kode diatas merupakan aplikasi WSGI yang lengkap. Secara default, uWSGI akan mencari aplikasi yang callable, oleh karena itu function applicationdi panggil. Seperti pada source code diatas, dibutuhkan dua parameter.<p>
Yang pertama yaitu environ karena itu akan menjadi variabel all-key seperti nilai lingkungan.<p>
Yang kedua disebut start_response dan nama aplikasi yang akan digunakan secara internal untuk merujuk ke server web (uWSGI) yang dapat dipanggil. Kedua nama parameter ini dipilih hanya karena penggunaannya dalam contoh di spesifikasi PEP 333 yang Mendefinisikan interaksi WSGI<p>

