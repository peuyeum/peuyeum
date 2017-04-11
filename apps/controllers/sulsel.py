import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'sulsel'
		# provloc = '119.9740534, -3.6687994'
		mapzoom = '9'
		kabkotcord = [
		'120.481566, -6.040677',
		'120.214471, -5.415704',
		'120.026454, -5.513190',
		'119.970836, -5.461244',
		'119.496695, -5.408397',
		'18.119.6730939,-5.554579',
	 	'19.119.6730939,-5.554579',
	  	'20.119.4875668,-5.4162493',
	  	'21.19.742604,-5.3102888',
	  	'22.120.112735,-5.2171961',
	  	'23.119.6962677,-5.0549145',
	  	'24.119.5571677,-4.805035',
	  # '25.119.6499162,-4.436417',
	  # '26.120.0665236,-4.7443383',
	  # '27.119.9277947,-4.3518541',
		'119.819438, -3.486817',
		'120.154072, -3.36392',
		'119.712573, -3.066465',
		'120.001852, -2.22533',
		'121.073119, -2.52923',
		'119.796522, -2.833211',
		'119.46058, -5.152792',
		'119.6290617, -4.0096221',
		'120.1985141, -3.0016343'
		]
		listkabkot = [
		'%7301%','%7302%','%7303%','%7304%','%7305%','%7306%','%7307%','%7308%','%7309%','%7310%',
		'%7311%','%7312%','%7313%','%7314%','%7315%','%7316%','%7317%','%7318%',
		'%7322%','%7325%','%7326%',
		'%7371%','%7372%','%7373%'
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