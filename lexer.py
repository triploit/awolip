import re

class Lexer:
	def typeOf(self, string):
		if re.match("([0-9]*(\.[0-9]+)|[0-9]+)", "".join(tmp)):
			return "int"

		elif "".join(tmp) in self.keywords:
			self.tokens.append({"type":"keyword", "value": "".join(tmp), "line": linen})

		elif re.match("(([a-zA-Z_]+[0-9a-zA-Z_]*)+)(\.(([a-zA-Z_]+[0-9a-zA-Z_]*)+))+", "".join(tmp)):
			self.tokens.append({"type": "dict", "value": "".join(tmp), "line": linen})

		elif re.match("([a-zA-Z_]+[0-9a-zA-Z_]*)+", "".join(tmp)):
			self.tokens.append({"type": "word", "value": "".join(tmp), "line": linen})

		elif "".join(tmp) == ";":
			self.tokens.append({"type":"semicolon", "value": ";"})

		elif "".join(tmp) in self.operators and tid == "":
			self.tokens.append({"type":"operator", "value": "".join(tmp), "line": linen})

		else:
			if tmp != []:
				self.tokens.append({"type":"unknown", "value": "".join(tmp), "line": linen})


	def __init__(self, data=""):
		self.data = data;
		self.tokens = []
		self.keywords = [
			"new",
			"println",
			"print",
			"set",
			"run",
			"return",
			"if",
			"scope",
			"input",
			"typeof"
		]

		self.operators = [
			"==",
			"!=",
			"<=",
			">=",
			"<",
			">",
			"==="
		]

	def tokenize(self):
		code = self.data
		tmp = []
		tid = ""
		linen = 1

		cm = 0
		cb = 0

		for l in code:
			if l == "\n":
				linen += 1

			if l == "\"" and tid == "":
				tid = "string"
				tmp = []

			elif l == "\"" and tid == "string":
				self.tokens.append({"type": tid, "value": "".join(tmp), "line": linen})
				tid = ""
				tmp = []

			elif l == "(" and (tid == "" or tid == "math"):
				tmp.append("(")
				cm += 1

				if tid == "math":
					continue

				tid = "math"
				tmp = []

			elif l == ")" and tid == "math":
				if cm > 1:
					tmp.append(")")
					cm -= 1
					continue

				cm = 0
				self.tokens.append({"type": tid, "value": "".join(tmp), "line": linen})
				tid = ""
				tmp = []

			elif l == "{" and (tid == "" or tid == "code"):
				tmp.append("{")
				cb += 1

				if tid == "code":
					continue

				tid = "code"
				tmp = []

			elif l == "}" and tid == "code":
				if cb > 1:
					tmp.append("}")
					cb -= 1
					continue

				cb = 0
				self.tokens.append({"type": tid, "value": "".join(tmp), "line": linen})
				tid = ""
				tmp = []

			elif l == ";" and (tid == ""):
				if re.match("([0-9]*(\.[0-9]+)|[0-9]+)", "".join(tmp)):
					self.tokens.append({"type": "int", "value": float("".join(tmp)), "line": linen})

				elif re.match("(([a-zA-Z_]+[0-9a-zA-Z_]*)+)(\.(([a-zA-Z_]+[0-9a-zA-Z_]*)+))+", "".join(tmp)):
					self.tokens.append({"type": "dict", "value": "".join(tmp), "line": linen})

				elif "".join(tmp) in self.keywords:
					self.tokens.append({"type":"keyword", "value": "".join(tmp), "line": linen})

				elif re.match("typeof<([a-zA-Z_]+[0-9a-zA-Z_]*)+>", "".join(tmp)):
					self.tokens.append({"type": "typeof", "value": "".join(tmp), "line": linen})

				elif re.match("([a-zA-Z_]+[0-9a-zA-Z_]*)+", "".join(tmp)):
					self.tokens.append({"type": "word", "value": "".join(tmp), "line": linen})

				elif "".join(tmp) in self.operators and tid == "":
					self.tokens.append({"type":"operator", "value": "".join(tmp), "line": linen})

				else:
					if tmp != []:
						self.tokens.append({"type":"unknown", "value": "".join(tmp), "line": linen})

				self.tokens.append({"type":"semicolon", "value": ";"})
				tmp = []
				continue

			elif (l == " " or l == "\t" or l == "\n") and (tid == ""):
				if re.match("([0-9]*(\.[0-9]+)|[0-9]+)", "".join(tmp)):
					self.tokens.append({"type": "int", "value": float("".join(tmp)), "line": linen})

				elif re.match("typeof<([a-zA-Z_]+[0-9a-zA-Z_]*)+>", "".join(tmp)):
					self.tokens.append({"type": "typeof", "value": "".join(tmp), "line": linen})

				elif "".join(tmp) in self.keywords:
					self.tokens.append({"type":"keyword", "value": "".join(tmp), "line": linen})

				elif re.match("(([a-zA-Z_]+[0-9a-zA-Z_]*)+)(\.(([a-zA-Z_]+[0-9a-zA-Z_]*)+))+", "".join(tmp)):
					self.tokens.append({"type": "dict", "value": "".join(tmp), "line": linen})

				elif re.match("([a-zA-Z_]+[0-9a-zA-Z_]*)+", "".join(tmp)):
					self.tokens.append({"type": "word", "value": "".join(tmp), "line": linen})

				elif "".join(tmp) == ";":
					self.tokens.append({"type":"semicolon", "value": ";"})

				elif "".join(tmp) in self.operators and tid == "":
					self.tokens.append({"type":"operator", "value": "".join(tmp), "line": linen})

				else:
					if tmp != []:
						self.tokens.append({"type":"unknown", "value": "".join(tmp), "line": linen})

				tmp = []
				continue
			else:
				tmp.append(l)
