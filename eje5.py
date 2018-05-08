#5. Pedir un id pelicula y contar
# cuantos generos tiene.
import json


from pprint import pprint
idd=input("Dime un id: ")
contador=0
with open('peliculas.json') as data_file:
	data = json.load(data_file)
for pelicula in data:
	if (pelicula["id"]) == idd:
		#for genero in pelicula["genres"]:
		#	contador=contador+1
		#print(contador)
		print("La pelicula con id", idd, "tiene", len(pelicula["genres"]), "género/s")
