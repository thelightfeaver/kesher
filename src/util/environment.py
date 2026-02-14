import os
import sys

from util.const import tecnology_extensions


class Environment:
    ENVS = [
        "bin/python",
        "bin/python3",
        "scripts/python.exe",
    ]

    def __init__(self, file_path: str, venv: str | None = None) -> None:
        self.venv_path = self._get_environments_exists(venv)
        self.api_type = self._determine_technology(file_path)
        self.file_path = file_path if self.api_type else None

    def _get_environments_exists(self, venv: str | None = None) -> str:
        if not venv:
            return sys.executable

        else:
            for env in self.ENVS:
                env_path = os.path.join(venv, env)
                if os.path.exists(env_path):
                    return env_path
            return None

    def _determine_technology(self, file_path: str) -> str:
        if not file_path.endswith(tecnology_extensions):
            return None

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
