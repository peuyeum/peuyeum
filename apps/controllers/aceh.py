import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'aceh'
		listkabkot = [
		'%1101%','%1102%','%1103%','%1104%','%1105%','%1106%','%1107%','%1108%','%1109%','%1110%',
		'%1111%','%1112%','%1113%','%1114%','%1115%','%1116%','%1117%','%1118%',
		'%1171%','%1172%','%1173%','%1174%','%1175%'
		]
		provloc = '96.678095, 4.311709'
		mapzoom = '9'	
		kabkotcord = [
		'96.148572, 2.575907',
		'98.007934, 2.394270',
		'97.985961, 2.405247',
		'97.399985, 3.146819',
		'97.718681, 3.354321',
		'97.619763, 4.609502',
		'96.855822, 4.504795',
		'96.187114, 4.480072',
		'96.022189, 5.018921',
		'96.583919, 5.050867',
		'96.623012, 5.092543',
		'97.147885, 5.003163',
		'96.894666, 3.839563',
		'97.356257, 3.950720',
		'97.935478, 4.262269',
		'96.497302, 4.179051',
		'95.679848, 4.827339',
		'97.008816, 4.773369',
		'96.238460, 5.154692',
		'95.327326, 5.554093',
		'95.342258, 5.867014',
		'97.122396, 5.175647',
		'97.889437, 2.724339'
		]
		batik.provinsi(provinsi,listkabkot,provloc,mapzoom,kabkotcord)
		cal = calendar.Calendar()
		dt = {}
		for kabkot in listkabkot:
			dt[kabkot]=cal.getYearCountKabKot(str(int(kabkot[1:3])),str(int(kabkot[3:5])),uridt)
		dt['%WMTS%']=getWMTS()
		dt['%PERIODE%']=uridt
		dt['%LAMAN INDONESIA%']=urlEncode16(keyuri+'%peta%home'+'%'+uridt)
		dt['%TAHUN SEBELUMNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)-1))
		dt['%TAHUN SETELAHNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)+1))
		cal.close()
		return dt