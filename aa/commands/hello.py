from aa.registry import Command, register

@register
class Hello(Command):
    name = "hello"

    def execute(self) -> None:
        print("hello world")