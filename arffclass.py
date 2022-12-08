"""
arffGenerator — build a Weka .arff dataset file filled with random data.
arffGenerator — genera un archivo de dataset .arff de Weka con datos aleatorios.

EN: Define a relation name, a set of attributes (each with its list of
    possible values) and the class values, then call randomize() to write
    the .arff file with randomly picked rows.
ES: Define el nombre de la relación, un conjunto de atributos (cada uno con
    su lista de valores posibles) y los valores de clase; luego llama a
    randomize() para escribir el archivo .arff con filas elegidas al azar.
"""

import random, os


class arffGenerator():
	"""Generator of Weka .arff files with randomized data."""

	def __init__(self):
		"""Initialize the generator with default values"""
		self.__datas = 5 					# EN: number of data rows to generate 	/ ES: cantidad de filas a generar
		self.__relation = "relacionName"	# EN: relation name 					/ ES: nombre de la relacion
		self.__fileName = "example.arff"	 # EN: output .arff file name 			  / ES: nombre del archivo .arff de salida
		self.__attributes = []				# EN: attributes and their values 		/ ES: atributos y sus valores
		self.__class = []					# EN: classification attribute values 	 / ES: valores del atributo de clasificacion

	def __searchAtribute(self, atribute):
		""" Return the index of an attribute by name; raise if not found."""
		for i in range(len(self.__attributes)):
			if self.__attributes[i] == atribute:
				return i
		raise Exception("This atributte doesn't exist")


	def randomize(self):
		"""
		EN: Generate the .arff file: writes the @relation header, the
		    @attribute declarations and @datas rows of random values.
		    Overwrites the file if it already exists.
		
		ES: Genera el archivo .arff: escribe la cabecera @relation, las
		    declaraciones @attribute y @datas filas de valores aleatorios.
		    Sobrescribe el archivo si ya existe.
		"""
		self.setAttribute("class", self.__class)

		# EN: export into ./output (created if missing) 
		# ES: exporta en ./output (se crea si no existe)
		outDir = "output"
		os.makedirs(outDir, exist_ok=True)
		outPath = os.path.join(outDir, self.__fileName)

		if os.path.exists(outPath):
			os.remove(outPath)

		try:
			with open (file=outPath, mode="w+") as file:
				# EN: @relation header / ES: cabecera @relation
				file.write(f"@relation {self.__relation}\n\n")

				# EN: one @attribute line per attribute, values inside { } 
				# ES: una línea @attribute por atributo, valores entre { }
				for i in range(len(self.__attributes)):
					file.write(f"@attribute {self.__attributes[i][0]} " + "{")
					for j in range(len(self.__attributes[i][1])):
						file.write(f"{str(self.__attributes[i][1][j])}, ")
					file.seek(file.tell()-2)
					file.write("}\n")

				# EN: @data section, one random row per iteration
				# ES: sección @data, una fila aleatoria por iteración
				file.write(f"\n@data\n")
				for z in range(self.__datas):
					for i in range(len(self.__attributes)):
						rand = random.randint(0, len(self.__attributes[i][1])-1)
						value = self.__attributes[i][1][rand]
						# EN: quote numbers so Weka treats them as nominal
						# ES: entrecomilla números para que Weka los trate como nominales
						if type(value) == int or type(value) == float:
							value = "'" + str(value) + "'"

						file.write(f"{value}, ")
					file.seek(file.tell()-2)
					file.write("\n")
		except IOError as error:
			print('Se ha producido el error: %s' %(error))


	# getters
	def getDatas(self):
		"""Return the configured row count."""
		self.__datas
	def getRelation(self):
		"""Return the relation name."""
		self.__relation
	def getFileName(self):
		"""Return the output file name."""
		self.__fileName
	def getClass(self):
		"""Return the attributes list."""
		self.__attributes
	def getAttribute(self):
		"""Return the class values."""
		self.__class

	# setters
	def setDatas(self, value):
		"""Set the number of data rows to generate."""
		self.__validateDatas(value)
		self.__datas = value

	def setRelation(self, value):
		"""Set the relation name (@relation)."""
		self.__validateRelation(value)
		self.__relation = value

	def setFileName(self, value):
		"""Set the output file name; ".arff" is appended automatically."""
		self.__validateFileName(value)
		self.__fileName = value +".arff"

	def setClass(self, values):
		"""
		Set the possible values of the class (classification) attribute.

			>> file.setClass( [valor1, valor2, valor3, ....] )
		"""
		self.__validateClass(values)
		self.__class = values

	def setAttribute(self, atributte, values=[]):
		"""
		Add an attribute and its list of possible values.

			>> file.setAttribute( atributo, [valor1, valor2, valor3, ....] )
		"""
		self.__validateAttribute(atributte, values)
		self.__attributes += [[atributte, values]]


	# validaciones / validations
	def __validateDatas(self, value):
		"""Require an int"""
		if type(value) != int:
			raise Exception("The Datas value must be a integer")

	def __validateRelation(self, value):
		"""Require a str"""
		if type(value) != str:
			raise Exception("The Relation value must be a string")

	def __validateFileName(self, value):
		"""Require a str"""
		if type(value) != str:
			raise Exception("The File name value must be a string")

	def __validateClass(self, values):
		"""EN: Validate class values as an attribute named "class". / ES: Valida los valores de clase como un atributo llamado "class"."""
		self.__validateAttribute("class", values)

	def __validateAttribute(self, atribute, values):
		"""Require attribute name to be a str and values to be a list"""
		if type(atribute) != str:
			raise Exception("The atribute value must be a string")
		elif type(values) != list:
			raise Exception("The datas value must be a list")
