import json
import os
import sys


class Environment:
    ENVS = [
        "./venv",
        "./.venv",
        "./env",
    ]

    def __init__(self, path: str) -> None:
        self.is_env = self._is_enviroments_exists()
        self.api_type = self._determine_technology(path)
        self._save_data()

    def _save_data(self) -> None:
        data = {"environments": self.is_env, "api_type": self.api_type}
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

    def _is_enviroments_exists(self) -> bool:
        for env in self.ENVS:
            cwd = os.getcwd()
            full_path = os.path.join(cwd, env)
            if os.path.exists(full_path):
                return True
        return False

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
