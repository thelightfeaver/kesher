import enum

StyleColor = {
    "success": "green",
    "info": "blue",
    "warning": "yellow",
    "error": "red",
}


class MessageType(enum.Enum):
    SUCCESS = "success"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
