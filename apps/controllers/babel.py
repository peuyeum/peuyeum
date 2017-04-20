import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'babel'
		listkabkot = [
		'%1901%','%1902%','%1903%','%1904%','%1905%','%1906%',
		'%1971%'
		]
		provloc = '106.400525, -2.755146'
		mapzoom = '9'
		kabkotcord = [
		'105.934932, -1.895816',
		'107.670962, -2.863657',
		'105.506129, -1.900851',
		'106.309493, -2.484852',
		'106.429581, -2.856389',
		'108.106855, -2.883306',
		'106.117265, -2.132463'
		]
		batik.provinsi(provinsi,listkabkot,provloc,mapzoom,kabkotcord)
		cal = calendar.Calendar()
		dt = {}
		for kabkot in listkabkot:
			dt[kabkot]=cal.getYearCountKabKot(str(int(kabkot[1:3])),str(int(kabkot[3:5])),uridt)
		dt['%WMTS%']=getWMTS()
		dt['%PERIODE%']=uridt
		dt['%LAMAN INDONESIA%']=urlEncode16(keyuri+'%peta%home'+'%'+uridt)
		dt['%TAHUN SEBELUMNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)-1))
		dt['%TAHUN SETELAHNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)+1))
		cal.close()
		return dt