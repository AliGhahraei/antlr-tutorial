import sys

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from antlr_py.ChatLexer import ChatLexer
from antlr_py.ChatParser import ChatParser
from antlr_py.HtmlChatListener import HtmlChatListener


def main(argv):
    input_ = FileStream(argv[1])
    lexer = ChatLexer(input_)
    parser = ChatParser(CommonTokenStream(lexer))
    tree = parser.chat()

    with open("output.html", "w") as output:
        chat_listener = HtmlChatListener(output)
        walker = ParseTreeWalker()
        walker.walk(chat_listener, tree)


if __name__ == '__main__':
    main(sys.argv)
