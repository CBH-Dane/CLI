"""add: sum any amount of numbers passed on the command line."""
import sys
from aa.registry import Command, register

@register
class Add(Command):
    name = "add"

    def execute(self, args: list[str]) -> int:
        if not args:
            print("add: need at least one number", file=sys.stderr)
            return 1
        try:
            numbers = [float(a) for a in args]
        except ValueError as exc:
            # e.g. "could not convert string to float: x"
            print(f"add: {exc}", file=sys.stderr)
            return 1
        total = sum(numbers)
        # Show 5 instead of 5.0 when the result is a whole number
        print(int(total) if total.is_integer() else total)
        return 0