import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'jambi'
		provloc = '103.616048, -1.610092'
		mapzoom = '9'
		kabkotcord = [
		'101.459556, -2.070815',
		'102.057124, -2.177450',
		'102.664399, -2.313669',
		'103.108822, -1.754890',
		'103.723340, -1.608084',
		'103.929264, -1.160174',
		'103.122444, -1.084338',
		'102.355956, -1.318974',
		'101.846269, -1.672173',
		'103.604032, -1.614553',
		'101.411225, -2.066537'
		]
		listkabkot = [
		'%1501%','%1502%','%1503%','%1504%','%1505%','%1506%','%1507%','%1508%','%1509%'
		'%1571%','%1572%'
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