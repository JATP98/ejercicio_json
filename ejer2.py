#2. pedir una nota y contar las peliculas con esa nota o mayor
import json
from pprint import pprint
contador=0
with open('peliculas.json') as data_file:
	data = json.load(data_file)
pedir=float(input("Introduce una nota: "))
for nota in data:
	if type(nota["imdbRating"])!=str:
		if nota["imdbRating"] >=pedir:
			contador=contador+1
print ("Hay ", contador, "peliculas con mas o igual de un", pedir," de nota")
