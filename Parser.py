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
        # Parsing logic
        pass
    def parse_unary_expression(self, tokens):
        token = tokens.pop(0)
        if token in ["-", "!"]:
            operand = self.parse_basic(tokens)
            return u_op_node(token,operand)
        else:
            raise ValueError("Unknown unary operator")

    def parse_binary_expression(self, tokens):
        pass

    def parse_basic(self, tokens):

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




