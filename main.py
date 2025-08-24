from dotenv import load_dotenv
import os
load_dotenv()

operators = os.getenv('operators', 'default_value')
precedence = {"^" : 4, "*" :3, "/":3, "+":2, "-":2}
associativity = {"^": "right" , "*": "left", "/" : "left", "+": "left" , "-" : "left"}
def parse(file):
    tokens = file.split()
    

    #Dijkstra's Shunting-yard algorithm
    output_q = []
    operator_stack = []
    while tokens :
        token = tokens.pop(0)
        

        if is_number(token) :
            output_q.append(token)


        elif token in operators:
            
            while operator_stack and o2 = operator_stack.pop() != "(" and precedence[o2] > precedence[token] or 
                i
            operator_stack.append()




    return 1



def eval(expression,env) :
    return 1
def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False