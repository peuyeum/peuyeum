import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'kalbar'
		provloc = '110.744972, -0.106978'
		mapzoom = '9'
		kabkotcord = [
		'109.394171, 1.389769', #1
		'109.481905, 0.854382', #2
		'109.682503, 0.488883', #3
		'109.334981, -0.026468', #4
		'110.583773, 0.339188', #5
		'110.495882, -0.979122', #6
		'111.478160, 0.052806', #7
		'112.623024, 0.784983',
		'110.870048, 0.007041',
		'111.693579, -0.707734',
		'110.009022, -1.053846',
		'109.47712, -0.4197',
		'109.345623, -0.025095', #71
		'108.974741, 0.910971'
		]
		listkabkot = [
		'%6101%','%6102%','%6103%','%6104%','%6105%','%6106%',
		'%6107%',
		'%6108%','%6109%','%6110%',
		'%6111%','%6112%',
		'%6171%','%6172%'
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