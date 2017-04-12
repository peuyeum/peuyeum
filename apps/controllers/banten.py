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
		provloc = '106.052411, -6.399373'
		mapzoom = '9'
		kabkotcord = [
		'106.114254, -6.326809',
		'106.234365, -6.360833',
		'106.485909, -6.156607',
		'106.108131, -6.191190',
		'106.648314, -6.204330',
		'106.008973, -6.003815',
		'111.527879, -7.630911',
		'106.701516, -6.284919'
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