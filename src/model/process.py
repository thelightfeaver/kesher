"""This module defines the ProcessBase class, which serves as a base for process management."""

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
    start_time: str
    version_interpreter: str
