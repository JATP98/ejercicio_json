#1. Muestrame el titulo y la duracion.

import json


from pprint import pprint

with open('peliculas.json') as data_file:
	data = json.load(data_file)
for x in data:
	print(x["title"])
	if x["duration"] == "":
		print("Duracion vacia")
		print("------------")
	else:
		print(x["duration"])
		print("------------")
