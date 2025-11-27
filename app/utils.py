import ast
from typing import Any


class ExpressionEvaluator(ast.NodeVisitor):
    allowed_nodes = {
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.Pow,
        ast.Mod,
        ast.FloorDiv,
        ast.USub,
        ast.UAdd,
        ast.Load,
        ast.Constant,
        ast.Num,
        ast.Expr,
    }

    def visit(self, node: ast.AST) -> Any:  # type: ignore[override]
        if type(node) not in self.allowed_nodes:  # noqa: E721
            raise ValueError(f"Operación no permitida: {type(node).__name__}")
        return super().visit(node)


def evaluate_expression(expression: str) -> float:
    parsed = ast.parse(expression, mode="eval")
    ExpressionEvaluator().visit(parsed)
    compiled = compile(parsed, filename="<expression>", mode="eval")
    return float(eval(compiled, {"__builtins__": {}}, {}))


def process_text_payload(text: str) -> dict[str, Any]:
    uppercase = text.upper()
    word_count = len([segment for segment in text.split() if segment])
    return {"original": text, "uppercase": uppercase, "word_count": word_count}
