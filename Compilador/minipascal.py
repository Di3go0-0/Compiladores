import ply.lex as lex
import sys

# lista de tokens
tokens = (
	# Reserved words
	'ABSOLUTE',
    'AND',
    'ARRAY',
    'ASM',	
    'BEGIN',
    'CASE', 
    'CONST',
    'CONSTRUCTOR',	
    'DESTRUCTOR',
    'EXTERNAL',	
    'DIV',	
    'DO',	
    'DOWNTO',	
    'ELSE',	
    'END',
    'FILE',
    'FOR',
    'FORWARD',	
    'FUNCTION',
    'GOTO',
    'IF',
    'IMPLEMENTATION',	
    'IN',
    'INLINE',	
    'INTERFACE',
    'INTERRUPT',	
    'LABEL',
    'MOD',
    'NIL',
    'NOT',
    'OBJECT',
    'OF',
    'OR',
    'PACKED',	
    'PRIVATE',		
    'PROCEDURE',
    'PROGRAM',
    'RECORD',
    'REPEAT',
    'SET',
    'SHL',
    'SHR',	
    'STRING',
    'THEN',
    'TO',
    'TYPE',
    'UNIT',
    'UNTIL',
    'USES',
    'VAR',
    'VIRTUAL',
    'WHILE',
    'WITH',
    'XOR',

    # Symbols
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULUS',
    'EQUAL',
    'LESS',
    'GREATER',
    'EXCLAMATION',
    'COLON',
    'SEMICOLON',
    'COMMA',
    'DOT',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'AMPERSANT',
    'PIPE',
    'HASHTAG',
    'DIACRITIC',
    'DOLLAR',
    'SQUOTE',
    
    # Operators     
    'DEQUAL',
    'LESSEQUAL',
    'GREATEREQUAL',
    'LSHIFT',
    'RSHIFT',
    'ASSIGN',

    # Others   
    'ID', 
    'NUMBER',
    'CONSTSTRING',
)

# Regular expressions rules for a simple tokens 
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_MODULUS = r'%'
t_EQUAL  = r'='
t_LESS   = r'<'
t_GREATER = r'>'
t_EXCLAMATION = r'!'
t_COLON   = r':'
t_SEMICOLON = ';'
t_COMMA  = r','
t_DOT = r'\.'
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_AMPERSANT = r'\&'
t_PIPE = r'\|'
t_HASHTAG = r'\#'
t_DIACRITIC = r'~'
t_DOLLAR = r'\$'
t_SQUOTE = r'\''
#t_STRING = r'(\".*?\")'

def t_CONSTSTRING(t):
    r'(\".*?\")|(\'.*?\')'
    return t

def t_DEQUAL(t):
	r'<>'
	return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_LSHIFT(t):
    r'<<'
    return t

def t_RSHIFT(t):
    r'>>'
    return t

def t_ASSIGN(t):
    r':='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    

def t_ABSOLUTE(t):
    r'(A|a)(B|b)(S|s)(O|o)(L|l)(U|u)(T|t)(E|e)'
    return t
def t_AND(t):
    r'(A|a)(N|n)(D|d)'
    return t
def t_ARRAY(t):
    r'(A|a)(R|r)(R|r)(A|a)(Y|y)'
    return t

def t_ASM(t):
    r'(A|a)(S|s)(M|m)'
    return t

def t_BEGIN(t):
    r'(B|b)(E|e)(G|g)(I|i)(N|n)'
    return t

def t_CASE(t):
    r'(C|c)(A|a)(S|s)(E|e)'
    return t

def t_CONST(t):
    r'(C|c)(O|o)(N|n)(S|s)(T|t)'
    return t

def t_CONSTRUCTOR(t):
    r'(C|c)(O|o)(N|n)(S|s)(T|t)(R|r)(U|u)(C|c)(T|t)(O|o)(R|r)'
    return t

def t_DESTRUCTOR(t):
    r'(D|d)(E|e)(S|s)(T|t)(R|r)(U|u)(C|c)(T|t)(O|o)(R|r)'
    return t

def t_EXTERNAL(t):
    r'(E|e)(X|x)(T|t)(E|e)(R|r)(N|n)(A|a)(L|l)'
    return t

def t_DIV(t):
    r'(D|d)(I|i)(V|v)'
    return t

def t_DO(t):
    r'(D|d)(O|o)'
    return t

def t_DOWNTO(t):
    r'(D|d)(O|o)(W|w)(N|n)(T|t)(O|o)'
    return t

def t_ELSE(t):
    r'(E|e)(L|l)(S|s)(E|e)'
    return t

def t_END(t):
    r'(E|e)(N|n)(D|d)'
    return t

def t_FILE(t):
    r'(F|f)(I|i)(L|l)(E|e)'
    return t

def t_FOR(t):
    r'(F|f)(O|o)(R|r)'
    return t

