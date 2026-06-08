"""mul: multiply any amount of numbers passed on the command line."""
import math
import sys
from aa.registry import Command, register

@register
class Multiply(Command):
    name = "mul"

    def execute(self, args: list[str]) -> int:
        if not args:
            print("mul: need at least one number", file=sys.stderr)
            return 1
        try:
            numbers = [float(a) for a in args]
        except ValueError as exc:
            print(f"mul: {exc}", file=sys.stderr)
            return 1
        total = math.prod(numbers)
        print(int(total) if total.is_integer() else total)
        return 0