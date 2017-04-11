import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'riau'
		provloc = '101.683500, 0.336998'
		mapzoom = '9'
		kabkotcord = [
		'101.256639, -0.397666',
		'102.27297, -0.665561',
		'103.224913,-0.179860',
		'102.245931,0.243687',
		'101.805764,0.806023',
		'101.121585,0.364270',
		'100.482103,0.953634',
		'1144033,101.687431,1.371394',
		'100.772193,1.804440', 
		'102.602121,0.997156',
		'101.471132,0.555383',
		'101.315122,1.816591'
		]
		listkabkot = [
		'%1401%','%1402%','%1403%','%1404%','%1405%','%2101%','%2102%','%2103%','%2104%','%2105%',
		'%2171%','%2172%'
		]
		batik.provinsi(provinsi,listkabkot,provloc,mapzoom,kabkotcord)
		cal = calendar.Calendar()
		dt = {}
		for kabkot in listkabkot:
			dt[kabkot]=cal.getYearCountKabKot(str(int(kabkot[1:3])),str(int(kabkot[3:5])),uridt)
		cal.close()
		dt['%WMTS%']=getWMTS()
		dt['%PERIODE%']=uridt
		dt['%LAMAN INDONESIA%']=urlEncode16(keyuri+'%peta%home'+'%'+uridt)
		dt['%TAHUN SEBELUMNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)-1))
		dt['%TAHUN SETELAHNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)+1))
		return dt