from typing import IO

from antlr4.error.ErrorListener import ErrorListener

from antlr_py.ChatParser import ChatParser
from antlr_py.ChatListener import ChatListener


class HtmlChatListener(ChatListener):
    def __init__(self, output: IO):
        self.output = output
        self.output.write('<html><head><meta charset="UTF-8"/></head><body>')

    def enterName(self, ctx: ChatParser.NameContext):
        self.output.write("<strong>")

    def exitName(self, ctx: ChatParser.NameContext):
        self.output.write(ctx.WORD().getText())
        self.output.write("</strong> ")

    def enterColor(self, ctx: ChatParser.ColorContext):
        color = ctx.WORD().getText()
        ctx.text = f'<span style="color: {color}">'

    def exitColor(self, ctx: ChatParser.ColorContext):
        ctx.text += ctx.message().text
        ctx.text += '</span>'

    def exitEmoticon(self, ctx: ChatParser.EmoticonContext):
        emoticon = ctx.getText()

        if emoticon == ':-)' or emoticon == ':)':
            ctx.text = "🙂"

        if emoticon == ':-(' or emoticon == ':(':
            ctx.text = "🙁"

    def enterLink(self, ctx: ChatParser.LinkContext):
        text = ctx.TEXT()
        ctx.text = f'<a href="{text[1]}">{text[0]}</a>'

    def exitMessage(self, ctx: ChatParser.MessageContext):
        text = ''

        for child in ctx.children:
            text += getattr(child, 'text', child.getText())

        if isinstance(ctx.parentCtx, ChatParser.LineContext) is False:
            ctx.text = text
        else:
            self.output.write(text)
            self.output.write("</p>")

    def enterCommand(self, ctx: ChatParser.CommandContext):
        if ctx.SAYS() is not None:
            self.output.write(ctx.SAYS().getText() + ':' + '<p>')

        if ctx.SHOUTS() is not None:
            self.output.write(
                ctx.SHOUTS().getText() + ':' + '<p style="text-transform: uppercase">')

    def exitChat(self, ctx: ChatParser.ChatContext):
        self.output.write("</body></html>")


class ChatErrorListener(ErrorListener):

    def __init__(self, output):
        self.output = output
        self._symbol = ''

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        self.output.write(msg)
        self._symbol = offending_symbol.text

    @property
    def symbol(self):
        return self._symbol
