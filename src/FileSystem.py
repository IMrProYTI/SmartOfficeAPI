import json
import os

class FileSystem():
	def __init__(self):
		self.__increment = -1
		try:
			os.mkdir('questionnaires')
		except:
			pass

	def getIncrement(self):
		self.__increment += 1
		return self.__increment

	def writeFileSync(self, data: dict):
		with open(f'questionnaires/ID_{self.getIncrement()}.json', 'w') as f:
			json.dump(data, f)
