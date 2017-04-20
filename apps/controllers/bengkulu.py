import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'bengkulu'
		listkabkot = [
		'%1701%','%1702%','%1703%','%1704%','%1705%','%1706%','%1707%','%1708%','%1709%'
		'%1771%'
		]
		provloc = '102.265780, -3.793485'
		mapzoom = '9'
		kabkotcord = [
		'103.030005, -4.334280',
		'102.674809, -3.429895',
		'101.896590, -3.185087',
		'103.385116, -4.623465',
		'102.633522, -4.054247',
		'101.433101, -2.642920',
		'102.260408, -3.123849',
		'102.630506, -3.619429',
		'102.400284, -3.578422',
		'102.264410, -3.793830'
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