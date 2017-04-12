import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'malut'
		provloc = '127.867580, 0.641499'
		mapzoom = '9'
		kabkotcord = [
		'127.60705673,1.39740732',
		'128.35871739999993,0.4419543',
		# '125.9128434, -2.1216504',
		# '127.7237678, -1.5109015',
		# '127.8936663, 1.5074308',
		# '128.4849923, 1.3121235',
		# '128.4008357, 2.3656672',
		# '124.7740793, -1.8268344',
		# '127.3613533, 0.7957999',#71
		'127.681228, 0.5060207'
		]
		listkabkot = [
		'%8201%','%8202%','%8203%','%8204%','%8205%','%8206%','%8207%','%8208%',
		'%8271%','%8272%'
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