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
		'101.660183, 0.759335',
		'103.40494450000006, 0.7697664999999999',
		'104.51892139999995, 1.0619173',
		'108.14286689999994, 3.9456514',
		'104.4257533, -0.4726065', 
		'105.75859079999998, 2.923624',
		'103.98401999999999, 1.0458378',
		'104.46650720000002, 0.9185504'
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