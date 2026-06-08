"""Dispatch Core & Entry Point
Depends on Framework Core only."""
from __future__ import annotations
import sys
from aa.registry import Registry, build_registry

def run(registry: Registry, argv: list[str]) -> int:
    # No command or an unknown one: print usage guide derived from registry.
    if not argv or (command := registry.get(argv[0])) is None:
        print(f"Usage: aa {'|'.join(registry.names())}", file=sys.stderr)
        return 1
    
    # Split command name off; The rest is the command args
    name, *rest = argv
    return command.execute(rest)

def main(argv: list[str] | None = None) -> int:
    # argv is injectable so tests can call main(["add", "2", "3"]) directly
    argv = sys.argv[1:] if argv is None else argv
    return run(build_registry(), argv)