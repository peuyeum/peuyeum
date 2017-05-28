import redis

class Pengantar():
	def __init__(self):
		self.db = redis.Redis()
		
	def setLokasi(self,sumber,lokasi):
		return self.db.set(sumber,lokasi)
		
	def getLokasi(self,sumber):
		return self.db.get(sumber)