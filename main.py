from arffclass import *


if __name__ == "__main__":

	
	file = arffGenerator()
	file.setDatas(20)					# cantidad de datos que genera
	file.setRelation("meteoritos")		# nombre de la relacion y del archivo
	file.setFileName("prueba")			# nombre del archivo
		
	# ------ valor del atributo clasificacion ------
	# file.setClass( [valor1, valor2, valor3, ....])	
	file.setClass(["Coronis", "Eos", "Temis", "Flora", "Maria"])

	# ------ valores a tomar de cada atributo ------ 				
	# file.setAttribute( atributo, [valor1, valor2, valor3, ....])	
	file.setAttribute("tiporoca", ["arcilla", "niquel", "hierro", "desconocido"])
	file.setAttribute("diametro", [ 1, 2, 3, 4, 5] )
	file.setAttribute("masa", [2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3])
	file.setAttribute("forma", ["dentada", "irregular"])
	file.setAttribute("riezgoimpacto", ["bajo", "medio", "alto"])


	file.randomize()		# general el archivo .arff con datos random a partir de los atributos y valores datos
