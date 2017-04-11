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
		'122.532670, -0.969612',
		'122.345902, -1.051996',
		'121.939852, -2.704650',
		'120.753889, -1.395064',
		'119.824081, -0.493822',
		'120.766576, 0.939380',
		'121.195815, 1.021996',
		'120.196286, 0.446431',	
		'122.59768409999992, -5.4700112',
		'122.51297420000003, -3.9984597 122',
		'121.90179539999997, -4.2279225',
		'122.08374449999997, -3.3803291',
		'123.03387670000006, -4.702342400000001 ',
		'122.9888319, -5.3096355',
		'122.6277455, -4.901629',
		# '122.0837445, -3.9380432',
		# '121.5826642, -3.9946988',
		# '122.4467238, -4.2027915',
		# '121.9017954, -4.6543462',
		# '123.5951925, -5.3264442',
		# '121.1710389, -3.1347227'
		]
		listkabkot = [
		'%7201%','%7202%','%7203%','%7204%','%7205%','%7206%','%7207%','%7208%','%7209%','%7210%',
		'%7211%','%7212%',
		'%7271%' ,'%7401%', '%7402%', '%7403%', '%7404%', '%7405%', '%7406%', '%7407%', '%7408%'
		
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