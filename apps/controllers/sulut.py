import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'sulut'
		provloc = '123.9750018, 0.6246932'
		mapzoom = '9'
		kabkotcord = [
		'124.06414189999998, 0.6870994',
		'124.8182593, 1.2168837',
		'125.5000999, 3.6329172',
		'126.8034921, 4.3066741',
		'124.4641848, 1.0946773',
		'124.994751, 1.5327973',
		'123.2657311, 0.9070359',
		'125.4124355, 2.345964',
		'124.7298765, 1.0278551',
		'123.8411288, 0.4053215',
		'124.4641848, 0.7152651',
		'1.248.420.794, 14.748.305',
		 '12.512.085.847, 143.887.284',
		 '12.484.085.142, 132.286.934',
		 '1.243.199.316, 0.72409437',
		# '1.248.955.195, 12.236.791,
		]
		listkabkot = [
		'%7101%','%7102%','%7103%','%7104%','%7105%','%7106%','%7107%','%7108%','%7109%','%7110%',
		'%7111%',
		'%7171%','%7172%','%7173%','%7174%','%7188%'
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