#!/bin/python3

from lexer import Lexer
from parser import Parser
from executor import Executor
import sys

def main():
	if sys.argv[1][0] == "-":
		if sys.argv[1] == "--help" or sys.argv[1] == "-h" or sys.argv[1] == "-help":
			print("""usage: ./awolip [source file]
options:
	-v,--version		- shows the current version of the interpreter
	-h,-help,--help		- shows this

You have an idea for this project and don't know where to say it?
Here is our slack: https://bit.ly/2o3FWzv""")

		elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
			print("v0.0.1")
	else:
		fname = sys.argv[1]
		file = open(fname, "r")
		Executor().programm(file)

if __name__ == "__main__":
	main()
