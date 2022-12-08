"""
EN: Example of how to use the arffGenerator class to produce an .arff file.
ES: Ejemplo de uso de la clase arffGenerator para producir un archivo .arff.
"""

from arffclass import *


if __name__ == "__main__":

	file = arffGenerator()
	file.setDatas(20)					# EN: number of data rows to generate 	/ ES: cantidad de datos que genera
	file.setRelation("meteoritos")		# EN: relation name 					/ ES: nombre de la relacion
	file.setFileName("prueba")			# EN: output file name (.arff appended)	 / ES: nombre del archivo

	# EN: ------ values of the classification attribute ------
	# ES: ------ valores del atributo de clasificacion ------
	# file.setClass( [valor1, valor2, valor3, ....])
	file.setClass(["Coronis", "Eos", "Temis", "Flora", "Maria"])

	# EN: ------ possible values of each attribute ------
	# ES: ------ valores a tomar de cada atributo ------
	# file.setAttribute( atributo, [valor1, valor2, valor3, ....])
	file.setAttribute("tiporoca", ["arcilla", "niquel", "hierro", "desconocido"])
	file.setAttribute("diametro", [ 1, 2, 3, 4, 5] )
	file.setAttribute("masa", [2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3])
	file.setAttribute("forma", ["dentada", "irregular"])
	file.setAttribute("riezgoimpacto", ["bajo", "medio", "alto"])

	# EN: write the .arff file with random data from the given attributes/values
	# ES: genera el archivo .arff con datos random a partir de los atributos y valores dados
	file.randomize()
