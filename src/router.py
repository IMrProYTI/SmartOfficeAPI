from src.FileSystem import FileSystem

def router(application):
	fs = FileSystem()

	@application.put('/')
	async def put_root(full_name: str, company: str, phone_number: str, email: str):
		fs.writeFileSync({
			'full_name': full_name,
			'company': company,
			'phone_number': phone_number,
			'email': email
		})
		return { 'status': 'OK' }