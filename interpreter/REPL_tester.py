from Interpreter import Interpreter
from Parser import Parser


class REPL_tester :
    def __init__(self):
        
        self.interpreter = Interpreter()
        self.parser = Parser()

    def start_test(self):

        while True:
            expression = input()
            if expression:
                result = self.interpreter.run(expression)
                tokenized = self.parser.tokenize(expression)
                if "define" in tokenized:
                    continue
                if "func" in tokenized:
                    continue
                elif "display" in tokenized:
                    print(f"{result}")
                else:
                    print(f"Result of expression: {result}")

if __name__ == "__main__":
    print("\033[1m" + "This is the interactive REPL command line tester for my interpreter. At any time, press ^C to exit the REPL" )
    print("\033[1m")

    repl = REPL_tester()
    repl.start_test()

