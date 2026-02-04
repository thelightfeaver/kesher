"""Module for managing system processes."""

import json
import os
import subprocess

import psutil


class Process:
    def __init__(self) -> None:
        self.info_process = self._load_data()

    def _load_data(self) -> dict:
        """Load process information from data.json file."""
        if os.path.exists("process.json"):
            with open("process.json", "r") as f:
                return json.load(f)
        return {}

    def _save_data(self) -> None:
        """Save process information to data.json file."""
        with open("process.json", "w") as f:
            json.dump(self.info_process, f, indent=4)

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

        data = {"pid": process.pid, "commands": commands, "status": "running"}
        self.info_process[str(process.pid)] = data
        self._save_data()

        print(f"Process started with PID: {process.pid}")
        return process

    def terminate(self, pid: int) -> None:
        """Terminate a process by its PID."""
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            proc.wait(timeout=3)
            print(f"Process with PID {pid} has been terminated.")
            self.info_process[str(pid)]["status"] = "terminated"
            self._save_data()
        except psutil.NoSuchProcess:
            print(f"No process found with PID {pid}.")
        except psutil.TimeoutExpired:
            print(f"Process with PID {pid} did not terminate in time; killing it.")
            proc.kill()
            self.info_process[str(pid)]["status"] = "terminated"
            self._save_data()
