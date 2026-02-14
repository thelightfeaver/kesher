"""
Module for logging messages to a file.
"""


class Logger:
    """A simple logger class that writes log messages to a file."""

    def __init__(
        self,
    ):
        self._log_path = "log.txt"

    def register_log(self, text):
        """Registers a log entry by writing the provided text to a log file. If the log file already exists, it will be overwritten with the new text.

        Args:
            text (str): The log entry to be written to the log file.
        """

        with open(self._log_path, "a") as f:
            f.write(text)
            f.write("\n")
