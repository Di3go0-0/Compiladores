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
     
def p_formal_parameter_list(p):
    '''formal_parameter_list : LPAREN formal_parameter_section formal_parameter_list_1 RPAREN'''

def p_formal_parameter_list_1(p):
    '''formal_parameter_list_1 : SEMICOLON formal_parameter_section formal_parameter_list_1
        | empty'''

def p_formal_parameter_section(p):
	'''formal_parameter_section : value_parameter_section | variable_parameter_section
		| procedure_parameter_section | function_parameter_section'''

def p_fraction_length(p):
	'''fraction_length : expression'''
 
def p_funtion_declaration(p):
	'''function_declaration : function_heading SEMICOLON function_declaration_1 ;'''
 
def p_function_declaration_1(p):
	'''function_declaration_1 : directive
	    | block'''
     
def p_function_designator(p):
    '''function_designator : ID function_designator_opt_1'''

def p_function_designator_opt_1(p):
	'''function_designator_opt_1 : actual_parameter_list
 		| empty'''

def p_function_heading(p):
	'''function_heading : FUNCTION ID function_heading_opt_1 COLON result_type'''

def p_function_heading_opt_1(p):
	'''function_heading_opt_1 : formal_parameter_list
	    | empty'''
     
def p_funtion_parameter_section(p):
	'''function_parameter_section : function_heading'''

def p_goto_statement(p):
	'''goto_statement : GOTO label'''
 
def p_identifier_list(p):
	'''identifier_list : ID identifier_list_1'''

def p_identifier_list_1(p):
	'''identifier_list_1 : COMMA ID identifier_list_1
	    | empty'''
     
def p_if_statement(p):
	'''if_statement : IF expression THEN statement if_statement_opt_1'''

def p_if_statement_opt_1(p):
	'''if_statement_opt_1 : ELSE statement
	    | empty'''
def p_index_type(p):
	'''index_type : simple_type'''
 
def p_indexed_variable(p):
	'''indexed_variable : array_variable LBRACKET expression_list RBRACKET'''
 
def p_initial_expression(p):
	'''initial_expression : expression'''
 
def p_integer_number(p):
	'''integer : ID'''

def p_label_declaration_part(p):
	'''label_declaration_part : LABEL label label_declaration_part_1 SEMICOLON'''
 
def label_declaration_part_1(p):
	'''label_declaration_part_1 : SEMICOLON label label_declaration_part_1
	    | empty''' 
     
def p_label(p):
	'''label : ID'''

def p_lower_bound(p):
	'''lower_bound : constant'''

def p_multiplication_operator(p):
	'''multiplication_operator : TIMES
	    | DIVIDE
		| MOD
		| AND'''

def p_number(p):
	'''number : integer
	    | real_number'''

def p_ordinal_type_identifier(p):
	'''ordinal_type_identifier : ID'''

def p_output_list(p):
	'''output_list : output_value output_list_opt_1'''

def p_output_list_opt_1(p):
	'''output_list_opt_1 : COMMA output_value output_list_opt_1
	    | empty'''

def p_output_value(p):
	'''output_value : expression output_value_opt_1'''

def p_output_value_opt_1(p):
	'''output_value_opt_1 : SEMICOLON field_width output_value_opt_2
	    | empty'''

def p_output_value_opt_2(p):
	'''output_value_opt_2 : COLON francion_length
	    | empty'''

def p_packed_conformant_array_schema(p):
	'''packed_conformant_array_schema : PACKED ARRAY LBRACKET bound_specification RBRACKET OF ID'''
 
def p_parameter_type(p):
    '''parameter_type : ID | conformant_array_schema'''

def p_pointer_type(p):
	'''pointer_type : CIRCUMFLEXTO ID'''

def p_pointer_variable(p):
	'''pointer_variable : variable'''
 
def p_procedure_and_function_declaration_part(p):
    '''procedure_and_function_declaration_part : procedure_and_function_declaration_part_1'''

def p_procedure_and_function_declaration_part_1(p):
    '''procedure_and_function_declaration_part_1 : procedure_declaration SEMICOLON procedure_and_function_declaration_part_1
                                                 | function_declaration SEMICOLON procedure_and_function_declaration_part_1
                                                 | empty'''

def p_procedure_declaration(p):
	'''procedure_declaration : procedure_heading SEMICOLON procedure_declaration_1'''
 
def p_procedure_declaration_1(p):
	'''procedure_declaration_1 : directive
	    | block'''

def p_procedure_heading(p):
    '''procedure_heading : PROCEDURE ID procedure_heading_opt_1'''
    
def p_procedure_heading_opt_1(p):
	'''procedure_heading_opt_1 : formal_parameter_list
	    | empty'''

def p_procedure_parameter_section(p):
    '''procedure_parameter_section : procedure_heading'''

def p_procedure_statement(p):
    '''procedure_statement : ID procedure_statement_opt_1'''
    
def p_procedure_statement_opt_1(p):
	'''procedure_statement_opt_1 : actual_parameter_list
	    | empty'''
     
def p_program_heading(p):
    '''program_heading : PROGRAM ID LPAREN identifier_list RPAREN SEMICOLON'''

def p_program(p):
    '''program : program_heading block DOT'''

def p_real_number(p):
    '''real_number : ID'''

def p_record_section(p):
    '''record_section : identifier_list COLON type'''

