class ASTNode:
    pass

class NumberNode(ASTNode):
    def __init__(self,value):
        self.value = value
    def eval(self, env):
        return float(self.value)
    
class OperatorNode(ASTNode):
    def __init__(self,operator,left,right):
        self.operator = operator
        self.left = left
        self.right = right

    def eval(self,env):
        left_val = self.left.eval(env)
        right_val = self.right.eval(env)

        if self.operator == "^":
            return left_val ** right_val
        elif self.operator == "*":
            return left_val * right_val
        elif self.operator == "/":
            return left_val / right_val
        elif self.operator == "+":
            return left_val + right_val 
        elif self.operator == "-":
            return left_val - right_val
        else:
            raise ValueError("Unknown operator")

class UnaryOpNode(ASTNode):
    def __init__(self, operator, operand): 
        self.operator = operator  
        self.operand = operand

    def eval(self,env):
        val = self.operand.eval(env)

        if self.operator == "-":
            return -val
        if self.operator == "!":
            return not val
        else:
            raise ValueError("Unknown unary operator")
class VariableNode(ASTNode):
    def __init__(self,name):
        self.name = name
    def eval(self,env):
        if self.name not in env:
            raise ValueError("Variable not defined")
        return env[self.name]
class AssignmentNode(ASTNode):
    def __init__(self, variable, value):
        self.variable = variable  # VariableNode
        self.value = value        # ASTNode (expression)
    def eval(self,env):
        ret = self.value.eval(env)
        env[self.variable.name] = ret
        return ret



    