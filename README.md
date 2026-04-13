# gh-practice-calculator

Python 電卓ライブラリ — `gh` コマンドを使った GitHub ワークフローの練習用リポジトリです。

## インストール

```bash
pip install -e ".[dev]"
```

## 使い方

```python
from calculator import Calculator

calc = Calculator()
print(calc.add(2, 3))       # 5
print(calc.subtract(10, 4)) # 6
print(calc.multiply(3, 4))  # 12
print(calc.divide(10, 2))   # 5.0
```

## テスト実行

```bash
pytest
```
