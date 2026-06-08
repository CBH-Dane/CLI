from __future__ import annotations

import pkgutil
from abc import ABC, abstractmethod

class Command(ABC):
    """Command Interface. Only seen by framework."""

    name: str

    @abstractmethod
    def execute(self) -> None:
        ...

class Registry:
    def __init__(self) -> None:
        self._commands: dict[str, type[Command]] = {}
    
    def register(self, command_cls: type[Command]) -> type[Command]:
        self._commands[command_cls.name] = command_cls
        return command_cls

    def get(self, name: str) -> Command | None:
        command_cls = self._commands.get(name)
        return command_cls() if command_cls is not None else None
    
    def names(self) -> list[str]:
        return list(self._commands)

registry = Registry()
register = registry.register

def load_commands(package: str = "aa.commands") -> None:
    pkg = importlib.import_module(package)
    for module in pkgutil.iter_modules(pkg.__path__):
        importlib.import_module(f"{package}.{module.name}")

def build_registry() -> Registry:
    load_commands()
    return registry