import ply.yacc as yacc
from minipascal_lexer import tokens
import minipascal_lexer
import sys

VERBOSE = 1

def p_actual_function(p):
	'''actual_function : ID'''

def p_actual_parameter_list(p):
	'''actual_parameter_list: LPAREN actual_parameter actual_parameter_list_1 RPAREN'''

def p_actual_parameter_list_1(p):
	'''actual_parameter_list_1 : COMMA actual_parameter_list_1
	    | empty'''
	
def p_actual_parameter(p):
	'''actual_parameter : actual_value
	    | actual_variable
		| actual_procedure'''
	
def p_actual_procedure(p):
	'''actual_procedure : ID'''

def p_actual_value(p):
	'''actual_value : expression'''
	
def p_actual_variable(p):
	'''actual_variable : variable'''
	
def p_addition_operator(p):
	'''addition_operator : PLUS 
	    | MINUS
		| OR'''

def p_array_type(p):
	'''array_type : ARRAY LBRACKET index_type '''
	
def p_array_type_1(p):
	'''array_type_1 : COMMA index_type array_type_1
	    | empty'''
	
def p_array_variable(p):
	'''array_variable : variable'''
	
def p_assignment_statement(p):
	'''assignment_statement : variable ASSIGN expression
	    | ID ASSIGN expression'''
	
def p_base_type(p):
	'''base_type : type'''
	
def p_block(p):
	'''block : declaration_part statement_part'''
	
def p_bound_specification(p):
	'''bound_specification : ID DOT DOT ID COLON ordinal_type_identifier'''
	
def p_case_element(p):
	'''case_element : case_label_list COLON statement'''
	
def p_case_label_list(p):
	'''case_label_list : constant case_label_list_1'''
	
def p_case_label_list_1(p):
	'''case_label_list_1 : COMMA constant case_label_list_1
	    | empty'''

def p_case_statement(p):
	'''CASE expression OF case_element case_statement_1 case_statement_opt END'''
	
def p_case_statement_1(p):
	'''case_statement_1 : SEMICOLON case_element case_statement_1
	    | empty'''

def p_case_statement_opt(p):
	'''case_statement_opt : SEMICOLON
	    | empty'''
	
def p_component_variable(p):
	'''component_variable : indexed_variable
	    | field_designator
		| file_buffer'''

def p_compound_statement(p):
	'''compound_statement : BEGIN statement_sequence END'''
	
def p_conditional_statement(p):
	'''conditional_statement : if_statement
	    | case_statement'''
	
def p_conformant_array_schema(p):
	'''conformant_array_schema : packed_conformant_array_schema
	    | unpacked_conformant_array_schema'''
	
def p_constant_definition_part(p):
	'''constant_definition_part : CONST constant_definition SEMICOLON constant_definition_part_1'''
	
def p_constant_definition_part_1(p):
	'''constant_definition_part_1 : constant_definition SEMICOLON constant_definition_part_1
	    | empty'''
	
def p_constant_definition(p):
	'''constant_definition : ID EQUAL constant'''
	
def p_constant(p):
	'''constant : constant_opt_sign ID
	    | constant_opt_sign number
		| CONSTSTRING '''
	
def p_constant_opt_sign(p):
	'''constant_opt_sign : PLUS
	    | MINUS
		| empty'''
	

def p_declaration_part(p):
	'''declaration_part : declaration_part_opt_1 declaration_part_opt_2'''

def p_declaration_part_opt_1(p):
	'''declaration_part_opt_1 : label_declaration_part
	    | empty'''

def p_declaration_part_opt_2(p):
	'''declaration_part_opt_2 : constant_definition_part
	    | empty'''
	
def p_declaration_part_opt_3(p):
	'''declaration_part_opt_3 : type_definition_part
	    | empty'''

def p_declaration_part_opt_4(p):
	'''declaration_part_opt_4 : variable_declaration_part
	    | empty'''

def p_directive(p):
	'''directive : FORWARD'''

def p_element_list(p):
	'''element_list : expression element_list_1
	    | empty'''

def p_element_list_1(p):
	'''element_list_1 : COMMA expression element_list_1
	    | empty'''
	
def p_element_type(p):
	'''element_type : type'''
	
def p_entire_variable(p):
	'''entire_variable : ID'''
	
def p_enumerated_type(p):
	'''enumerated_type : LPAREN identifier_list RPAREN'''
	
def p_expression_list(p):
	'''expression_list : expression expression_list_1'''
	
def p_expression_list_1(p):
	'''expression_list_1 : COMMA expression expression_list_1
	    | empty'''

def p_expression(p):
	'''expression : simple_expression 
	    | simple_expression relational_operator simple_expression'''

def p_factor(p):
	'''factor : NUMBER
	    | CONSTSTRING
		| NIL
		| ID
		| set
		| variable
		| function_designator
		| LPAREN expression RPAREN
		| NOT factor'''

def p_field_designator(p):
    '''field_designator : record_variable DOT ID'''

def p_field_list(p):
	'''field_list : fixed_part field_list_opt_1 field_list_opt_2
	    | variant_part field_list_opt_2'''
	
def p_field_list_opt_1(p):
	'''field_list_opt_1 : SEMICOLON variant_part
	    | empty'''

def p_field_list_opt_2(p):
    '''field_list_opt_2 : SEMICOLON
	    | empty'''
    
def p_field_width(p):
	'''field_width : expression'''

def p_file_buffer(p):
	'''file_buffer : file_variable CIRCUMFLEX'''

def p_component_type(p):
	'''component_type : type'''

def p_file_type(p):
	'''file_type : FILE OF file_component_type'''

def p_file_variable(p):
	'''file_variable : variable'''

def p_final_expression(p):
	'''final_expression : expression'''

def p_fixed_part(p):
	'''fixed_part : record_section fixed_part_1'''

def p_fixed_part_1(p):
	'''fixed_part_1 : SEMICOLON record_section fixed_part_1
	    | empty'''

def p_for_statement(p):
	'''for_statement : FOR ID ASSIGN initial_expression for_statement_opt_1 final_expression DO statement'''

def p_for_statement_opt_1(p):
	'''for_statement_opt_1 : TO
	    | DOWNTO'''



def p_program(p):
	'''program : program_heading block DOT
	'''

def p_identifier_list(p):
	'''identifier_ist : ID LBLOCK COMMA ID RBLOCK'''
	

def p_empty(p):
	'''empty :'''

#######################################

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(minipascal_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba2.txt'

	f = open(fin, 'r')
	data = f.read()
	print (data)
	parser.parse(data, tracking=True)
	print("Amiguito, tengo el placer de informar que Tu parser reconocio correctamente todo")
	#input()