import os
import sys


class Environment:
    ENVS = [
        "venv/bin/python",
        "venv/bin/python3",
        ".venv/bin/python3",
        ".venv/bin/python",
    ]

    def __init__(self, file_path: str) -> None:
        self.venv_path = self._get_enviroments_exists()
        self.api_type = self._determine_technology(file_path)
        self.file_path = None if self.api_type == None else file_path

    def _get_enviroments_exists(self) -> str:
        for env in self.ENVS:
            cwd = os.getcwd()
            full_path = os.path.join(cwd, env)
            if os.path.exists(full_path):
                return full_path

        return sys.executable

    def _determine_technology(self, file_path: str) -> str:
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                lines = f.read().lower()
                if "fastapi" in lines:
                    return "fastapi"
                elif "flask" in lines:
                    return "flask"
                elif "django" in lines:
                    return "django"
                else:
                    return "general"
        else:
            return None