def t_FORWARD(t):
    r'(F|f)(O|o)(R|r)(W|w)(A|a)(R|r)(D|d)'
    return t

def t_FUNCTION(t):
    r'(F|f)(U|u)(N|n)(C|c)(T|t)(I|i)(O|o)(N|n)'
    return t

def t_GOTO(t):
    r'(G|g)(O|o)(T|t)(O|o)'
    return t

def t_IF(t):
    r'(I|i)(F|f)'
    return t

def t_IMPLEMENTATION(t):
    r'(I|i)(M|m)(P|p)(L|l)(E|e)(M|m)(E|e)(N|n)(T|t)(A|a)(T|t)(I|i)(O|o)(N|n)'
    return t

def t_IN(t):
    r'(I|i)(N|n)'
    return t

def t_INLINE(t):
    r'(I|i)(N|n)(L|l)(I|i)(N|n)(E|e)'
    return t

def t_INTERFACE(t):
    r'(I|i)(N|n)(T|t)(E|e)(R|r)(F|f)(A|a)(C|c)(E|e)'
    return t

def t_INTERRUPT(t):
    r'(I|i)(N|n)(T|t)(E|e)(R|r)(R|r)(U|u)(P|p)(T|t)'
    return t

def t_LABEL(t):
    r'(L|l)(A|a)(B|b)(E|e)(L|l)'
    return t

def t_MOD(t):
    r'(M|m)(O|o)(D|d)'
    return t

def t_NIL(t):
    r'(N|n)(I|i)(L|l)'
    return t

def t_NOT(t):
    r'(N|n)(O|o)(T|t)'
    return t

def t_OBJECT(t):
    r'(O|o)(B|b)(J|j)(E|e)(C|c)(T|t)'
    return t

def t_OF(t):
    r'(O|o)(F|f)'
    return t

def t_OR(t):
    r'(O|o)(R|r)'
    return t

def t_PACKED(t):
    r'(P|p)(A|a)(C|c)(K|k)(E|e)(D|d)'
    return t

def t_PRIVATE(t):
    r'(P|p)(R|r)(I|i)(V|v)(A|a)(T|t)(E|e)'
    return t

def t_PROCEDURE(t):
    r'(P|p)(R|r)(O|o)(C|c)(E|e)(D|d)(U|u)(R|r)(E|e)'
    return t

def t_PROGRAM(t):
    r'(P|p)(R|r)(O|o)(G|g)(R|r)(A|a)(M|m)'
    return t

def t_RECORD(t):
    r'(R|r)(E|e)(C|c)(O|o)(R|r)(D|d)'
    return t

def t_REPEAT(t):
    r'(R|r)(E|e)(P|p)(E|e)(A|a)(T|t)'
    return t

def t_SET(t):
    r'(S|s)(E|e)(T|t)'
    return t

def t_SHL(t):
    r'(S|s)(H|h)(L|l)'
    return t

def t_SHR(t):
    r'(S|s)(H|h)(R|r)'
    return t

def t_STRING(t):
    r'(S|s)(T|t)(R|r)(I|i)(N|n)(G|g)'
    return t

def t_THEN(t):
    r'(T|t)(H|h)(E|e)(N|n)'
    return t

def t_TO(t):
    r'(T|t)(O|o)'
    return t

def t_TYPE(t):
    r'(T|t)(Y|y)(P|p)(E|e)'
    return t

def t_UNIT(t):
    r'(U|u)(N|n)(I|i)(T|t)'
    return t

def t_UNTIL(t):
    r'(U|u)(N|n)(T|t)(I|i)(L|l)'
    return t

def t_USES(t):
    r'(U|u)(S|s)(E|e)(S|s)'
    return t

def t_VAR(t):
    r'(V|v)(A|a)(R|r)'
    return t

def t_VIRTUAL(t):
    r'(V|v)(I|i)(R|r)(T|t)(U|u)(A|a)(L|l)'
    return t

def t_WHILE(t):
    r'(W|w)(H|h)(I|i)(L|l)(E|e)'
    return t

def t_WITH(t):
    r'(W|w)(I|i)(T|t)(H|h)'
    return t

def t_XOR(t):
    r'(X|x)(O|o)(R|r)'
    return t

def t_INVALIDID(t):
    r'[^_a-zA-Z]([a-zA-Z]|_|\d)+'
    print(f"lexical error: invalid identfiier starting with a digit")
    t.lexer.skip(len(t.value))


def t_ID(t):
    r'([a-zA-Z]|_)([a-zA-Z]|_|\d)*'
    return t

def t_NUMBER(t):
    r'(-?)[0-9]+(\.-?[0-9]+)?((e|E)(-)?[0-9]+)?' 
    return t

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

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

    
t_ignore = ' \t'

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'evaluacion.pas'
	f = open(fin, 'r')
	data = f.read()
	print("ey wat",data)
	lexer.input(data)
	test(data, lexer)
	#input()