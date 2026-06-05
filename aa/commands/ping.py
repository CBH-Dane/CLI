from aa.registry import Command, register

@register
class Ping(Command):
    name = "ping"

    def execute(self) -> None:
        print("ok")