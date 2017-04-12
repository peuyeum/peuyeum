import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'kalteng'
		provloc = '113.913977,-2.2161048'
		mapzoom = '7'
		kabkotcord = [
		'111.555839, -2.456964',
		'112.737093, -2.098138',
		'114.380207, -2.920394',
		#'114.8092691, -1.875943',
		#'115.094045, -0.9587136',
		#'111.2368084,-2.6267517',
		'111.2845025,-1.8526377',
		'112.4291464,-3.0123467',
		'112.8105512,-0.9758379',
		'113.9536466,-2.6849607',
		'113.5728501,-1.2522464',
		'115.188916,-2.0123999',
		'114.3341432,-0.1362171',
		'113.914539, -2.216049'
		]
		listkabkot = [
		'%6201%','%6202%','%6203%','%6204%','%6205%','%6206%','%6207%','%6208%','%6209%','%6210%',
		'%6211%','%6212%','%6213%',
		'%6271%'
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