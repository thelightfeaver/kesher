"""Module for managing system processes."""

import json
import os
import subprocess

import psutil
from faker import Faker
from rich.console import Console
from rich.table import Table


class Process:
    def __init__(self) -> None:
        self.info_process = self._load_data()
        self._update_info_process()
        self._create_folder_log()

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

    def execute(
        self, commands: list[str], name=str | None, auto_start=False
    ) -> subprocess.Popen:
        """Execute a system command and return the running process.
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

        data = {
            "pid": process.pid,
            "host": os.uname().nodename,
            "name": temp_name,
            "log": f".logs/{temp_name}.log",
            "auto_start": auto_start,
            "size": round(psutil.Process(process.pid).memory_info().rss / 1024 / 1024, 1),
            "commands": commands,
            "status": "running",
        }
        self.info_process[str(process.pid)] = data
        self._save_data()

        print(f"Process started with PID: {process.pid} and Name: {temp_name}")
        return process

    def terminate(self, pid: str) -> None:
        """Terminate a process by its PID."""
        data = self._get_process_info(str(pid))
        if data is None:
            print(f"No process found with PID {pid}.")
            return

        try:
            proc = psutil.Process(data["pid"])
            proc.terminate()
            proc.wait(timeout=3)
            print(f"Process with PID {data['pid']} has been terminated.")
            if pid in self.info_process:
                self.info_process[pid]["status"] = "terminated"
                self._save_data()
        except psutil.NoSuchProcess:
            print(f"No process found with PID {data['pid']}.")
        except psutil.TimeoutExpired:
            print(
                f"Process with PID {data['pid']} did not terminate in time; killing it."
            )
            proc.kill()
            if pid in self.info_process:
                self.info_process[pid]["status"] = "terminated"
                self._save_data()

    def _update_info_process(self) -> None:
        """Update the status of all tracked processes."""
        for pid_str, info in list(self.info_process.items()):
            pid = int(pid_str)
            if psutil.pid_exists(pid):
                proc = psutil.Process(pid)
                if proc.is_running():
                    info["status"] = "running"
                else:
                    info["status"] = "stopped"
            else:
                del self.info_process[pid_str]
        self._save_data()

    def get_process_info(self, pid: str) -> None:
        """Get information about a specific process by its PID.
        Args:
            pid (int): The PID of the process to retrieve information for.
        Returns:
            dict | None: A dictionary containing process information or None if not found.
        """
        data = self._get_process_info(pid)
        if data is None:
            print(f"No process found with PID {pid}.")
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

        for pid, info in self.info_process.items():
            status_color = "green" if info["status"] == "running" else "red"
            table.add_row(
                pid,
                info["name"],
                f"[{status_color}]{info['status']}[/{status_color}]",
                "✓" if info["auto_start"] else "✗",
                " ".join(info["commands"]),
                str(info["size"]),
            )

        console.print(table)

    def _create_folder_log(self) -> None:
        """Create a log folder for the process."""
        log_folder = os.path.join(".logs")
        os.makedirs(log_folder, exist_ok=True)

    def terminate_all_processes(self):
        """Terminate all running processes tracked in info_process."""
        if self.info_process:
            for pid_str in list(self.info_process.keys()):
                pid = int(pid_str)
                self.terminate(pid)
        else:
            print("There are no processes to terminate.")

    def log(self, id: str) -> None:
        """Retrieve and print the log of a specific process by its PID.
        Args:
            id (str): The PID of the process whose log is to be retrieved.
        """
        process_info = self._get_process_info(id)
        if process_info is None:
            print(f"No process found with PID {id}.")
            return

        if process_info:
            log_path = process_info.get("log")
            if log_path and os.path.exists(log_path):
                with open(log_path, "r") as log_file:
                    print(log_file.read().replace("None", ""))
            else:
                print(f"No log file found for process with PID {id}.")
        else:
            print(f"No process found with PID {id}.")

    def _get_process_info(self, pid: str) -> dict | None:
        """Get information about a specific process by its PID.
        Args:
            pid (int): The PID of the process to retrieve information for.
        Returns:
            dict | None: A dictionary containing process information or None if not found.
        """

        for key, value in self.info_process.items():
            if key == pid or value["name"] == pid:
                return value
        return None
