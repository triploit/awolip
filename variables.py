import re
import sys
from lexer import Lexer
from parser import Parser

class VariableContainer:
	def __init__(self, name = None, parent = None, variable_code = None):
		if name is None or parent is None or variable_code is None:
			self.variables = []
			self.name = "MAIN"
			self.parent = "<NONE>"
			self.scopes = []
		else:
			vars = self.get_variables_in_code(variable_code)
			self.variables = vars.variables
			self.name = name
			self.parent = parent
			self.scopes = vars.scopes

	def get_variables_in_code(self, code):
		SCOPE = ""
		vars = VariableContainer()

		file = re.sub(r"[;]", " ; ", "".join(code))
		file = re.sub(r"\\\"", "<AF!!!456:23>", file)
		file = re.sub(r"\\\(", "<MKLAO!!!456:23>", file)
		file = re.sub(r"\\\)", "<MKLAC!!!456:23>", file)

		lexer = Lexer(file)
		lexer.tokenize()
		parser = Parser(lexer.tokens)
		parser.build_AST()

		for c in parser.AST:
			if c[0]["value"] == "new":
				if len(c) != 3:
					print("fatal error: new: needs 2 arguments. given: "+str(len(c)-1))
					print("line: "+str(c[0]["line"]))
					sys.exit(1)
				else:
					if c[1]["type"] != "word":
						print("fatal error: new: incorrect name: "+c[1]["value"])
						print("line: "+str(c[0]["line"]))
						sys.exit(1)
					else:
						for v in Variables.variables:
							if v["name"] == c[1]["value"]:
								print("fatal error: new: variable already exists: "+v["name"])
								print("line: "+str(c[0]["line"]))
								sys.exit(1)

						name = c[1]["value"]
						value = c[2]["value"]
						_type = c[2]["type"]

						vars.variables.append({"name":name,"value":value,"type":_type})

			elif c[0]["value"] == "scope":
				if len(c) != 3:
					print("fatal error: scope: needs 2 arguments. given: "+str(len(c)-1))
					print("line: "+str(c[0]["line"]))
					sys.exit(1)
				else:
					if c[1]["type"] != "word":
						print("fatal error: scope: incorrect name: "+c[1]["value"])
						print("line: "+str(c[0]["line"]))
						sys.exit(1)
					else:
						for v in Variables.scopes:
							if v["name"] == c[1]["value"]:
								print("fatal error: scope: variable already exists: "+v["name"])
								print("line: "+str(c[0]["line"]))
								sys.exit(1)

						name = c[1]["value"]
						value = c[2]["value"]

						vars.scopes.append(VariableContainer(name, SCOPE, value))
		return vars

Variables = VariableContainer()
