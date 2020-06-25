# Generated from Chat.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\6\4\'\n")
        buf.write("\4\r\4\16\4(\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\5\7\64")
        buf.write("\n\7\3\7\3\7\3\7\5\79\n\7\3\7\5\7<\n\7\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n")
        buf.write("\f\16\20\22\2\3\3\2\t\n\2J\2\25\3\2\2\2\4\33\3\2\2\2\6")
        buf.write("&\3\2\2\2\b*\3\2\2\2\n-\3\2\2\2\f;\3\2\2\2\16=\3\2\2\2")
        buf.write("\20@\3\2\2\2\22F\3\2\2\2\24\26\5\4\3\2\25\24\3\2\2\2\26")
        buf.write("\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2")
        buf.write("\31\32\7\2\2\3\32\3\3\2\2\2\33\34\5\b\5\2\34\35\5\n\6")
        buf.write("\2\35\36\5\6\4\2\36\37\7\r\2\2\37\5\3\2\2\2 \'\5\f\7\2")
        buf.write("!\'\5\16\b\2\"\'\5\20\t\2#\'\5\22\n\2$\'\7\13\2\2%\'\7")
        buf.write("\f\2\2& \3\2\2\2&!\3\2\2\2&\"\3\2\2\2&#\3\2\2\2&$\3\2")
        buf.write("\2\2&%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)\7\3\2\2")
        buf.write("\2*+\7\13\2\2+,\7\f\2\2,\t\3\2\2\2-.\t\2\2\2./\7\3\2\2")
        buf.write("/\60\7\f\2\2\60\13\3\2\2\2\61\63\7\3\2\2\62\64\7\4\2\2")
        buf.write("\63\62\3\2\2\2\63\64\3\2\2\2\64\65\3\2\2\2\65<\7\5\2\2")
        buf.write("\668\7\3\2\2\679\7\4\2\28\67\3\2\2\289\3\2\2\29:\3\2\2")
        buf.write("\2:<\7\6\2\2;\61\3\2\2\2;\66\3\2\2\2<\r\3\2\2\2=>\7\16")
        buf.write("\2\2>?\7\16\2\2?\17\3\2\2\2@A\7\7\2\2AB\7\13\2\2BC\7\7")
        buf.write("\2\2CD\5\6\4\2DE\7\7\2\2E\21\3\2\2\2FG\7\b\2\2GH\7\13")
        buf.write("\2\2H\23\3\2\2\2\b\27&(\638;")
        return buf.getvalue()


