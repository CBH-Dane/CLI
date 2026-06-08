from aa.registry import Command, register

@register
class Hello(Command):
    name = "hello"

    def execute(self, args: list[str]) -> int: # args ignored
        print("hello world")
        return 0