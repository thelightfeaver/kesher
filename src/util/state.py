"""Module for managing application state."""

import json
import os
from pprint import pprint

import psutil

from model.process import ProcessBase


class State:
    """Class to manage the state of processes."""

    def __init__(self):
        self.processes: dict[str, ProcessBase] = {}
        self._state_file = "state.json"
        self.load()

    def save(self):
        """
        Save the current state to a file.
        """
        with open(self._state_file, "w") as file:
            json.dump(self.processes, file, default=lambda o: o.__dict__, indent=4)
        self.load()

    def load(self):
        """
        Load the state from a file.
        """
        try:
            if os.path.exists(self._state_file):
                with open(self._state_file, "r") as file:
                    self.processes = json.load(file)
            else:
                self.processes = {}
        except json.JSONDecodeError:
            with open(self._state_file, "w") as file:
                json.dump(self.processes, indent=4)

    def search(self, key: str) -> dict[str, ProcessBase]:
        """
        Search for a specific key in the state.
        Args:
            key (str): The key to search for.
        Returns:
            The value associated with the key, or an empty dictionary if not found.
        """
        self.load()
        if key == "all":
            return self.processes.copy()

        for id, value in self.processes.items():
            if key == str(id) or value["name"] == key:
                return dict({key: value})

        print(f"Key: {key} not found in state.")
        return {}

    def update(self, key: str, field: str, value: str):
        """
        Update the state with a new key-value pair.
        Args:
            key (str): The key to update.
            value: The value to associate with the key.
        """

        if key in self.processes.keys():
            self.processes[key][field] = value
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
