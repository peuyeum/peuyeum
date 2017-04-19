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
		'96.060445, 2.669019',
		'97.922151, 2.384000',
		'97.988713, 2.538332',
		'97.676114, 3.388599',
		'97.618384, 4.627398',
		'96.855833, 4.528079',
		'96.187806, 4.468440',
		'95.53111, 5.365889',
		'95.972559, 5.081671',
		'96.623012, 5.092543',
		'97.147885, 5.003163',
		'96.896034, 3.824400',
		'97.354895, 3.983611',
		'97.953342, 4.233520',
		'96.497994, 4.163305',
		'95.679848, 4.827339',
		'97.008816, 4.773369',
		'96.243269, 5.054155',
		'95.339173, 5.560588',#71
		'95.3422588, 5.867014',
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