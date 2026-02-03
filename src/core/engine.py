import os
from util.enviroment import Environment


def start(path: str) -> None:
    if path:
        env = Environment(path)
        if env.is_env:
            if env.api_type == "fastapi":
                os.system(f"fastapi run {path}")
            elif env.api_type == "flask":
                os.system(f"python3 {path}")
            elif env.api_type == "django":
                os.system(f"python3 {path} runserver")

            else:
                print("API type is unknown. Cannot start the application.")
        else:
            print("No virtual environment found in the specified path.")
    else:
        print("Please provide a valid path to start the application.")
