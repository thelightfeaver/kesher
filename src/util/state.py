"""Module for managing application state."""

import json
import os
from pprint import pprint

import psutil
from model.process import ProcessBase

class State:
    """Class to manage the state of processes."""
    def __init__(self):
        self._state_file = "state.json"
        self.processes: dict[str, ProcessBase] = {}
        self.load()

    def save(self):
        """
        Save the current state to a file.
        """
        with open(self._state_file, "w") as file:
            json.dump(self.processes, file, default=lambda o: o.__dict__, indent=4)

    def load(self):
        """
        Load the state from a file.
        """
        if os.path.exists(self._state_file):
            with open(self._state_file, "r") as file:
                self.processes = json.load(file)

    def search(self, key: str) -> dict[str, ProcessBase]:
        """
        Search for a specific key in the state.
        Args:
            key (str): The key to search for.
        Returns:
            The value associated with the key, or an empty dictionary if not found.
        """

        if key == "all":
            return self.processes.copy()

        for key, value in self.processes.items():
            if key == id or value.name == id:
                return dict({key: value})
        return {}

    def update(self, key: str, value: ProcessBase):
        """
        Update the state with a new key-value pair.
        Args:
            key (str): The key to update.
            value: The value to associate with the key.
        """
        self.processes[key] = value
        self.save()

    def delete(self, key: str):
        """
        Delete a key from the state.
        Args:
            key (str): The key to delete.
        """
        if key in self.processes:
            del self.processes[key]
            self.save()

    def add(self, value: ProcessBase):
        """
        Add a new ProcessBase instance to the state.
        Args:
            value (ProcessBase): The ProcessBase instance to add.
        """
        self.processes[str(value.pid)] = value
        self.save()


if __name__ == "__main__":
    state = State()
    for proc in psutil.process_iter(["pid", "name"]):
        process_info = ProcessBase(
            pid=proc.info["pid"],
            host=os.uname().nodename,
            name=proc.info["name"],
            log="",
            commands=[],
            auto_start=False,
            status="running",
            technology="",
            size=round(proc.memory_info().rss / 1024 / 1024, 1),
        )
        state.add(process_info)

    pprint(state.processes)
