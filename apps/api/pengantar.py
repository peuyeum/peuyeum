import sys
sys.path.append('../../')
from lib.cilok import urlEncode16
from apps.models import pengantar

class Api(object):
	def getList(self,kabkotno='null',postdata='null'):
		periode = postdata.get('periode', [''])[0]
		cal = calendar.Calendar()
		id_prov = kabkotno[:2]
		id_kabkot = str(int(kabkotno[2:]))
		agendalist_arr = cal.getYearAllDataKabKot(id_prov,id_kabkot,periode)
		try :
			list_on_html = '<ul>'
			for agendalist in agendalist_arr:
				stragd = str(agendalist)
				sumlist = stragd.split("SUMMARY:",1)[1].rsplit('DTSTART', 1)[0].replace('\\r\\n', '')
				list_on_html = list_on_html+'<li>'+sumlist+'</li>'
			list_on_html = list_on_html+'</ul>'
		except IndexError:
			list_on_html='Belum ada kunjungan'
		return list_on_html
	
	def postLoc(self,getdt='null',postdt='null'):
		lokasi = postdt.get('loc', [''])[0]
		sumber = postdt.get('sumber', [''])[0]
		peng = pengantar.Pengantar()
		#uid = getdt
		return peng.setLokasi(sumber,lokasi)