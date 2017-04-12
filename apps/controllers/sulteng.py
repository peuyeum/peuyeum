import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'sulteng'
		provloc = '121.8020017, -3.5562244'
		mapzoom = '7'
		kabkotcord = [
		'1.226.277.455,  -0.95616761',
		'12.262.754.112, -0.956083688',
		'12.190.256.788, -269.649.398',
		'12.075.484.488, -139.408.592',
		'1.198.352.303, -0.4233155'
		#'120.757983, 0.876823',
		#'121.354163, 0.969545',
		#'120.803947, 0.581761',
		#'121.537000, -1.098757',
		#'119.881520, -1.385990',
		'123.550408, -1.673453',
		'121.354163, -1.631176',
		'119.877999, -0.900291',
	
		'122.59768409999992, -5.4700112',
		'122.51297420000003, -3.9984597 122',
		'121.90179539999997, -4.2279225',
		'122.08374449999997, -3.3803291',
		'123.03387670000006, -4.702342400000001 ',
		'122.9888319, -5.3096355',
		'122.6277455, -4.901629',
		'122.0837445, -3.9380432',
		'121.5826642, -3.9946988',
		'122.4467238, -4.2027915',
		'121.9017954, -4.6543462',
		'123.5951925, -5.3264442',
		'121.1710389, -3.1347227'
		]
		listkabkot = [
		'%7201%','%7202%','%7203%','%7204%','%7205%','%7206%','%7207%','%7208%','%7209%','%7210%','%7211%','%7212%','%7271%'
		,'%7472%'
		,'%7471%','%7411%','%7410%','%7409%','%7401%', '%7402%', '%7403%', '%7404%', '%7405%', '%7406%', '%7407%', '%7408%'
		
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