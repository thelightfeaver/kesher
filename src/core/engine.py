"""This module defines the core engine for managing processes based on the environment configuration."""

from util.console import show_message
from util.const import MessageType
from util.environment import Environment

from .process import Process


def start(file_path: str, name=str | None, auto_start=False, venv=str | None) -> None:
    env = Environment(file_path, venv)
    if not env.file_path:
        show_message(
            "The specified file does not exist.",
            title="Error",
            message_type=MessageType.ERROR,
        )
        return

    if not env.venv_path:
        show_message(
            "The specified virtual environment does not exist.",
            title="Error",
            message_type=MessageType.ERROR,
        )
        return

    if env.api_type == "fastapi":
        commands = [
            f"{env.venv_path}",
            "-u",
            "-m",
            "fastapi",
            "run",
            f"{file_path}",
        ]
    elif env.api_type == "flask":
        commands = [f"{env.venv_path}", "-u", f"{file_path}"]
    elif env.api_type == "django":
        commands = [f"{env.venv_path}", "-u", f"{file_path}", "runserver"]
    elif env.api_type == "general":
        commands = ([f"{env.venv_path}", "-u", f"{file_path}"],)
    Process().start(
        commands=commands,
        name=name,
        auto_start=auto_start,
        technology=env.api_type,
    )


def stop(id: str) -> None:
    Process().stop(id)


def restart(id: str) -> None:
    Process().restart(id)


def status(id: str) -> None:
    Process().status(id)


def log(id: str) -> None:
    Process().log(id)


def delete(id: str) -> None:
    Process().delete(id)
