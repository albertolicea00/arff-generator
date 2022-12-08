import random



datas = 10000000					# cantidad de datos que genera
relacion = "meteoritos"				# nombre de la relacion y del archivo



# valores a tomar de cada atributo 	[atributo, [valor1, valor2, ....]]
attributes = [
	["tiporoca", 		["arcilla", "niquel", "hierro", "desconocido"]	],
	["diametro", 		[ 1, 2, 3, 4, 5] 								],
	["masa", 	 		[2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3] 			],
	["forma", 			["dentada", "irregular"] 						],
	["riezgoimpacto",	["bajo", "medio", "alto"] 						],
	["class", 			["Coronis", "Eos", "Temis", "Flora", "Maria"]	]
]

[
	['tiporoca', ['arcilla', 'niquel', 'hierro', 'desconocido']], 
	['diametro', [1, 2, 3, 4, 5]], 
	['masa', [2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3]], 
	['forma', ['dentada', 'irregular']], 
	['riezgoimpacto', ['bajo', 'medio', 'alto']], 
	['class', ['Coronis', 'Eos', 'Temis', 'Flora', 'Maria']]
]





with open (file=relacion+".arff" , mode="w+") as file:
	file.write(f"@relation {relacion}\n\n")
	
	for i in range(len(attributes)):
		file.write(f"@attribute {attributes[i][0]} " + "{")
		for j in range(len(attributes[i][1])):
			file.write(f"{str(attributes[i][1][j])}, ")
		file.seek(file.tell()-2)
		file.write("}\n")	

	file.write(f"\n@data\n")
	for z in range(datas):
		for i in range(len(attributes)):
			rand = random.randint(0, len(attributes[i][1])-1)
			value = attributes[i][1][rand]
			if type(value) == int or type(value) == float:
				value = "'" + str(value) + "'"
			
			file.write(f"{value}, ")
		file.seek(file.tell()-2)
		file.write("\n")

