import sys
from antlr4 import *
from YARSpgLexer import YARSpgLexer
from YARSpgParser import YARSpgParser



def main(argv):
    input = FileStream(argv[1])
    lexer = YARSpgLexer(input)
    stream = CommonTokenStream(lexer)
    parser = YARSpgParser(stream)
    tree = parser.yarspg()


if __name__ == '__main__':
    main(sys.argv)
