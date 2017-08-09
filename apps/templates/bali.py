import batik
import sys
import os

views_path = '../views/'+__file__.split('.')[0]
if not os.path.exists(views_path):
	os.makedirs(views_path)
sys.stdout = open(views_path+'/index.batik','w')

kabkot = ['%5101%','%5102%','%5103%','%5104%','%5105%','%5106%','%5107%','%5108%','%5171%']
provloc = '115.184055, -8.425745'
kabkotcord = [
'114.701385, -8.295495',
'115.055052, -8.435786',
'115.178503, -8.534605',
'115.323008, -8.230679',
'115.542554, -8.719174',
'115.354594, -8.454195',
'115.570658, -8.382352',
'114.958329, -8.227131',
'115.211556, -8.669962'
]


batik.kabkot(kabkot,provloc,kabkotcord)
