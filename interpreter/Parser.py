from .Helpers import Helpers
from .AST import OperatorNode as bin_op_node
from .AST import UnaryOpNode as u_op_node
from .AST import VariableNode as v_node
from .AST import NumberNode as n_node
from .AST import AssignmentNode as a_node
from .AST import BooleanNode as b_node
from .AST import ComparisonNode as c_node
from .AST import FunctionCallNode as f_c_node
from .AST import FunctionNode as f_node


class Parser:
    def __init__(self):
        self.operators = ['+', '-', '*', '/', '^']
        self.helpers = Helpers()
    
    def parse_whole(self, expression):
        tokens = self.tokenize(expression)
        if tokens[0] == "func":
            return self.parse_function_def(tokens)
        elif "define" in tokens and "as" in tokens:
            return self.parse_variable_assignment(tokens)
        elif tokens[0] == "display":
            tokens.pop(0)
            return self.parse_comparison(tokens)
        elif "equals" in tokens or "nequals" in tokens or "lt" in tokens or "lte" in tokens or "gt" in tokens or "gte" in tokens:
            return self.parse_comparison(tokens)
        else:
            return self.parse_low(tokens)
    
    def tokenize(self, expression):
        processed = expression.replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("=", " = ").replace("/", " / ").replace("^", " ^ ").replace("(", " ( ").replace(")", " ) ").replace(",", " , ").replace(":"," : ")
        return processed.split()
    
    def parse_function_def(self,tokens):
        tokens.pop(0)
        name = tokens.pop(0)

        if tokens.pop(0) != "(" :
            raise ValueError("Expected ( after function declaration")
        args = []
        while tokens and tokens[0] != ")":
            if tokens[0] != ",":
                args.append(tokens.pop(0))
            else:
                tokens.pop(0)
        tokens.pop(0)
        while tokens and tokens[0] == " ":
            tokens.pop()
        if tokens and tokens[0] != ":":
            raise ValueError("Incorrect function declaration")
        tokens.pop(0)
        body = self.parse_comparison(tokens)
        return f_node(name,args,body)
    
    def parse_function_call(self,tokens):
        name = tokens.pop(0)
        if tokens.pop(0) != "(" :
            raise ValueError("Expected ( after function declaration")
        args = []
        while tokens and tokens[0] != ")":
            if tokens[0] != ",":
                args.append(self.parse_comparison(tokens))
            else:
                tokens.pop(0)
        tokens.pop(0)
        return f_c_node(name,args)
    
    def parse_unary_expression(self, tokens):
        if tokens and tokens[0] in ["-", "!"]:
            token = tokens.pop(0)
            operand = self.parse_unary_expression(tokens)
            return u_op_node(token, operand)
        return self.parse_basic(tokens)
    
    def parse_high(self, tokens):
        left = self.parse_unary_expression(tokens)
        while tokens and tokens[0] == "^":
            token = tokens.pop(0)
            right = self.parse_high(tokens)
            left = bin_op_node(token, left, right)
        return left
    
    def parse_med(self, tokens):
        left = self.parse_high(tokens)
        while tokens and tokens[0] in ["*", "/"]:
            token = tokens.pop(0)
            right = self.parse_high(tokens)
            left = bin_op_node(token, left, right)
        return left
    
    def parse_low(self, tokens):
        left = self.parse_med(tokens)
        while tokens and tokens[0] in ["+", "-"]:
            token = tokens.pop(0)
            right = self.parse_med(tokens)
            left = bin_op_node(token, left, right)
        return left
    
    def parse_variable_assignment(self, tokens):
        if len(tokens) >= 4 and tokens[0] == "define" and tokens[2] == "as":
            tokens.pop(0)
            var = tokens.pop(0)
            tokens.pop(0)
            assignment_val = self.parse_comparison(tokens)
            return a_node(v_node(var), assignment_val)
        else:
            return self.parse_low(tokens)
    
    def parse_comparison(self, tokens):
        left = self.parse_low(tokens)
        while tokens and tokens[0] in ["equals", "nequals", "lt", "lte", "gt", "gte"]:
            comparator = tokens.pop(0)
            right = self.parse_low(tokens)
            left = c_node(comparator, left, right)
        return left
    
    def parse_basic(self, tokens):
        if not tokens:
            raise ValueError("Unexpected Termination")
        token = tokens.pop(0)
        if self.helpers.is_boolean(token):
            return b_node(token)
        elif self.helpers.is_number(token):
            return n_node(token)
        elif tokens and self.helpers.is_variable(token) and tokens[0] == "(": #is function call, ex. add(x,y)
            tokens.insert(0,token)
            return self.parse_function_call(tokens)
        elif self.helpers.is_variable(token):
            return v_node(token)
        elif token == "(":
            expression = self.parse_comparison(tokens)
            if not tokens or tokens.pop(0) != ')':
                raise ValueError("Mismatched parentheses: expected ')'")
            return expression
        else:
            raise ValueError(f"Invalid token: {token}")