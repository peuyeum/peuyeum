import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'sumsel'
		provloc = '104.669016, -2.929209'
		mapzoom = '9'
		kabkotcord = [
		'104.088588, -4.107725',
		'105.374245, -3.338106',
		'104.005788, -3.762634',
		'103.423180, -3.796126',
		'103.122779, -3.164189',
		'103.830211, -2.438087',
		'105.054037, -2.491875',
		'103.905171, -4.578598',
		'104.565937, -4.056827',
		'104.597077, -3.410024',
		'102.927196, -3.749890',
		'103.992169, -3.212477',
		'102.711294, -2.734880',
		'104.740084, -2.968469',
		'104.238309, -3.455368',
		'103.264261, -4.103628',
		'102.859608, -3.299299',
		'103.907185, -4.831922'
		]
		listkabkot = [
		'%1601%','%1602%','%1603%','%1604%','%1605%','%1606%','%1607%','%1608%','%1609%','%1610%',
		'%1611%','%1612%','%1613%',
		'%1671%','%1672%','%1673%','%1674%','%1688%'
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