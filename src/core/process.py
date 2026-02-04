"""Module for managing system processes."""

import os
import subprocess

import psutil


class Process:
    def __init__(self) -> None:
        pass

    def execute(self, commands: list[str]) -> subprocess.Popen:
        """Execute a system command and return the running process."""
        with open("process.log", "a") as log:
            process = subprocess.Popen(
                commands,
                stdout=log,
                stderr=subprocess.STDOUT,
                stdin=subprocess.DEVNULL,
                cwd=".",
            )

        print(f"Process started with PID: {process.pid}")
        return process
