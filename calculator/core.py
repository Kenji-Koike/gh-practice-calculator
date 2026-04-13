"""電卓の基本演算を提供するモジュール"""


class Calculator:
    """四則演算をサポートするシンプルな電卓クラス"""

    def add(self, a: float, b: float) -> float:
        """加算: a + b"""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """減算: a - b"""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """乗算: a * b"""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """除算: a / b

        Raises:
            ZeroDivisionError: b が 0 の場合
        """
        if b == 0:
            raise ZeroDivisionError("ゼロ除算はできません")
        return a / b

    def power(self, base: float, exp: float) -> float:
        """べき乗: base ** exp"""
        return base ** exp
