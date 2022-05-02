from json import *
from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.web import JsonLexer

def adaptResponse (response):
  json = dumps(response, indent=2, default=str)
  colorful = highlight(
    json,
    lexer=JsonLexer(),
    formatter=Terminal256Formatter(),
  )
  print(colorful)