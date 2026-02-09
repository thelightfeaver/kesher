"""This module defines the Command class"""


class Command:
    def __init__(self, python_venv):
        self._python_venv = python_venv
        self._kesher = "./src/main.py"
        self._app = "./app/app1.py"

    def start(self, app_name):
        """
        Returns the command to start a process with the given name.

        Args:
            app_name (str): The name of the process to start.
        Returns:
            list: The command to start the process.
        """
        command = [
            self._python_venv,
            self._kesher,
            "start",
            self._app,
            "--name",
            app_name,
            "--auto-start",
        ]
        return command

    def stop(self, app_name):
        """
        Returns the command to stop a specific process.

        Args:
            app_name (str): The name of the process to stop.
        Returns:
            list: The command to stop the process.
        """
        command = [
            self._python_venv,
            self._kesher,
            "stop",
            app_name,
        ]
        return command

    def status(self, app_name):
        """
        Returns the command to check the status of a specific process.

        Args:
            app_name (str): The name of the process to check the status for.
        Returns:
            list: The command to check the process status.
        """
        command = [
            self._python_venv,
            self._kesher,
            "status",
            app_name,
        ]
        return command

    def log(self, app_name):
        """
        Returns the command to view logs for a specific process.

        Args:
            app_name (str): The name of the process to view logs for.
        Returns:
            list: The command to view the process logs.
        """
        command = [
            self._python_venv,
            self._kesher,
            "log",
            app_name,
        ]
        return command

    def delete(self, app_name):
        """
        Returns the command to delete a specific process.

        Args:
            app_name (str): The name of the process to delete.
        Returns:
            list: The command to delete the process.
        """
        command = [
            self._python_venv,
            self._kesher,
            "delete",
            app_name,
        ]
        return command
