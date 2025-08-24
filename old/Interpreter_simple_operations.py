import os

class Interpreter_simple_operations:
    def __init__(self):

        self.operators = ['+', '-', '*', '/', '^']
        
        self.precedence = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2}

        self.associativity = {"^": "right", "*": "left", "/": "left", "+": "left", "-": "left"}

    def is_number(self, token):
        """Check if a token is a number"""
        try:
            float(token)
            return True
        except ValueError:
            return False

    def parse(self, file):
        """Convert infix expression to postfix using Shunting-yard algorithm"""
        processed = file.replace("+", " + ").replace("-", " - ").replace("*", " * ")
        processed = processed.replace("/", " / ").replace("^", " ^ ").replace("(", " ( ").replace(")", " ) ")
        tokens = processed.split()

        output_q = []
        operator_stack = []
        
        while tokens:
            token = tokens.pop(0)
            
            if self.is_number(token):
                output_q.append(token)
            elif token in self.operators:
                while (operator_stack and 
                       (o2 := operator_stack[-1]) != "(" and 
                       (self.precedence[o2] > self.precedence[token] or 
                        (self.precedence[o2] == self.precedence[token] and 
                         self.associativity[o2] == "left"))):
                    output_q.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == ",":
                while operator_stack and (o2 := operator_stack[-1]) != "(":
                    output_q.append(operator_stack.pop())
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack and (o2 := operator_stack[-1]) != "(":
                    output_q.append(operator_stack.pop())
                assert operator_stack[-1] == "("
                operator_stack.pop()
        
        while operator_stack:
            assert operator_stack[-1] != "("
            output_q.append(operator_stack.pop())
        
        return output_q

    def eval(self, expression, env=None):
        """Evaluate a postfix expression"""
        if env is None:
            env = {}

        stack = []

        for token in expression:
            if self.is_number(token):
                stack.append(float(token))
            elif token in self.operators:
                b = stack.pop()
                a = stack.pop()
                if token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(a / b)
                elif token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)  
                elif token == "^":
                    stack.append(a ** b)
            elif token in env:

                stack.append(env[token])
            else:
                raise ValueError(f"Error, token is of unknown type: {token}")  
        return stack[0] if stack else 0

def test_parser():
    """Test the shunting-yard algorithm with various expressions"""
    
    interpreter = Interpreter_simple_operations()
    

    test_cases = [
        ("3 + 4", ["3", "4", "+"]),
        ("2 * 3 + 4", ["2", "3", "*", "4", "+"]),
        ("( 2 + 3 ) * 4", ["2", "3", "+", "4", "*"]),
        ("10 - 5 * 2", ["10", "5", "2", "*", "-"]),
        ("2 ^ 3 ^ 2", ["2", "3", "2", "^", "^"]),  
        ("1 + 2 + 3", ["1", "2", "+", "3", "+"]), 
        ("(1 + 2) * 3", ["1", "2", "+", "3", "*"]),
        ("(1 ^ 10) ^ (2 ^ 15) + (10 * 5)", ["1", "10", "^", "2", "15", "^", "^", "10" ,"5", "*", "+"])

    ]
    
    print("Testing Shunting-Yard Algorithm:")
    print("=" * 40)
    
    for expression, expected in test_cases:
        result = interpreter.parse(expression)
        print(result)
        val = interpreter.eval(result)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} | Input: {expression}")
        print(f"         Expected: {expected}")
        print(f"         Got:      {result}")
        print(f"         Value:    {val}")
        print()

if __name__ == "__main__":
    test_parser()
