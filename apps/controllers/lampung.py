import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'lampung'
		provloc = '105.248220, -5.295055'
		mapzoom = '9'
		kabkotcord = [
		'104.193063, -5.032130',
		'104.671493, -5.379051',
		'105.509049, -5.490190',
		'105.591926, -5.134634',
		'105.263090, -4.862953',
		'104.803865, -4.809700',
		'104.613519, -4.514942',
		'105.532582, -4.372526',
		'105.104489, -5.463606',
		'104.920791, -5.329430',
		'105.376261, -4.020605',
		'105.115601, -4.315114',
		'104.046358, -5.259768',
		'105.264212, -5.399865',#71
		'105.307924, -5.118348',
		'103.922607, -4.932111'
		]
		listkabkot = [
		'%1801%','%1802%','%1803%','%1804%','%1805%','%1806%','%1807%','%1808%','%1809%','%1810%',
		'%1811%','%1812%','%1813%',
		'%1871%','%1872%','%1888%'
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