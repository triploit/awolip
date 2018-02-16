class Parser:
	def __init__(self, tokens):
		self.tokens = tokens
		self.AST = []

	def build_AST(self):
		tmp = []

		for token in self.tokens:
			if token["type"] == "semicolon":
				self.AST.append(tmp)
				tmp = []
			else:
				tmp.append(token)
