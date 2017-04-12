import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'kaltim'
		provloc = '116.365086, 0.659612'
		mapzoom = '9'
		kabkotcord = [
		
		'-1.7175266, 115.94679969999993',
		'-0.4051796, 115.85217639999996',
		# '-0.1336655, 116.6081653',
		# # '0.9433774, 116.98524220000002',
		# # '2.0450883, 117.36164759999997',
		# # '-1.2917094, 116.51379640000005'
		]
		listkabkot = [
		'%6401%','%6402%','%6403%','%6404%','%6405%','%6409%'
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