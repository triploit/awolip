from lexer import Lexer
from parser import Parser
from executor import Executor
import sys

def main():
	fname = sys.argv[1]
	file = open(fname, "r")

	Executor().programm(file)

if __name__ == "__main__":
	main()
