import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'lampung'
		provloc = '105.248220, -5.295055'
		mapzoom = '9'
		kabkotcord = [
		'104.187577, -5.037602',
		'104.575340,-5.429636',
		'105.476069,-5.491557',
		'105.517748,-5.084708',
		'105.204016,-4.871163',
		'104.843685,-4.778225',
		'104.585361,-4.489734',
		'105.500304,-4.336239',
		'105.093154,-5.490262',
		'104.920059,-5.325281',
		'105.429819, -3.990466',
		'105.092256, -4.457518',
		'104.161716, -5.331558',
		'105.267130, -5.416955',
		'105.309897, -5.122207',
		'103.893686, -4.913788'
		]
		listkabkot = [
		'%1801%','%1802%','%1803%','%1804%','%1805%','%1806%','%1807%','%1808%','%1809%','%1810%',
		'%1811%','%1812%','%1813%',
		'%1871%','%1872%','%1888%'
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