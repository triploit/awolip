from variables import Variables
from variables import VariableContainer
from lexer import Lexer
from parser import Parser

import re
import sys

class Executor:
	def __init__(self):
		self.SCOPE = "MAIN"

	def run(self, command):
		RET = 0

		for c in command:
			if RET != 2:
				RET = self.execute(c)

	def programm(self, data):
		file = re.sub(r"[;]", " ; ", "".join(data))
		file = re.sub(r"\\\"", "<AF!!!456:23>", file)
		file = re.sub(r"\\\(", "<MKLAO!!!456:23>", file)
		file = re.sub(r"\\\)", "<MKLAC!!!456:23>", file)
		lexer = Lexer(file)

		lexer.tokenize()
		# print("")
		# print("TOKENS: "+str(lexer.tokens))
		parser = Parser(lexer.tokens)
		#print("")
		parser.build_AST()
		#print("AST: "+str(parser.AST))
		#print("")
		executor = Executor()
		executor.run(parser.AST)

	def get_variable_in_scope(self, name):
		tree = name.split(".")
		i = 0
		li = i
		vars = Variables

		for n in tree:
			for sc in vars.scopes:
				if sc.name == n:
					vars = sc

			for v in vars.variables:
				if v["name"] == n:
					return v

			li = i
			i += 1

		return {"type":"NONE","value":"NONE","line":"NONE"}

	def execute(self, c):
		if c == []: return 0

		for i in range(0, len(c)):
			if c[i]["type"] == "math":
				for v in Variables.variables:
					c[i]["value"] = str(c[i]["value"]).replace(v["name"], str(v["value"]))

				try:
					c[i] = {"type": "int",
							"value": eval(str(c[i]["value"])),
							"line":c[i]["line"]}
				except TypeError:
					print("fatal error: math-error: can't evaluate different types: "+str(c[i]["value"]))
					print("line: "+str(c[0]["line"]))
					sys.exit(1)
				except ZeroDivisionError:
					print("fatal error: math-error: division by zero: "+str(c[i]["value"]))
					print("line: "+str(c[0]["line"]))
					sys.exit(1)
				except ArithmeticError:
					print("fatal error: math-error: can't evaluate different types: "+str(c[i]["value"]))
					print("line: "+str(c[0]["line"]))
					sys.exit(1)
				except Exception:
					print("fatal error: math-error: unknown error in: "+str(c[i]["value"]))
					print("line: "+str(c[0]["line"]))
					sys.exit(1)

			elif c[i]["type"] == "dict":
				# print("EXEC: "+str(k))
				c[i] = self.get_variable_in_scope(c[i]["value"])

			elif c[i]["type"] == "typeof":
				c[i]["type"] = "word"
				name = c[i]["value"][7:-1]
				found = False

				for v in Variables.variables:
					if v["name"] == name:
						c[i]["value"] = v["type"]
						found = True
						break

				if found == False:
					print("fatal error: typeof<>: variable not found: "+name)
					print("line: "+str(c[0]["line"]))
					sys.exit(1)

		#print("EXEC: "+str(c))

		if c[0]["type"] == "keyword":
			if c[0]["value"] == "println":
				for i in c[1:]:
					if i["type"] == "word":
						t = False
						for v in Variables.variables:
							if v["name"] == i["value"]:
								v["value"] = re.sub(r"<AF!!!456:23>", "\"", str(v["value"]))
								v["value"] = re.sub(r"\\n", "\n", str(v["value"]))
								v["value"] = re.sub(r"<MKLAO!!!456:23>", "(", (v["value"]))
								v["value"] = re.sub(r"<MKLAC!!!456:23>", ")", (v["value"]))

								sys.stdout.write(""+str(v["value"]))
								sys.stdout.flush()
								t = True

						if t == False:
							i["value"] = re.sub(r"<AF!!!456:23>", "\"", str(i["value"]))
							i["value"] = re.sub(r"\\n", "\n", str(i["value"]))
							i["value"] = re.sub(r"<MKLAO!!!456:23>", "(", (i["value"]))
							i["value"] = re.sub(r"<MKLAC!!!456:23>", ")", (i["value"]))

							sys.stdout.write(str(i["value"]))
							sys.stdout.flush()
					else:
						i["value"] = re.sub(r"<AF!!!456:23>", "\"", str(i["value"]))
						i["value"] = re.sub(r"\\n", "\n", str(i["value"]))
						i["value"] = re.sub(r"<MKLAO!!!456:23>", "(", (i["value"]))
						i["value"] = re.sub(r"<MKLAC!!!456:23>", ")", (i["value"]))
						sys.stdout.write(str(i["value"]))
						sys.stdout.flush()

				print("")

			elif c[0]["value"] == "print":
				for i in c[1:]:
					if i["type"] == "word":
						t = False
						for v in Variables.variables:
							if v["name"] == i["value"]:
								v["value"] = re.sub(r"<AF!!!456:23>", "\"", str(v["value"]))
								v["value"] = re.sub(r"\\n", "\n", str(v["value"]))
								v["value"] = re.sub(r"<MKLAO!!!456:23>", "(", (v["value"]))
								v["value"] = re.sub(r"<MKLAC!!!456:23>", ")", (v["value"]))

								sys.stdout.write(""+str(v["value"]))
								sys.stdout.flush()
								t = True

						if t == False:
							i["value"] = re.sub(r"<AF!!!456:23>", "\"", str(i["value"]))
							i["value"] = re.sub(r"\\n", "\n", str(i["value"]))
							i["value"] = re.sub(r"<MKLAO!!!456:23>", "(", (i["value"]))
							i["value"] = re.sub(r"<MKLAC!!!456:23>", ")", (i["value"]))

							sys.stdout.write(str(i["value"]))
							sys.stdout.flush()
					else:
						i["value"] = re.sub(r"<AF!!!456:23>", "\"", str(i["value"]))
						i["value"] = re.sub(r"\\n", "\n", str(i["value"]))
						i["value"] = re.sub(r"<MKLAO!!!456:23>", "(", (i["value"]))
						i["value"] = re.sub(r"<MKLAC!!!456:23>", ")", (i["value"]))
						sys.stdout.write(str(i["value"]))
						sys.stdout.flush()

			elif c[0]["value"] == "return":
				return 2

			elif c[0]["value"] == "if":
				if len(c) != 5 and len(c) != 7:
					print("fatal error: if: needs 4 or 6 arguments. given: "+str(len(c)-1))
					print("line: "+str(c[0]["line"]))
					sys.exit(1)
				else:
					if c[2]["type"] != "operator":
						print("fatal error: if: argument 2 : incorrect type: "+c[2]["type"])
						print("                 expected   : operator")
						print("line: "+str(c[0]["line"]))
						sys.exit(1)

					if c[4]["type"] != "code":
						print("fatal error: if: argument 3 : incorrect type: "+c[4]["type"])
						print("                 expected   : code")
						print("line: "+str(c[0]["line"]))
						sys.exit(1)

					if len(c) == 7 and c[5]["value"] != "else":
						print("fatal error: if: argument 6 : incorrect type: "+c[5]["type"])
						print("                 expected   : else")
						print("line: "+str(c[0]["line"]))
						sys.exit(1)

					if len(c) == 7 and c[6]["type"] != "code":
						print("fatal error: if: argument 7 : incorrect type: "+c[6]["type"])
						print("                 expected   : code")
						print("line: "+str(c[0]["line"]))
						sys.exit(1)

					if c[2]["value"] == "==":
						if c[1]["value"] == c[3]["value"]:
							self.programm(c[4]["value"])
						else:
							if len(c) == 7:
								self.programm(c[6]["value"])
					elif c[2]["value"] == "!=":
						if c[1]["value"] != c[3]["value"]:
							self.programm(c[4]["value"])
						else:
							if len(c) == 7:
								self.programm(c[6]["value"])
					elif c[2]["value"] == "===":
						if c[1]["value"] == c[3]["value"] and c[1]["type"] == c[3]["type"]:
							self.programm(c[4]["value"])
						else:
							if len(c) == 7:
								self.programm(c[6]["value"])
					elif c[2]["value"] == "<=":
						if c[1]["value"] <= c[3]["value"]:
							self.programm(c[4]["value"])
						else:
							if len(c) == 7:
								self.programm(c[6]["value"])
					elif c[2]["value"] == ">=":
						if c[1]["value"] >= c[3]["value"]:
							self.programm(c[4]["value"])
						else:
							if len(c) == 7:
								self.programm(c[6]["value"])
					elif c[2]["value"] == ">":
						if c[1]["value"] > c[3]["value"]:
							self.programm(c[4]["value"])
						else:
							if len(c) == 7:
								programm(c[6]["value"])
					elif c[2]["value"] == "<":
						if c[1]["value"] < c[3]["value"]:
							self.programm(c[4]["value"])
						else:
							if len(c) == 7:
								self.programm(c[6]["value"])
				return 0

			elif c[0]["value"] == "set":
				if len(c) != 3:
					print("fatal error: set: needs 2 arguments. given: "+str(len(c)-1))
					print("line: "+str(c[0]["line"]))
					sys.exit(1)
				else:
					for i in range(0, len(Variables.variables)):
						if Variables.variables[i]["name"] == c[1]["value"]:
							Variables.variables[i]["value"] = c[2]["value"]
							return 0

					Variables.variables.append({"name":c[1]["value"], "value":c[2]["value"], "type":c[2]["type"]})


			elif c[0]["value"] == "new":
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

						Variables.variables.append({"name":name,"value":value,"type":_type})

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
						_type = c[2]["type"]

						Variables.scopes.append(VariableContainer(name, self.SCOPE, value))

			elif c[0]["value"] == "run":
				if len(c) != 2:
					print("fatal error: run: needs 1 argument. given: "+str(len(c)-1))
					print("line: "+str(c[0]["line"]))
					sys.exit(1)
				else:
					if c[1]["type"] == "code":
						self.programm(c[1]["value"])
					elif c[1]["type"] == "word":
						for v in Variables.variables:
							if v["name"] == c[1]["value"]:
								self.programm(v["value"])
								return 0
						print("fatal error: run: variable not found: "+c[1]["value"])
						print("line: "+str(c[0]["line"]))
						sys.exit(1)
					else:
						print("fatal error: run: wrong type: "+c[1]["value"])
						print("line: "+str(c[0]["line"]))
						sys.exit(1)

