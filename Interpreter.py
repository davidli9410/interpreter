from Parser import Parser
from Evaluator import Evaluator
class Interpreter:
    def __init__(self):
        self.parser = Parser()
        self.evaluator = Evaluator()
    
    def parse(self, expression):
        return self.parser.parse_whole(expression)
    
    def eval(self, ast_node, env=None):
        return self.evaluator.eval(ast_node, env)
    
    def run(self, code):
        # Handle multiple statements
        pass