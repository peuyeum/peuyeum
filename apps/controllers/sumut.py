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
		'97.604550, 1.014795',
		'99.495703, 0.768582',
		'99.16264, 1.509810',
		'98.624952, 1.951664',
		'98.927957, 1.994440',
		'99.279916, 2.279898',
		'0.821941, 97.759366',
		'3.764071, 98.061242',
		'3.414014, 98.751974',
		'3.099794, 98.339607',
		'2.867582,98.352160',
		'3.019149,98.815741',
		'2.765916,99.518179',
		'2.278715,98.582038',
		'2.268484,98.571455',
		'2.560726,98.247536',
		'98.612349, 2.495827',
		'99.078520, 3.366468',
		'99.480677, 3.237990',
		'99.752107, 1.582852',
		'99.834382, 1.137306',
		'100.126363, 1.852969',
		'99.754776, 2.402272',
		'97.492443, 1.044102',
		'97.473903, 1.042729',
		'98.781743, 1.739830',
		'99.79854569999998, 2.9662346',
		'99.06816679999997, 2.970042',
		'99.15668549999998, 3.3262879',
		'98.67222270000002, 3.5951956',
		'98.5025286, 3.6135482',
		'99.27301460000001, 1.3721801',
		'97.54638849999992, 1.335263',
		'98.61606740000002, 2.7860786'
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