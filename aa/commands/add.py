from aa.registry import Command, register

@register
class Add(Command):
    name = "add"

    def execute(self) -> None:
        print("1+1=", 1+1)