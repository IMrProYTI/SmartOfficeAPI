from pydantic import BaseModel
from hashlib import sha512
import json
import os


class Login(BaseModel):
	login: str
	password: str

class Registration(BaseModel):
	fullName: str
	company: str
	phone: str
	email: str
	password: str
	gender: str

class Questionnaire(BaseModel):
	fullName: str
	company: str
	phone: str
	email: str


class FileSystem():
	def __init__(self):
		self.__increment = -1
		try:
			os.mkdir('data')
			os.mkdir('data/accounts')
			os.mkdir('data/questionnaires')
		except:
			pass

	def getIncrement(self):
		self.__increment += 1
		return self.__increment

	def writeQuestionnaireSync(self, data: Questionnaire):
		with open(f'data/questionnaires/{data.email}.json', 'w') as f:
			f.writelines(json.dumps({
				"fullName": data.fullName,
				"company": data.company,
				"phone": data.phone,
				"email": data.email
			}))

	def writeAccountSync(self, data: Registration):
		with open(f'data/accounts/{data.email}.json', 'w') as f:
			f.writelines(json.dumps({
				"fullName": data.fullName,
				"company": data.company,
				"phone": data.phone,
				"email": data.email,
				"password": sha512(bytes(data.password, encoding='utf8')).hexdigest(),
				"gender": data.gender
			}))

	def readAccountSync(self, login: str):
		try:
			with open(f'data/accounts/{login}.json') as f:
				return json.loads(*f.readlines())
		except:
			return {}
