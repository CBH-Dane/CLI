from __future__ import annotations
import sys
from abc import ABC, abstractmethod

# --- Framework: Knows nothing about specific commands ---
class Command(ABC):
    """Command Interface. Only seen by framework."""

    name: str

    @abstractmethod
    def execute(self) -> None:
        ...

class Registry:
    def __init__(self) -> None:
        self._commands: dict[str, Command] = {}
    
    def register(self, command: Command) -> None:
        self._commands[command.name] = command

    def get(self, name: str) -> Command | None:
        return self._commands.get(name)
    
    def names(self) -> list[str]:
        return list(self._commands)

def run(registry: Registry, argv: list[str]) -> int:
    if not argv or (command := registry.get(argv[0])) is None:
        print(f"Usage: aa {'|'.join(registry.names())}", file=sys.stderr)
        return 1
    command.execute()
    return 0

# --- Commands: depend on the framework, define only their own behavior ---

class Ping(Command):
    name = "ping"

    def execute(self) -> None:
        print("ok")

class Hello(Command):
    name = "hello"

    def execute(self) -> None:
        print("hello world")

class Add(Command):
    name = "add"

    def execute(self) -> None:
        print ("1+1=", 1+1)

# --- Wiring/Routing ---
def build_registry() -> Registry:
    registry = Registry()
    for command in (Ping(), Hello(), Add()):
        registry.register(command)
    return registry

def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    return run(build_registry(), argv)

if __name__ == "__main__":
    sys.exit(main())