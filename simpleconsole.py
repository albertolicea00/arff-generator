"""
EN: Standalone script version (no class). Same logic as arffGenerator.randomize()
    but configured via plain variables at the top — edit them, then run.
ES: Versión script standalone (sin clase). Misma lógica que arffGenerator.randomize()
    pero configurada con variables al inicio — edítalas y ejecuta.
"""

import random



datas = 10000000					# EN: number of data rows to generate 	/ ES: cantidad de datos que genera
relacion = "meteoritos"				# EN: relation name (also the file name) / ES: nombre de la relacion y del archivo



# EN: possible values of each attribute	[name, [value1, value2, ....]]
# ES: valores a tomar de cada atributo 	[atributo, [valor1, valor2, ....]]
attributes = [
	["tiporoca", 		["arcilla", "niquel", "hierro", "desconocido"]	],
	["diametro", 		[ 1, 2, 3, 4, 5] 								],
	["masa", 	 		[2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3] 			],
	["forma", 			["dentada", "irregular"] 						],
	["riezgoimpacto",	["bajo", "medio", "alto"] 						],
	["class", 			["Coronis", "Eos", "Temis", "Flora", "Maria"]	]
]



# EN: write the .arff file: header, @attribute declarations, then @data rows
# ES: genera el archivo .arff: cabecera, declaraciones @attribute y filas @data
with open (file=relacion+".arff" , mode="w+") as file:
	# EN: @relation header 
	# ES: cabecera @relation
	file.write(f"@relation {relacion}\n\n")

	# EN: one @attribute line per attribute, values inside { } 
	# ES: una línea @attribute por atributo, valores entre { }
	for i in range(len(attributes)):
		file.write(f"@attribute {attributes[i][0]} " + "{")
		for j in range(len(attributes[i][1])):
			file.write(f"{str(attributes[i][1][j])}, ")
		file.seek(file.tell()-2)
		file.write("}\n")

	# EN: @data section, one random row per iteration 
	# ES: sección @data, una fila aleatoria por iteración
	file.write(f"\n@data\n")
	for z in range(datas):
		for i in range(len(attributes)):
			rand = random.randint(0, len(attributes[i][1])-1)
			value = attributes[i][1][rand]
			# EN: quote numbers so Weka treats them as nominal 
			# ES: entrecomilla números para que Weka los trate como nominales
			if type(value) == int or type(value) == float:
				value = "'" + str(value) + "'"

			file.write(f"{value}, ")
		file.seek(file.tell()-2)
		file.write("\n")

