"""Framework core
Contains:
    - Command Interface/ABC
    - Command Registry
    - Command Discovery"""
from __future__ import annotations

import importlib
import pkgutil
from abc import ABC, abstractmethod

class Command(ABC):
    """Command Interface.
    `args` is a list of CLI tokens after the command name."""

    name: str

    @abstractmethod
    def execute(self, args: list[str]) -> int:
        ...     # Returns process exit code: 0 = success, non-zero = failure

class Registry:
    def __init__(self) -> None:
        # name -> class (not instance); instance built on lookup
        self._commands: dict[str, type[Command]] = {}
    
    def register(self, command_cls: type[Command]) -> type[Command]:
        # returns the class unchanged
        self._commands[command_cls.name] = command_cls
        return command_cls

    def get(self, name: str) -> Command | None:
        command_cls = self._commands.get(name)
        return command_cls() if command_cls is not None else None
    
    def names(self) -> list[str]:
        return list(self._commands)

# Module-level singleton; Any command file can import `register` and use
registry = Registry()
register = registry.register

def load_commands(package: str = "aa.commands") -> None:
    """Import every module under aa/commands/ so @register fires
    Registration is an import side-effect: command only exists once its module is imported. 
    The result is that dropping in a new file is the only step needed to import a new command."""
    pkg = importlib.import_module(package)
    for module in pkgutil.iter_modules(pkg.__path__):
        importlib.import_module(f"{package}.{module.name}")

def build_registry() -> Registry:
    load_commands()
    return registry