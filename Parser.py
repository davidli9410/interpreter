from Helpers import Helpers
from AST import OperatorNode as bin_op_node
from AST import UnaryOpNode as u_op_node
from AST import VariableNode as v_node
from AST import NumberNode as n_node
from AST import AssignmentNode as a_node

class Parser:
    def __init__(self):
        self.operators = ['+', '-', '*', '/', '^']
        self.precedence = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2}
        self.associativity = {"^": "right", "*": "left", "/": "left", "+": "left", "-": "left"}
        self.helpers = Helpers()
    
    def parse_whole(self, expression):

        tokens = self.tokenize(expression)

        if "define" in tokens and "as" in tokens:
            return self.parse_variable_assignment(tokens)
        else :
            return self.parse_low(tokens)
    
    def tokenize(self, expression):
        # Tokenization logic
        processed = expression.replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("=", " = ").replace("/", " / ").replace("^", " ^ ").replace("(", " ( ").replace(")", " ) ")

        return processed.split()
    
    def parse_unary_expression(self, tokens):
        
        if tokens and tokens[0] in ["-", "!"]:
            token = tokens.pop(0)
            operand = self.parse_unary_expression(tokens)
            return u_op_node(token,operand)
        
        return self.parse_basic(tokens)
    

    def parse_high(self,tokens):

        left = self.parse_unary_expression(tokens)
        while tokens and tokens[0] == "^":
            token = tokens.pop(0)
            right = self.parse_high(tokens)
            left = bin_op_node(token,left,right)
        return left
    
    def parse_med(self, tokens):
        
        left = self.parse_high(tokens)
        while tokens and tokens[0] in ["*", "/"]:
            token = tokens.pop(0)
            right = self.parse_high(tokens)
            left = bin_op_node(token,left,right)
        return left
    
    def parse_low(self,tokens):

        left = self.parse_med(tokens)
        while tokens and tokens[0] in ["+", "-"]:
            token = tokens.pop(0)
            right = self.parse_med(tokens)
            left = bin_op_node(token,left,right)
        return left
    
    def parse_variable_assignment(self,tokens):

        if len(tokens) >= 4 and tokens[0] == "define" and tokens[2] == "as":
            tokens.pop(0)
            var = tokens.pop(0)
            tokens.pop(0)
            assignment_val = self.parse_low(tokens)
            return a_node(v_node(var), assignment_val)
        else:
            return self.parse_low(tokens)
    
    def parse_basic(self, tokens):

        if not tokens:
            raise ValueError("Unexpected Termination")
        token = tokens.pop(0)

        if self.helpers.is_number(token):
            return n_node(token)
        elif self.helpers.is_variable(token):
            return v_node(token)
        elif token == "(":
            expression = self.parse_low(tokens)
            if not tokens or tokens.pop(0) != ')':
                raise ValueError("Mismatched parentheses: expected ')'")
            return expression
        else:
            raise ValueError(f"Invalid token: {token}")




