import ast
import operator
from typing import Any


class CalculationService:
    _allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
    }

    def evaluate(self, expression: str) -> float:
        try:
            node = ast.parse(expression, mode="eval").body
            return float(self._eval_node(node))
        except Exception as exc:  # noqa: BLE001
            raise ValueError("Invalid expression") from exc

    def _eval_node(self, node: ast.AST) -> Any:
        if isinstance(node, ast.BinOp) and type(node.op) in self._allowed_operators:
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            return self._allowed_operators[type(node.op)](left, right)
        if isinstance(node, ast.Num):
            return node.n
        raise ValueError("Unsupported operation")
