import ply.lex as lex 
import re

tokens = (
    "CONDICAO",
    "CICLO",
    "COMENTARIO",
    "COMENTARIO_AUMENTADO",
    "PROGRAM",
    "FUNC",
    "TYPE",
    "SIZE",
    "NUM",
    "VARIAVEL",
    "OPERADOR",
    "FIMSTRING",
    "INTERVALO",
    "CHAVETAS_BEG", 
    "CHAVETAS_END",
    "PARENTISIS_BEG",
    "PARENTISIS_END"
)

t_CONDICAO = r"if|else|in\s"
t_CICLO = r"while|for"
t_COMENTARIO = r"\/\/.*"
t_COMENTARIO_AUMENTADO = r"\/\*(.|\n)*\*\/"

def t_PROGRAM(t):
    r"program\s(\w+)"
    result = re.match(r"program\s(\w+)", t.value)
    t.value = result.group(1)
    return t

t_FUNC = r"(function\s)?\w+(?=\()"
t_TYPE = r"int"
t_SIZE = r"\[\w+\]"
t_NUM = r"\d+"
t_VARIAVEL = r"\w+"
t_OPERADOR = "\+|-|\*|%|=|<|>|\,"
t_FIMSTRING = r";"
t_INTERVALO = r"\[\d+\.\.\d+\]"
t_CHAVETAS_BEG = r"{"
t_CHAVETAS_END = r"}"
t_PARENTISIS_BEG = r"\("
t_PARENTISIS_END = r"\)"

def t_whitespace(t):
    r"\s+"
    pass

def t_error(t):
    print(f"Inválido: '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()
f = open("max.p", "r")
texto = ""
for linha in f.readlines(): texto += linha

lexer.input(texto)
for token in lexer:
    print(token)

