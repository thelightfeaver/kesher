import json
import os
import sys


class Environment:
    ENVS = [
        "venv/bin/python",
        "venv/bin/python3",
        ".venv/bin/python3",
        ".venv/bin/python",
    ]

    def __init__(self, path: str) -> None:
        self.venv_path = self._is_enviroments_exists()
        self.api_type = self._determine_technology(path)
        self._save_data()

    def _save_data(self) -> None:
        data = {"venv_path": self.venv_path, "api_type": self.api_type}
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

    def _is_enviroments_exists(self) -> bool:
        for env in self.ENVS:
            cwd = os.getcwd()
            full_path = os.path.join(cwd, env)
            if os.path.exists(full_path):
                return full_path

        return sys.executable

    def _determine_technology(self, path: str) -> str:
        with open(path, "r") as f:
            lines = f.read().lower()
            if "fastapi" in lines:
                return "fastapi"
            elif "flask" in lines:
                return "flask"
            elif "django" in lines:
                return "django"
            else:
                return "unknown"
