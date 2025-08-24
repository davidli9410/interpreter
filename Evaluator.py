class Evaluator:
    def eval(self, ast_node, env=None):
        return ast_node.eval(env)
