from util.enviroment import Environment

from .process import Process


def start(file_path: str) -> None:
    if file_path:
        env = Environment(file_path)
        if env.venv_path:
            if env.api_type == "fastapi":
                Process().execute(
                    [f"{env.venv_path}", "-u", "-m", "fastapi", "dev", f"{file_path}"]
                )
            elif env.api_type == "flask":
                Process().execute([f"{env.venv_path}", "-u", f"{file_path}"])
            elif env.api_type == "django":
                Process().execute(
                    [f"{env.venv_path}", "-u", f"{file_path}", "runserver"]
                )
            elif env.api_type == "unknown":
                Process().execute([f"{env.venv_path}", "-u", f"{file_path}"])
            else:
                print("API type is unknown. Cannot start the application.")
        else:
            print("No virtual environment found in the specified file_path.")
    else:
        print("Please provide a valid path to start the application.")
