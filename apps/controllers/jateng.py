import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,keyuri,setTTL
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'jateng'
		listkabkot = [
		'%3301%','%3302%','%3303%','%3304%','%3305%','%3306%','%3307%','%3308%','%3309%','%3310%',
		'%3311%','%3312%','%3313%','%3314%','%3315%','%3316%','%3317%','%3318%','%3319%','%3320%',
		'%3321%','%3322%','%3323%','%3324%','%3325%','%3326%','%3327%','%3328%','%3329%',
		'%3371%','%3372%','%3373%','%3374%','%3375%','%3376%'
		]
		provloc = '109.945218, -7.284288'
		mapzoom = '9'
		kabkotcord = [
		'108.842237, -7.471174',
		'109.184998, -7.438573',
		'109.418501, -7.318796',
		'109.649131, -7.349061',
		'109.622358, -7.637793',
		'110.023972, -7.721327',
		'109.908372, -7.394262',
		'110.244757, -7.493802',
		'110.658770, -7.421050',
		'110.600926, -7.675459',
		'110.842407, -7.675339',
		'110.991364, -7.899248',
		'111.033809, -7.614131',
		'110.968307, -7.372507',
		'110.903759, -7.102690',
		'111.390128, -7.069585',
		'111.449333, -6.769833',
		'111.069968, -6.746277',
		'110.870712, -6.790130',
		'110.773890, -6.573575',
		'110.429145, -7.008073',
		'110.636568, -6.891042',
		'110.143177, -7.247370',
		'110.167539, -7.004711',
		'109.859251, -7.021758',
		'109.672786, -6.893896',
		'109.397830, -7.024089',
		'109.144876, -7.026439',
		'108.906710, -7.068114',
		'110.218039, -7.473393',#3371
		'110.820013, -7.555974',
		'110.496440, -7.335682',
		'110.462048, -7.250925',
		'109.617024, -7.045267',
		'109.119470, -6.868013'
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