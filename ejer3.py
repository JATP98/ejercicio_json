#3. Pedir un id y mostrar el titulo 
#y el genero

import json


from pprint import pprint
idd=int(input("Dime un ID: "))

with open('peliculas.json') as data_file:
	data = json.load(data_file)
for x in data:
	if int(x["id"]) == idd:
		print(x["title"])
		print(x["genres"])
