import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'kalsel'
		provloc = '115.411328, -2.914826'
		mapzoom = '8'
		kabkotcord = [
		# '115.94679969999993' , '-3.0029841'
		# '114.99914639999997' , '-3.3200228'
		'114.66679390000002' , '-3.0714738'
		'115.04659909999998' , '-2.9160746'
		'115.2363408' , '-2.7662681'
		'115.52073580000001' , '-2.615316200000001'
		'115.18891600000006' ,'-2.4421225'
		'115.56810840000003' , '-1.864302'
		
		
		]
		listkabkot = [
		'%6310%','%6311%','%6371%','%6372%'
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