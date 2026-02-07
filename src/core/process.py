"""Module for managing system processes."""

import json
import os
import subprocess

import psutil
from faker import Faker
from rich.console import Console
from rich.table import Table

from model.process import ProcessBase
from util.state import State


class Process:
    """Class to manage system processes."""

    def __init__(self) -> None:
        self.state = State()
        self._create_folder_log()

    def start(
        self, commands: list[str], name=str | None, auto_start=False, technology=None
    ) -> subprocess.Popen:
        """
        Execute a system command and return the running process.
        Args:
            commands (list[str]): The command and its arguments to execute.
            name (str | None): Optional name for the process.
            auto_start (bool): Flag to enable auto-start for the process.
        Returns:
            subprocess.Popen: The running process object.
        """
        temp_name = (
            name
            if name
            else Faker().word() + str(Faker().random_number(digits=5, fix_len=True))
        )
        with open(f".logs/{temp_name}.log", "a") as log:
            process = subprocess.Popen(
                commands,
                stdout=log,
                stderr=subprocess.STDOUT,
                stdin=subprocess.DEVNULL,
                cwd=".",
            )
        id = process.pid

        # TODO: CHECK IF CURRENT PROCESS IS RUNNING

        # Save information about process
        self.state.add(
            ProcessBase(
                pid=id,
                host=os.uname().nodename,
                name=temp_name,
                log=f".logs/{temp_name}.log",
                auto_start=auto_start,
                size=round(
                    psutil.Process(process.pid).memory_info().rss / 1024 / 1024, 1
                ),
                technology=technology,
                commands=commands,
                status="running",
            )
        )
        print(f"Process started with PID: {process.pid} and Name: {temp_name}")
        return process

    def stop(self, id: str) -> None:
        """
        stop a process by its PID.
        args:
            id (str): The PID of the process to stop.
        """
        data = self.state.search(id)
        if not data:
            print(f"No process found with PID {id}.")
            return

        # Select first records
        for pid, value in data.items():
            try:
                proc = psutil.Process(int(pid))
                proc.terminate()
                proc.wait(timeout=3)
                print(f"Process with PID {pid} has been stopped.")
                #  Update process status in state
                self.state.update(pid, "status", "stopped")
            except psutil.NoSuchProcess:
                self.state.update(pid, "status", "stopped")
                print(f"No process found with PID {pid}.")
            except psutil.TimeoutExpired:
                print(f"Process with PID {pid} did not stop in time; killing it.")
                proc.kill()
                self.state.update(pid, "status", "stopped")

    def status(self, id: str) -> None:
        """
        Get information about a specific process by its PID.
        Args:
            id (str): The PID of the process to retrieve information for.
        """
        data = self.state.search(id)
        if data is None:
            print(f"No process found with PID {id}.")
            return

        console = Console()
        table = Table(
            title="Process Information", show_header=True, header_style="bold magenta"
        )

        table.add_column("PID", style="cyan", justify="right")
        table.add_column("Name", style="green")
        table.add_column("Status", style="yellow")
        table.add_column("Auto Start", justify="center")
        table.add_column("Commands", style="blue")
        table.add_column("Memory (MB)", justify="right")
        table.add_column("Technology", style="magenta")
        for pid, info in data.items():
            status_color = "green" if info["status"] == "running" else "red"
            table.add_row(
                pid,
                info["name"],
                f"[{status_color}]{info['status']}[/{status_color}]",
                "✓" if info["auto_start"] else "✗",
                " ".join(info["commands"]),
                str(info["size"]),
                info["technology"] if info["technology"] else "N/A",
            )

        console.print(table)

    def _create_folder_log(self) -> None:
        """Create a log folder for the process."""
        log_folder = os.path.join(".logs")
        os.makedirs(log_folder, exist_ok=True)

    def log(self, id: str) -> None:
        """
        Retrieve and print the log of a specific process by its PID.
        Args:
            id (str): The PID of the process whose log is to be retrieved.
        """
        if id == "all":
            return

        # Get log path from state
        data = self.state.search(id)
        data = next(iter(data.values()), None)

        if data != {}:
            log_path = data.get("log")
            if log_path and os.path.exists(log_path):
                with open(log_path, "r") as log_file:
                    print(log_file.read().replace("None", ""))
            else:
                print(f"No log file found for process with PID {id}.")
        else:
            print(f"No process found with PID {id}.")

    def restart(self, id: str) -> None:
        """
        Restart a process by its PID.
        Args:
            id (str): The PID of the process to restart.
        """
        data = self.state.search(id)
        if data is None:
            print(f"No process found with PID {id}.")
            return

        if data:
            for key, value in data.items():
                if value["status"] == "running" and psutil.pid_exists(value["pid"]):
                    self.stop(key)

                self.start(
                    value["commands"],
                    value["name"],
                    value["auto_start"],
                    value["technology"],
                )
                self.state.delete(key)
                print(f"Process with PID {key} has been restarted.")
        else:
            print("No process will be restarted")

    def delete(self, id: str) -> None:
        """
        Delete a process entry by its PID.
        Args:
            id (str): The PID of the process to delete.
        """
        data = self.state.search(id)
        if data is None or data is {}:
            print(f"No process found with PID {id}.")
            return

        if data:
            for key, _ in data.items():
                if psutil.pid_exists(int(key)):
                    self.stop(key)
                self.state.delete(key)
                print(f"Process with PID {key} has been deleted from records.")
        else:
            print("No process will be deleted")
