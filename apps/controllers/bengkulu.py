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
		'103.007302, -4.324655',
		'102.678929, -3.439491',
		'101.987230, -3.278322',
		'103.393361, -4.641259',
		'102.652754, -4.040548',
		'101.444109, -2.675844',
		'102.260408, -3.123849',
		'102.630506, -3.619429',
		'102.400284, -3.578422',
		'103.021079, -4.334965'
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
