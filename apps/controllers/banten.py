import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'banten'
		listkabkot = [
		'%3601%','%3602%','%3603%','%3604%',
		'%3671%','%3672%','%3673%','%3674%'
		]
		provloc = '106.143949, -6.460788'
		mapzoom = '9'
		kabkotcord = [
		'105.790328, -6.572485',
		'106.208272, -6.655552',
		'106.650031, -6.181121',
		'106.167182, -6.109267',
		'106.485223, -6.173674',
		'106.011024, -6.004235',
		'106.134223, -6.223955',
		'106.712159, -6.305395'
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