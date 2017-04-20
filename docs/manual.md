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
