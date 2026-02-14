import enum

tecnology_extensions = (
    ".py",
    ".js",
    ".java",
    ".cpp",
    ".c",
    ".cs",
    ".rb",
    ".go",
    ".php",
    ".ts",
)


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