def p_record_type(p):
    '''record_type : RECORD field_list END'''

def p_record_variable(p):
    '''record_variable : variable'''

def p_referenced_variable(p):
    '''referenced_variable : pointer_variable CIRCUMFLEXTO'''

def p_relational_operator(p):
    '''relational_operator : EQUAL
                           | NOTEQUAL
                           | LESS
                           | LESSEQUAL
                           | GREATER
                           | GREATEREQUAL
                           | IN'''

def p_repeat_statement(p):
    '''repeat_statement : REPEAT statement_sequence UNTIL expression'''

def p_repetitive_statement(p):
    '''repetitive_statement : while_statement
                            | repeat_statement
                            | for_statement'''

def p_result_type(p):
    '''result_type : ID'''

def p_set_type(p):
    '''set_type : SET OF base_type'''
    
def p_set(p):
    '''set : LBRACKET element_list RBRACKET'''

def p_simple_expression(p):
    '''simple_expression : simple_expression_opt_1 term simple_expression_1'''

def p_simple_expression_1(p):
    '''simple_expression_1 : addition_operator term simple_expression_1
                           | empty'''
def p_simple_expression_opt_1(p):
	'''simple_expression_opt_1 : PLUS | MINUS | empty'''

def p_simple_statement(p):
    '''simple_statement : assignment_statement
                        | procedure_statement
                        | goto_statement
                        | empty'''

def p_simple_type(p):
    '''simple_type : subrange_type
                   | enumerated_type'''

def p_statement_part(p):
    '''statement_part : BEGIN statement_sequence END'''

def p_statement_sequence(p):
    '''statement_sequence : statement statement_sequence_1'''

def p_statement_sequence_1(p):
    '''statement_sequence_1 : SEMICOLON statement statement_sequence_1
                            | empty'''

def p_statement(p):
    '''statement : statement_opt_1 statement_1'''

def p_statement_1(p):
    '''statement_1 : simple_statement
                   | structured_statement'''

def p_statement_opt_1(p):
	'''statement_opt_1 : Label  COLON
					   | empty'''

def p_structured_statement(p):
    '''structured_statement : compound_statement
                            | repetitive_statement
                            | conditional_statement
                            | with_statement'''

def p_structured_type(p):
    '''structured_type : structered_type_opt_1 unpacked_structured_type'''
                       
def p_structered_type_opt_1(p):
	'''structered_type_opt_1 : PACKED | empty'''

def p_subrange_type(p):
    '''subrange_type : lower_bound DOT DOT upper_bound'''

def p_tag_field(p):
    '''tag_field : ID COLON
                 | empty'''

def p_term(p):
    '''term : factor term_1'''

def p_term_1(p):
    '''term_1 : multiplication_operator factor term_1
              | empty'''

def p_type_definition_part(p):
    '''type_definition_part : TYPE type_definition SEMICOLON type_definition_part_1'''

def p_type_definition_part_1(p):
    '''type_definition_part_1 : type_definition SEMICOLON type_definition_part_1
                              | empty'''

def p_type_definition(p):
    '''type_definition : ID EQUAL type'''

def p_type(p):
    '''type : simple_type
            | structured_type
            | pointer_type
            | ID'''

def p_unpacked_conformant_array_schema(p):
    '''unpacked_conformant_array_schema : ARRAY LBRACKET bound_specification unpacked_conformant_array_schema_1 RBRACKET OF unpacked_conformant_array_schema_2'''

def p_unpacked_conformant_array_schema_1(p):
    '''unpacked_conformant_array_schema_1 : SEMICOLON bound_specification unpacked_conformant_array_schema_1
                                          | empty'''

def p_unpacked_conformant_array_schema_2(p):
    '''unpacked_conformant_array_schema_2 : ID
                                          | conformant_array_schema'''

def p_unpacked_structured_type(p):
    '''unpacked_structured_type : array_type
                                | record_type
                                | set_type
                                | file_type'''

def p_upper_bound(p):
    '''upper_bound : constant'''

def p_value_parameter_section(p):
    '''value_parameter_section : identifier_list COLON parameter_type'''

def p_variable_declaration_part(p):
    '''variable_declaration_part : VAR variable_declaration SEMICOLON variable_declaration_part_1'''

def p_variable_declaration_part_1(p):
    '''variable_declaration_part_1 : variable_declaration SEMICOLON variable_declaration_part_1
                                   | empty'''

def p_variable_declaration(p):
    '''variable_declaration : identifier_list COLON type'''

def p_variable_parameter_section(p):
    '''variable_parameter_section : VAR identifier_list COLON parameter_type'''

def p_variable(p):
    '''variable : entire_variable
                | component_variable
                | referenced_variable'''

def p_variant_part(p):
    '''variant_part : CASE tag_field TYPE_NAME OF variant variant_part_1'''

def p_variant_part_1(p):
    '''variant_part_1 : SEMICOLON variant variant_part_1
                      | empty'''

def p_variant(p):
    '''variant : case_label_list COLON LPAREN field_list RPAREN'''

def p_while_statement(p):
    '''while_statement : WHILE expression DO statement'''

def p_with_statement(p):
    '''with_statement : WITH record_variable with_statement_1 DO statement'''

def p_with_statement_1(p):
    '''with_statement_1 : COMMA record_variable with_statement_1
                        | empty'''

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