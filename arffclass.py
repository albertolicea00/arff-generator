import random, os


class arffGenerator():

	def __init__(self):
		self.__datas = 5 					# cantidad de datos que genera
		self.__relation = "relacionName"	# nombre de la relacion 
		self.__fileName = "example.arff"	# nombre del archivo.arff
		self.__attributes = []				# atributos y sus correspondientes valores
		self.__class = []					# valores del atributo clasificacion

	def __searchAtribute(self, atribute):
		for i in range(len(self.__attributes)):
			if self.__attributes[i] == atribute:
				return i
		raise Exception("This atributte doesn't exist")


	def randomize(self):
		self.setAttribute("class", self.__class)

		if os.path.exists(self.__fileName):
			os.remove(self.__fileName)

		try:
			with open (file=self.__fileName, mode="w+") as file:
				file.write(f"@relation {self.__relation}\n\n")
				
				for i in range(len(self.__attributes)):
					file.write(f"@attribute {self.__attributes[i][0]} " + "{")
					for j in range(len(self.__attributes[i][1])):
						file.write(f"{str(self.__attributes[i][1][j])}, ")
					file.seek(file.tell()-2)
					file.write("}\n")	

				file.write(f"\n@data\n")
				for z in range(self.__datas):
					for i in range(len(self.__attributes)):
						rand = random.randint(0, len(self.__attributes[i][1])-1)
						value = self.__attributes[i][1][rand]
						if type(value) == int or type(value) == float:
							value = "'" + str(value) + "'"
						
						file.write(f"{value}, ")
					file.seek(file.tell()-2)
					file.write("\n")
		except IOError as error:
			print('Se ha producido el error: %s' %(error))


	# getters
	def getDatas():
		self.__datas
	def getRelation():
		self.__relation
	def getFileName():
		self.__fileName
	def getClass():
		self.__attributes
	def getAttribute():
		self.__class

	# setters
	def setDatas (self, value):
		self.__validateDatas(value)
		self.__datas = value

	def setRelation (self, value):
		self.__validateRelation(value)
		self.__relation = value

	def setFileName (self, value):
		self.__validateFileName(value)
		self.__fileName = value +".arff"

	def setClass (self, values):
		"""
			>> file.setClass( [valor1, valor2, valor3, ....] )	
		"""
		self.__validateClass(values)
		self.__class = values

	def setAttribute(self, atributte, values=[]):
		"""
			>> file.setAttribute( atributo, [valor1, valor2, valor3, ....] )	
		"""
		self.__validateAttribute(atributte, values)
		self.__attributes += [[atributte, values]]


	# validaciones
	def __validateDatas(self, value):
		if type(value) != int:
			raise Exception("The Datas value must be a integer")

	def __validateRelation(self, value):
		if type(value) != str:
			raise Exception("The Relation value must be a string")

	def __validateFileName(self, value):
		if type(value) != str:
			raise Exception("The File name value must be a string")

	def __validateClass(self, values):
		self.__validateAttribute("class", values)

	def __validateAttribute(self, atribute, values):
		if type(atribute) != str:
			raise Exception("The atribute value must be a string")
		elif type(values) != list:
			raise Exception("The datas value must be a list")