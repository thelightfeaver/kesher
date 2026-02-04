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
        # TODO: FIX ERROR WHEN FILE NOT HAVE CORRECT JSON FORMAT
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
        data = {
            "pid": id,
            "host": os.uname().nodename,
            "name": temp_name,
            "log": f".logs/{temp_name}.log",
            "auto_start": auto_start,
            "size": round(
                psutil.Process(process.pid).memory_info().rss / 1024 / 1024, 1
            ),
            "commands": commands,
            "status": "running",
        }
        self.info_process[str(id)] = data
        self._save_data()

        print(f"Process started with PID: {process.pid} and Name: {temp_name}")
        return process

    def stop(self, id: str) -> None:
        """
        stop a process by its PID.
        args:
            id (str): The PID of the process to stop.
        """
        data = self._get_process_info(str(id))
        if data is None:
            print(f"No process found with PID {id}.")
            return
        pid = next(iter(data.values()))["pid"]
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            proc.wait(timeout=3)
            print(f"Process with PID {pid} has been stopped.")
            if pid in self.info_process:
                self.info_process[f"{pid}"]["status"] = "stopped"
                self._save_data()
        except psutil.NoSuchProcess:
            print(f"No process found with PID {pid}.")
        except psutil.TimeoutExpired:
            print(f"Process with PID {pid} did not stop in time; killing it.")
            proc.kill()
            if pid in self.info_process:
                self.info_process[f"{pid}"]["status"] = "stopped"
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
        self._save_data()

    def status(self, id: str) -> None:
        """
        Get information about a specific process by its PID.
        Args:
            id (str): The PID of the process to retrieve information for.
        """
        data = self._get_process_info(id)
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
        for pid, info in data.items():
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

    def stop_all(self):
        """
        Stop all running processes tracked in info_process."""
        if self.info_process:
            for pid in list(self.info_process.keys()):
                self.stop(int(pid))
        else:
            print("There are no processes to stop.")

    def log(self, id: str) -> None:
        """
        Retrieve and print the log of a specific process by its PID.
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

    def _get_process_info(self, id: str) -> dict | None:
        """
        Get information about a specific process by its PID.
        Args:
            id (str): The PID of the process to retrieve information for.
        Returns:
            dict | None: A dictionary containing process information or None if not found.
        """
        
        if id:
            if id == "all":
                return self.info_process.copy()

            for key, value in self.info_process.items():
                if key == id or value["name"] == id:
                    return dict({key: value})
        return None

    def restart(self, id: str) -> None:
        pass

    def delete(self, id: str) -> None:
        """
        Delete a process entry by its PID.
        Args:
            id (str): The PID of the process to delete.
        """
        data = self._get_process_info(id)
        if data is None or data is {}:
            print(f"No process found with PID {id}.")
            return

        if data:
            for key, value in data.items() :
                if psutil.pid_exists(int(key)):
                    self.stop(key)
                del self.info_process[key]
                print(f"Process with PID {key} has been deleted from records.")
        else:
            print("No process will be deleted")
        self._save_data()