#			elif c[0]["value"] == "typeof":
#				if len(c) != 3:
#					print("fatal error: typeof: needs 2 arguments. given: "+str(len(c)-1))
#					print("line: "+str(c[0]["line"]))
#					sys.exit(1)
#				else:
#					if c[2]["type"] != "word":
#						print("fatal error: typeof: wrong type: "+c[1]["value"])
#						print("line: "+str(c[0]["line"]))
#						sys.exit(1)
#
#					for i in range(0, len(Variables.variables)):
#						if Variables.variables[i]["name"] == c[1]["value"]:
#
#					print("fatal error: typeof: variable not found: "+c[1]["value"])
#					print("line: "+str(c[0]["line"]))
#					sys.exit(1)


			elif c[0]["value"] == "input":
				if len(c) != 2:
					print("fatal error: input: needs 1 argument. given: "+str(len(c)-1))
					print("line: "+str(c[0]["line"]))
					sys.exit(1)
				else:
					if c[1]["type"] != "word":
						print("fatal error: input: wrong type: "+c[1]["value"])
						print("line: "+str(c[0]["line"]))
						sys.exit(1)
					else:
						for i in range(0, len(Variables.variables)):
							if Variables.variables[i]["name"] == c[1]["value"]:
								string = input();

								if re.match("([0-9]*(\.[0-9]+)|[0-9]+)", string):
									Variables.variables[i]["type"] = "int"
								else:
									Variables.variables[i]["type"] = "string"

								Variables.variables[i]["value"] = string
								return 0

						print("fatal error: input: variable not found: "+c[1]["value"])
						print("line: "+str(c[0]["line"]))
						sys.exit(1)