class ChatParser ( Parser ):

    grammarFileName = "Chat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'-'", "')'", "'('", "'/'", "'@'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SAYS", "SHOUTS", 
                      "WORD", "WHITESPACE", "NEWLINE", "TEXT" ]

    RULE_chat = 0
    RULE_line = 1
    RULE_message = 2
    RULE_name = 3
    RULE_command = 4
    RULE_emoticon = 5
    RULE_link = 6
    RULE_color = 7
    RULE_mention = 8

    ruleNames =  [ "chat", "line", "message", "name", "command", "emoticon", 
                   "link", "color", "mention" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    SAYS=7
    SHOUTS=8
    WORD=9
    WHITESPACE=10
    NEWLINE=11
    TEXT=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ChatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ChatParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.LineContext)
            else:
                return self.getTypedRuleContext(ChatParser.LineContext,i)


        def getRuleIndex(self):
            return ChatParser.RULE_chat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChat" ):
                listener.enterChat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChat" ):
                listener.exitChat(self)




    def chat(self):

        localctx = ChatParser.ChatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_chat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.line()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ChatParser.WORD):
                    break

            self.state = 23
            self.match(ChatParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(ChatParser.NameContext,0)


        def command(self):
            return self.getTypedRuleContext(ChatParser.CommandContext,0)


        def message(self):
            return self.getTypedRuleContext(ChatParser.MessageContext,0)


        def NEWLINE(self):
            return self.getToken(ChatParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ChatParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = ChatParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.name()
            self.state = 26
            self.command()
            self.state = 27
            self.message()
            self.state = 28
            self.match(ChatParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MessageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def emoticon(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.EmoticonContext)
            else:
                return self.getTypedRuleContext(ChatParser.EmoticonContext,i)


        def link(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.LinkContext)
            else:
                return self.getTypedRuleContext(ChatParser.LinkContext,i)


        def color(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.ColorContext)
            else:
                return self.getTypedRuleContext(ChatParser.ColorContext,i)


        def mention(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.MentionContext)
            else:
                return self.getTypedRuleContext(ChatParser.MentionContext,i)


        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.WORD)
            else:
                return self.getToken(ChatParser.WORD, i)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.WHITESPACE)
            else:
                return self.getToken(ChatParser.WHITESPACE, i)

        def getRuleIndex(self):
            return ChatParser.RULE_message

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMessage" ):
                listener.enterMessage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMessage" ):
                listener.exitMessage(self)




    def message(self):

        localctx = ChatParser.MessageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_message)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 36
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ChatParser.T__0]:
                        self.state = 30
                        self.emoticon()
                        pass
                    elif token in [ChatParser.TEXT]:
                        self.state = 31
                        self.link()
                        pass
                    elif token in [ChatParser.T__4]:
                        self.state = 32
                        self.color()
                        pass
                    elif token in [ChatParser.T__5]:
                        self.state = 33
                        self.mention()
                        pass
                    elif token in [ChatParser.WORD]:
                        self.state = 34
                        self.match(ChatParser.WORD)
                        pass
                    elif token in [ChatParser.WHITESPACE]:
                        self.state = 35
                        self.match(ChatParser.WHITESPACE)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 38 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(ChatParser.WORD, 0)

        def WHITESPACE(self):
            return self.getToken(ChatParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return ChatParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = ChatParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(ChatParser.WORD)
            self.state = 41
            self.match(ChatParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self):
            return self.getToken(ChatParser.WHITESPACE, 0)

        def SAYS(self):
            return self.getToken(ChatParser.SAYS, 0)

        def SHOUTS(self):
            return self.getToken(ChatParser.SHOUTS, 0)

        def getRuleIndex(self):
            return ChatParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = ChatParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not(_la==ChatParser.SAYS or _la==ChatParser.SHOUTS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 44
            self.match(ChatParser.T__0)
            self.state = 45
            self.match(ChatParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmoticonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ChatParser.RULE_emoticon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmoticon" ):
                listener.enterEmoticon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmoticon" ):
                listener.exitEmoticon(self)




    def emoticon(self):

        localctx = ChatParser.EmoticonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_emoticon)
        self._la = 0 # Token type
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(ChatParser.T__0)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ChatParser.T__1:
                    self.state = 48
                    self.match(ChatParser.T__1)


                self.state = 51
                self.match(ChatParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(ChatParser.T__0)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ChatParser.T__1:
                    self.state = 53
                    self.match(ChatParser.T__1)


                self.state = 56
                self.match(ChatParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.TEXT)
            else:
                return self.getToken(ChatParser.TEXT, i)

        def getRuleIndex(self):
            return ChatParser.RULE_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink" ):
                listener.enterLink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink" ):
                listener.exitLink(self)




    def link(self):

        localctx = ChatParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(ChatParser.TEXT)
            self.state = 60
            self.match(ChatParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(ChatParser.WORD, 0)

        def message(self):
            return self.getTypedRuleContext(ChatParser.MessageContext,0)


        def getRuleIndex(self):
            return ChatParser.RULE_color

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColor" ):
                listener.enterColor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColor" ):
                listener.exitColor(self)




    def color(self):

        localctx = ChatParser.ColorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_color)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(ChatParser.T__4)
            self.state = 63
            self.match(ChatParser.WORD)
            self.state = 64
            self.match(ChatParser.T__4)
            self.state = 65
            self.message()
            self.state = 66
            self.match(ChatParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MentionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(ChatParser.WORD, 0)

        def getRuleIndex(self):
            return ChatParser.RULE_mention

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMention" ):
                listener.enterMention(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMention" ):
                listener.exitMention(self)




    def mention(self):

        localctx = ChatParser.MentionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_mention)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ChatParser.T__5)
            self.state = 69
            self.match(ChatParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





