from dataclasses import dataclass


@dataclass
class ProcessBase:
    """
    Base class for process management.
    """

    pid: int
    host: str
    name: str
    log: str
    commands: list[str]
    auto_start: bool
    status: str
    technology: str
    size: int
    status: str
