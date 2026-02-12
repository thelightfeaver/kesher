from rich.console import Console
from rich.panel import Panel

from .const import MessageType, StyleColor


def show_message(
    message: str, title: str, message_type: MessageType = MessageType.SUCCESS
) -> None:
    """
    Display a message in a styled panel using Rich library.

    Args:
        message (str): The message to display.
        title (str): The title of the message panel.
        message_type (MessageType, optional): The type of message that determines the panel's border color. Defaults to MessageType.SUCCESS.
            - MessageType.SUCCESS: Green border for success messages
            - MessageType.ERROR: Red border for error messages
            - MessageType.INFO: Blue border for informational messages
            - MessageType.WARNING: Yellow border for warning messages
    """
    color = StyleColor[message_type.value]
    Console().print(
        Panel(
            f"{message}",
            title=f"[bold]{title}[/bold]",
            border_style=color,
            safe_box=True,
            expand=False,
        )
    )
