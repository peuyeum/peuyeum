import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'pabar'
		provloc = '133.1747162, -1.3361154'
		mapzoom = '9'
		kabkotcord = [
		'133.0194897, -3.097706',
		'133.9436788, -3.288406',

		'134.3236557, -2.8551699',
		'133.329466, -1.9056848',
		'134.0620421, -0.8614531',
		'132.1572702, -1.7657744',
		'131.255828, -0.8761629',
		'130.5052176, -1.0320468',
		'132.3938375, -0.781856',
		'132.3150993, -1.2970979',
		# '134.0008674, -0.9135107',
		# '134.0620421, -0.8614531',
		'131.312243, 0.885879'

		'131.255.828, -0.876163'
		]
		listkabkot = [
		'%9101%','%9102%','%9103%','%9104%','%9105%','%9106%','%9107%','%9108%','%9109%','%9110%',
		'%9111%','%9112%',
		'%9171%'
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