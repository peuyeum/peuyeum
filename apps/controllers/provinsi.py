import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,keyuri,setTTL
from lib.sampeu import getWMTS
from apps.models import calendar

class Controller(object):
	def jateng(self,uridt='null'):
		listkabkot = [
		'%PROV3301%','%PROV3302%','%PROV3303%','%PROV3304%','%PROV3305%','%PROV3306%','%PROV3307%','%PROV3308%','%PROV3309%','%PROV3310%',
		'%PROV3311%','%PROV3312%','%PROV3313%','%PROV3314%','%PROV3315%','%PROV3316%','%PROV3317%','%PROV3318%','%PROV3319%','%PROV3320%',
		'%PROV3321%','%PROV3322%','%PROV3323%','%PROV3324%','%PROV3325%','%PROV3326%','%PROV3327%','%PROV3328%','%PROV3329%',
		'%PROV3371%','%PROV3372%','%PROV3373%','%PROV3374%','%PROV3375%','%PROV3376%'
		]
		cal = calendar.Calendar()
		dt = {}
		for kabkot in listkabkot:
			dt[kabkot]=cal.getYearCountKabKot(str(int(kabkot[1:3])),str(int(kabkot[3:5])),uridt)
		dt['%WMTS%']=getWMTS()
		dt['%PERIODE%']=uridt
		dt['%TAHUN SEBELUMNYA%']=urlEncode16(keyuri+'%jateng%home'+'%'+str(int(uridt)-1))
		dt['%TAHUN SETELAHNYA%']=urlEncode16(keyuri+'%jateng%home'+'%'+str(int(uridt)+1))
		cal.close()
		return dt