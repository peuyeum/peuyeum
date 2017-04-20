import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'sumut'
		provloc = '99.188581, 2.312969'
		mapzoom = '9'
		kabkotcord = [
		'97.522109, 1.154846',
		'99.363823, 0.793299',
		'99.154356, 1.515302',
		'98.656347, 1.918657',
		'99.074889, 2.023261',
		'99.293638, 2.377321',
		'100.065178, 2.275284',
		'99.640398, 2.863302',
		'98.939155, 2.928528',
		'98.256026, 2.855924',
		'98.310077, 3.125848',
		'98.665443, 3.438689',
		'98.187571, 3.738034',
'97.744257, 0.799970',
'98.546646, 2.278004',
'98.293194, 2.562098',
		'98.771646, 2.602838',
'99.064781, 3.393886',
'99.481319, 3.235904',
'99.757415, 1.592403',
		'99.845183, 1.129026',
'100.129103, 1.840616',
'99.750471, 2.395324',
'97.364021, 1.303287',
		'97.419657, 1.053713',
'98.785090, 1.736999',
'99.798478, 2.965885',
'99.064177, 2.960991',
		'99.156183, 3.327379',
		'98.669479, 3.597733',
		'98.485410, 3.589259',
		'99.284581, 1.365369',
		'97.524199, 1.321364',
		'98.677986, 2.778086'
		]
		listkabkot = [
		'%1201%','%1202%','%1203%','%1204%','%1205%','%1206%','%1207%','%1208%','%1209%','%1210%',
		'%1211%','%1212%','%1213%','%1214%','%1215%','%1216%','%1217%','%1218%','%1219%','%1220%',
		'%1221%','%1222%','%1223%','%1224%','%1225%',
		'%1271%','%1272%','%1273%','%1274%','%1275%','%1276%','%1277%','%1278%','%1288%'
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