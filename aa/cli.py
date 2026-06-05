from __future__ import annotations
import sys
from aa.registry import Registry, build_registry

def run(registry: Registry, argv: list[str]) -> int:
    if not argv or (command := registry.get(argv[0])) is None:
        print(f"Usage: aa {'|'.join(registry.names())}", file=sys.stderr)
        return 1
    command.execute()
    return 0

def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    return run(build_registry(), argv)