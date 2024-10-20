class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parse_expression(expr: str) -> bool:
            if expr == 't':
                return True
            elif expr == 'f':
                return False
            elif expr.startswith('!'):
                return not parse_expression(expr[2:-1])
            elif expr.startswith('&'):
                sub_exprs = split_expressions(expr[2:-1])
                return all(parse_expression(sub) for sub in sub_exprs)
            elif expr.startswith('|'):
                sub_exprs = split_expressions(expr[2:-1])
                return any(parse_expression(sub) for sub in sub_exprs)
            else:
                raise ValueError("Invalid expression")

        def split_expressions(expr: str) -> list:
            sub_exprs = []
            balance = 0
            start = 0
            for i, char in enumerate(expr):
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                elif char == ',' and balance == 0:
                    sub_exprs.append(expr[start:i])
                    start = i + 1
            sub_exprs.append(expr[start:])
            return sub_exprs

        return parse_expression(expression)

