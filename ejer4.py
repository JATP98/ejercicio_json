#4. Pedir un actor y contar las
# peliculas en las que haya participado.

import json


from pprint import pprint
actor=input("Dime un actor: ")
contador=0
with open('peliculas.json') as data_file:
	data = json.load(data_file)
for pelicula in data:
	for nombre in pelicula["actors"]:
		if nombre == actor:
			contador=contador+1
print("Este actor participa en",contador, "pelicula/s")
