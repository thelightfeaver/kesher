"""This module serves as the core of the application, providing essential classes and functions for process management and daemonization. It includes the Daemon class for running processes in the background, as well as functions for starting, stopping, restarting, and deleting processes. The Process class is also included for representing individual processes."""

from .entry import delete, restart, start, stop
from .process import Process

__all__ = ["Process", "start", "stop", "restart", "delete"]
