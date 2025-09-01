from Global import arithmetic_operations_binary
from Global import arithmetic_operations_unary
from Global import comparison_operations


class ASTNode:
    pass


class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value
    
    def eval(self, env):
        return float(self.value)


class BooleanNode(ASTNode):
    def __init__(self, value):
        self.value = value
    
    def eval(self, env):
        if self.value == "true":
            return True
        elif self.value == "false":
            return False
        else:
            raise ValueError(f"Unknown boolean: {self.value}")


class ComparisonNode(ASTNode):
    def __init__(self, comparator, left, right):
        self.comparator = comparator
        self.left = left
        self.right = right
    
    def eval(self, env):
        left_val = self.left.eval(env)
        right_val = self.right.eval(env)

        if self.comparator in comparison_operations:
            result = comparison_operations[self.comparator](left_val, right_val)
            return result
        else:
            raise ValueError(f"Unknown comparator: {self.comparator}")


class OperatorNode(ASTNode):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def eval(self, env):
        left_val = self.left.eval(env)
        right_val = self.right.eval(env)

        if self.operator in arithmetic_operations_binary:
            result = arithmetic_operations_binary[self.operator](left_val, right_val)
            return result
        else:
            raise ValueError(f"Unknown comparator: {self.operator}")


class UnaryOpNode(ASTNode):
    def __init__(self, operator, operand): 
        self.operator = operator  
        self.operand = operand

    def eval(self, env):
        val = self.operand.eval(env)

        if self.operator in arithmetic_operations_unary:
            result = arithmetic_operations_unary[self.operator](val)
            return result
        else:
            raise ValueError(f"Unknown comparator: {self.operator}")


class VariableNode(ASTNode):
    def __init__(self, name):
        self.name = name
    
    def eval(self, env):
        if self.name not in env:
            raise ValueError(f"Variable not defined: {self.name}")
        return env[self.name]


class AssignmentNode(ASTNode):
    def __init__(self, variable, value):
        self.variable = variable  
        self.value = value        

    def eval(self, env):
        ret = self.value.eval(env)
        env[self.variable.name] = ret
        return ret