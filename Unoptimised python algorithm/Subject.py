from Default import Default

class Subject(Default):
	def __init__(self, subject: str, amount: int):
		self.subject = subject
		self.amount = amount
		Default.__init__(self)