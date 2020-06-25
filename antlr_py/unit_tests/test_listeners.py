from io import StringIO

from antlr4 import *
from pytest import fixture, mark

from antlr_py.ChatLexer import ChatLexer
from antlr_py.ChatParser import ChatParser
from antlr_py.listeners import HtmlChatListener, ChatErrorListener


@fixture
def output():
    return StringIO()


@fixture
def error():
    return StringIO()


@fixture
def error_listener(error):
    return ChatErrorListener(error)


@fixture
def listener(output):
    return HtmlChatListener(output)


@fixture
def walker():
    return ParseTreeWalker()


@fixture
def parser(request, error, error_listener):
    lexer = ChatLexer(InputStream(request.param))
    parser = ChatParser(CommonTokenStream(lexer))

    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    return parser


class TestChatParser:
    @staticmethod
    @mark.parametrize('parser', ['John '], indirect=True)
    def test_valid_name(listener, parser, error_listener, walker):
        walker.walk(listener, parser.name())
        assert not error_listener.symbol

    @staticmethod
    @mark.parametrize('parser', ['Joh-'], indirect=True)
    def test_invalid_name(listener, parser, error_listener, walker):
        walker.walk(listener, parser.name())
        assert error_listener.symbol == '-'
