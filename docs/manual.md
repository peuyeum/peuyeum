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
