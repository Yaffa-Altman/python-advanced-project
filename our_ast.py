import ast

def if_variable_unused(file_path):
    class VariableVisitor(ast.NodeVisitor):
        def __init__(self):
            self.defined_variables = set()
            self.used_variables = set()

        def visit_Assign(self, node):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.defined_variables.add(target.id)
            self.generic_visit(node)

        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Load):
                self.used_variables.add(node.id)

        def visit_FunctionDef(self, node):
            for arg in node.args.args:
                self.defined_variables.add(arg.arg)
            self.generic_visit(node)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()
    except FileNotFoundError:
        return "not found"

    try:
        tree = ast.parse(code)
        visitor = VariableVisitor()
        visitor.visit(tree)
        unused_variables = visitor.defined_variables - visitor.used_variables
        return unused_variables
    except SyntaxError:
        return "error in this file"
