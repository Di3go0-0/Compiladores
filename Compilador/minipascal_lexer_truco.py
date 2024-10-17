import ply.lex as lex
import sys

# Reserved words list
reserved = {
    'ABSOLUTE': 'ABSOLUTE',
    'AND': 'AND',
    'ARRAY': 'ARRAY',
    'ASM': 'ASM',
    'BEGIN': 'BEGIN',
    'CASE': 'CASE',
    'CONST': 'CONST',
    'CONSTRUCTOR': 'CONSTRUCTOR',
    'DESTRUCTOR': 'DESTRUCTOR',
    'EXTERNAL': 'EXTERNAL',
    'DIV': 'DIV',
    'DO': 'DO',
    'DOWNTO': 'DOWNTO',
    'ELSE': 'ELSE',
    'END': 'END',
    'FILE': 'FILE',
    'FOR': 'FOR',
    'FORWARD': 'FORWARD',
    'FUNCTION': 'FUNCTION',
    'GOTO': 'GOTO',
    'IF': 'IF',
    'IMPLEMENTATION': 'IMPLEMENTATION',
    'IN': 'IN',
    'INLINE': 'INLINE',
    'INTERFACE': 'INTERFACE',
    'INTERRUPT': 'INTERRUPT',
    'LABEL': 'LABEL',
    'MOD': 'MOD',
    'NIL': 'NIL',
    'NOT': 'NOT',
    'OBJECT': 'OBJECT',
    'OF': 'OF',
    'OR': 'OR',
    'PACKED': 'PACKED',
    'PRIVATE': 'PRIVATE',
    'PROCEDURE': 'PROCEDURE',
    'PROGRAM': 'PROGRAM',
    'RECORD': 'RECORD',
    'REPEAT': 'REPEAT',
    'SET': 'SET',
    'SHL': 'SHL',
    'SHR': 'SHR',
    'STRING': 'STRING',
    'THEN': 'THEN',
    'TO': 'TO',
    'TYPE': 'TYPE',
    'UNIT': 'UNIT',
    'UNTIL': 'UNTIL',
    'USES': 'USES',
    'VAR': 'VAR',
    'VIRTUAL': 'VIRTUAL',
    'WHILE': 'WHILE',
    'WITH': 'WITH',
    'XOR': 'XOR'
}

# Token list
tokens = [
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULUS',
    'EQUAL', 'LESS', 'GREATER', 'CIRCUMFLEX', 'EXCLAMATION',
    'COLON', 'SEMICOLON', 'COMMA', 'DOT', 'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET', 'LBLOCK', 'RBLOCK', 'AMPERSANT',
    'PIPE', 'HASHTAG', 'DIACRITIC', 'DOLLAR', 'SQUOTE',
    'DEQUAL', 'LESSEQUAL', 'GREATEREQUAL', 'LSHIFT', 'RSHIFT',
    'ASSIGN', 'ID', 'NUMBER', 'CONSTSTRING'
] + list(reserved.values())

# Regular expressions for symbols
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULUS = r'%'
t_EQUAL = r'='
t_LESS = r'<'
t_GREATER = r'>'
t_CIRCUMFLEX = r'\^'
t_EXCLAMATION = r'!'
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','
t_DOT = r'\.'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_AMPERSANT = r'&'
t_PIPE = r'\|'
t_HASHTAG = r'\#'
t_DIACRITIC = r'~'
t_DOLLAR = r'\$'
t_SQUOTE = r'\''

# Regular expressions for operators
t_DEQUAL = r'<>'
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_ASSIGN = r':='

# Constant string rule
def t_CONSTSTRING(t):
    r'(\".*?\")|(\'.*?\')'
    return t

# Number rule
def t_NUMBER(t):
    r'(-?)[0-9]+(\.[0-9]+)?((e|E)(-)?[0-9]+)?'
    return t

# Reserved words and ID rule
def t_ID(t):
    r'([a-zA-Z_][a-zA-Z_0-9]*)'
    t.type = reserved.get(t.value.upper(), 'ID')  # Check for reserved words
    return t

# Newline rule
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Comments
def t_comment(t):
    r'//[^\n]*'
    t.lexer.lineno += 1
    pass

def t_comments(t):
    r'\{(.|\n)*?\}'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_comments_2(t):
    r'\(\*(.|\n)*?\*\)'
    t.lexer.lineno += t.value.count('\n')
    pass

# Error handling rule
def t_error(t):
    print("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

# Ignore spaces and tabs
t_ignore = ' \t'

# Test function for lexer
def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# Build the lexer
lexer = lex.lex()

# Main function for testing
if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = sys.argv[1]
    else:
        fin = 'evaluacion.pas'
    with open(fin, 'r') as f:
        data = f.read()
    lexer.input(data)
    test(data, lexer)
