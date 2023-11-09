from src.FileSystem import Login, Registration, Questionnaire, FileSystem
from pydantic import BaseModel
from hashlib import sha512

class Status(BaseModel):
	status: bool

def router(application):
	fs = FileSystem()
	
	@application.post('/login')
	async def post_login(user: Login) -> Status:
		userData = fs.readAccountSync(user.login)
		if (userData == {}):
			return { 'status': False }
		else:
			tempPassword = sha512(bytes(user.password, encoding='utf8')).hexdigest()
			return { 'status': userData['password'] == tempPassword }

	@application.post('/registration')
	async def post_registration(user: Registration) -> Login:
		fs.writeAccountSync(user)
		return {
			"login": user.email,
			"password": user.password
		}

	@application.post('/questionnaire')
	async def put_questionnaire(questionnaire: Questionnaire) -> Status:
		fs.writeQuestionnaireSync(questionnaire)
		return { 'status': True }