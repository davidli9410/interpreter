import operator

arithmetic_operations_binary = {

    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv,
    "^" : operator.pow

}

arithmetic_operations_unary = {

    "-" : operator.neg,
    "!" : operator.not_

}

comparison_operations = {

    "equals" : operator.eq,
    "nequals" : operator.ne,
    "lt" : operator.lt,
    "lte" : operator.le,
    "gt" : operator.gt,
    "gte" : operator.ge

}

#TODO - same optimization for types

types = {
    
}