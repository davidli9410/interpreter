class ASTNode:
    pass

class NumberNode(ASTNode):
    def __init__(self,value):
        self.value = value
    def eval(self, env):
        return float(self.value)
    
class BooleanNode(ASTNode):
    def __init__(self, value):
        self.value = value
    def eval(self,env):
        return bool(self.value)
    
class ComparisonNode(ASTNode):
    def __init__(self,comparator,left,right):
        self.comparator = comparator
        self.left = left
        self.right = right
    def eval(self,env):
        left_val = self.left.eval(env)
        right_val = self.right.eval(env)

        if self.comparator == "equals":
            return left_val == right_val
        
        elif self.comparator == "lt" :
            return left_val < right_val
        elif self.comparator == "lte":
            return left_val <= right_val
        elif self.comparator == "gt":
            return left_val > right_val
        elif self.comparator == "gte":
            return left_val >= right_val
        elif self.comparator == "nequals":
            return left_val != right_val
        else:
            raise ValueError(f"Unknown comparator: {self.comparator}")
    
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
            raise ValueError(f"Unknown operator: {self.operator}")

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
            raise ValueError(f"Unknown unary operator: {self.operator}")
class VariableNode(ASTNode):
    def __init__(self,name):
        self.name = name
    def eval(self,env):
        if self.name not in env:
            raise ValueError(f"Variable not defined: {self.variable}")
        return env[self.name]
class AssignmentNode(ASTNode):
    def __init__(self, variable, value):
        self.variable = variable  # VariableNode
        self.value = value        # ASTNode (expression)
    def eval(self,env):
        ret = self.value.eval(env)
        env[self.variable.name] = ret
        return ret



    