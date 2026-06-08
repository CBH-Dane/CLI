from aa.registry import Command, register

@register
class Ping(Command):
    name = "ping"

    def execute(self, args: list[str]) -> int: # args ignored
        print("ok")
        return 0