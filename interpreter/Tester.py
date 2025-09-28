from .Interpreter import Interpreter

class Tester:

    def test_interpreter(self):
        interpreter = Interpreter()
        
        precedence_tests = [
            ("5 + 3 * 2", 11.0),           # Should be 5 + (3 * 2) = 11
            ("10 - 2 * 3", 4.0),           # Should be 10 - (2 * 3) = 4
            ("2 + 3 * 4 + 5", 19.0),       # Should be 2 + (3 * 4) + 5 = 19
            ("8 / 2 + 3 * 2", 10.0),       # Should be (8 / 2) + (3 * 2) = 10
            ("2 ^ 3 + 1", 9.0),            # Should be (2 ^ 3) + 1 = 9
            ("3 * 2 ^ 2", 12.0),           # Should be 3 * (2 ^ 2) = 12
            ("10 - 2 ^ 2", 6.0)            # Should be 10 - (2 ^ 2) = 6
        ]

        associativity_tests = [
            ("2 ^ 3 ^ 2", 512.0),          # Should be 2 ^ (3 ^ 2) = 2 ^ 9 = 512
            ("5 + 3 + 2", 10.0),           # Should be (5 + 3) + 2 = 10
            ("5 * 3 * 2", 30.0),           # Should be (5 * 3) * 2 = 30
            ("10 - 3 - 2", 5.0),           # Should be (10 - 3) - 2 = 5
            ("8 / 4 / 2", 1.0)             # Should be (8 / 4) / 2 = 1
        ]

        parentheses_tests = [
            ("(5 + 3) * 2", 16.0),         # Should be 8 * 2 = 16
            ("5 + (3 * 2)", 11.0),         # Should be 5 + 6 = 11
            ("((5 + 3) * 2)", 16.0),       # Should be 8 * 2 = 16
            ("(2 + 3) * (4 + 1)", 25.0),   # Should be 5 * 5 = 25
            ("2 ^ (3 + 1)", 16.0)          # Should be 2 ^ 4 = 16
        ]

        unary_tests = [
            ("-5 + 3", -2.0),              # Should be -5 + 3 = -2
            ("5 + -3", 2.0),               # Should be 5 + (-3) = 2
            ("-2 * 3", -6.0),              # Should be -2 * 3 = -6
            ("2 ^ -2", 0.25),              # Should be 2 ^ (-2) = 0.25
            ("-(-5)", 5.0)                 # Should be -(-5) = 5
        ]


        variable_tests = [
            ("define x as 5", 5.0),                    # Simple assignment
            ("define y as 10", 10.0),                  # Another assignment
            ("define z as x + y", 15.0),               # Assignment with variables
            ("define w as x + y + z", 30.0)
        ]
        
        all_tests = [
            precedence_tests,
            associativity_tests,
            parentheses_tests,
            unary_tests,
            variable_tests
        ]
        total_cases = 0
        
        count = 0
        for tests in all_tests:
            total_cases += len(tests)
            
            for expression,expected in tests:
                try:
                    result = interpreter.run(expression)
                    if result == expected:
                        count += 1
                    print(f"expression : {expression}, result: {result}, expected : {expected}")

                except Exception as e:
                    print("Error")
        print(f"total cases: {total_cases}, cases passed: {count}")

    def test_from_file(self,filename):
        interpreter = Interpreter()

        with open(filename, "r") as file:
            for line_num, line in enumerate(file, 1):
                expression = line.strip()

                if expression:
                    try:
                        result = interpreter.run(expression)
                        print(f"expression : {expression}, result: {result}")
                    except Exception as e:
                        print(f"Error on line {line_num}")

    
        

if __name__ == "__main__":
    tester = Tester()
    tester.test_interpreter()
    print("Testing with file")
    tester.test_from_file("code.txt")