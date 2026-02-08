"""Module for managing system processes."""

import os
import subprocess
from datetime import datetime

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
    ) -> None:
        """
        Execute a system command and return the running process.
        Args:
            commands (list[str]): The command and its arguments to execute.
            name (str | None): Optional name for the process.
            auto_start (bool): Flag to enable auto-start for the process.
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
                start_time=datetime.fromtimestamp(
                    psutil.Process(process.pid).create_time()
                ).strftime("%Y-%m-%d %H:%M:%S"),
                version_interpreter=str(
                    subprocess.check_output([commands[0], "--version"]).decode().strip()
                ),
            )
        )
        print(f"Process started with PID: {process.pid} and Name: {temp_name}")

    def stop(self, id: str) -> None:
        """
        stop a process by its PID.
        args:
            id (str): The PID of the process to stop.
        """
        data = self.state.search(id)
        if data == {}:
            print(f"No process found with PID {id}.")
            return

        for pid, _ in data.items():
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
        if data == {}:
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
        for pid, value in data.items():
            status_color = "green" if value["status"] == "running" else "red"
            table.add_row(
                pid,
                value["name"],
                f"[{status_color}]{value['status']}[/{status_color}]",
                "✓" if value["auto_start"] else "✗",
                " ".join(value["commands"]),
                str(value["size"]),
                value["technology"] if value["technology"] else "N/A",
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
        if data == {}:
            return

        data = next(iter(data.values()), None)

        log_path = data.get("log")
        if log_path and os.path.exists(log_path):
            with open(log_path, "r") as log_file:
                print(log_file.read().replace("None", ""))
        else:
            print("No log file found.")

    def restart(self, id: str) -> None:
        """
        Restart a process by its PID.
        Args:
            id (str): The PID of the process to restart.
        """
        data = self.state.search(id)
        if data == {}:
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
        if data == {}:
            print("No process found for deletion.")
            return

        if data:
            for key, _ in data.items():
                if psutil.pid_exists(int(key)):
                    self.stop(key)
                self.state.delete(key)
                print(f"Process with PID {key} has been deleted from records.")
        else:
            print("No process will be deleted")

    def get_resources(self) -> dict:
        """Get current system resource usage.

        Returns:
            dict: A dictionary containing CPU usage, CPU count, total RAM, used RAM, and RAM usage percentage.
                keys:
                    - cpu_usage (float): Current CPU usage percentage.
                    - cpu_count (int): Total number of logical CPU cores.
                    - total_ram_gb (float): Total RAM in gigabytes.
                    - used_ram_gb (float): Used RAM in gigabytes.
                    - ram_usage_percent (float): Current RAM usage percentage.
        """
        # --- CPU Information ---
        cpu_usage = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count(logical=True)

        # --- RAM Information ---
        ram = psutil.virtual_memory()
        total_ram_gb = round(ram.total / (1024**3), 2)
        used_ram_gb = round(ram.used / (1024**3), 2)

        return {
            "CPU Usage": str(cpu_usage) + "%",
            "CPU Cores": cpu_count,
            "RAM": str(used_ram_gb) + " /" + str(total_ram_gb) + " GB",
        }
