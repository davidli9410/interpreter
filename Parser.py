from Helpers import Helpers
from AST import OperatorNode,UnaryOpNode,VariableNode,NumberNode as bin_op_node,u_op_node,v_node, n_node
class Parser:
    def __init__(self):
        self.operators = ['+', '-', '*', '/', '^']
        self.precedence = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2}
        self.associativity = {"^": "right", "*": "left", "/": "left", "+": "left", "-": "left"}
        self.helpers = Helpers()
    
    def parse_whole(self, expression):
        tokens = self.tokenize(expression)
        return self.parse_expression(tokens)
    
    def tokenize(self, expression):
        # Tokenization logic
        processed = expression.replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("=", " = ").replace("/", " / ").replace("^", " ^ ").replace("(", " ( ").replace(")", " ) ")

        return processed.split()
    
    def parse_expression(self, tokens):
        return self.parse_low(tokens)
    def parse_unary_expression(self, tokens):
        
        if tokens and tokens[0] in ["-", "!"]:
            token = tokens.pop(0)
            operand = self.parse_basic(tokens)
            return u_op_node(token,operand)
        
        return self.parse_basic(tokens)
    

    def parse_high(self,tokens):
        if tokens:
            left = self.parse_unary_expression(tokens)
        while tokens and tokens[0] == "^":
            token = tokens.pop(0)
            right = self.parse_high(tokens)
            left = bin_op_node(token,left,right)
        return left
    def parse_med(self, tokens):
        if tokens:
            left = self.parse_unary_expression(tokens)
        while tokens and tokens[0] in ["*", "/"]:
            token = tokens.pop(0)
            right = self.parse_high(tokens)
            left = bin_op_node(token,left,right)
        return left
    def parse_low(self,tokens):
        if tokens:
            left = self.parse_unary_expression(tokens)
        while tokens and tokens[0] in ["+", "-"]:
            token = tokens.pop(0)
            right = self.parse_med(tokens)
            left = bin_op_node(token,left,right)
        return left
    def parse_basic(self, tokens):
        if not tokens:
            raise ValueError("Unexpected Termination")
        token = tokens.pop(0)

        if self.helpers.is_number(token):
            return n_node(token)
        elif self.helpers.is_variable(token):
            return v_node(token)
        elif token == "(":
            expression = self.parse_expression(tokens)
            if not tokens or tokens.pop(0) != ')':
                raise ValueError("Mismatched parentheses: expected ')'")
            return expression
        else:
            raise ValueError(f"Invalid token: {token}")




