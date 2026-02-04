from util.enviroment import Environment

from .process import Process


def start(file_path: str, name=str | None, auto_start=False) -> None:
    env = Environment(file_path)
    if env.file_path:
        if env.venv_path:
            if env.api_type == "fastapi":
                Process().execute(
                    [f"{env.venv_path}", "-u", "-m", "fastapi", "dev", f"{file_path}"],
                    name=name,
                    auto_start=auto_start,
                )
            elif env.api_type == "flask":
                Process().execute(
                    [f"{env.venv_path}", "-u", f"{file_path}"],
                    name=name,
                    auto_start=auto_start,
                )
            elif env.api_type == "django":
                Process().execute(
                    [f"{env.venv_path}", "-u", f"{file_path}", "runserver"],
                    name=name,
                    auto_start=auto_start,
                )
            elif env.api_type == "general":
                Process().execute(
                    [f"{env.venv_path}", "-u", f"{file_path}"],
                    name=name,
                    auto_start=auto_start,
                )
            else:
                print("Path not recognized for starting the application.")
        else:
            print("No virtual environment found in the specified file_path.")
    else:
        print("Please provide a valid path to start the application.")


def stop(id: str) -> None:
    if "all" == id.lower():
        Process().stop_all()
    else:
        Process().stop(id)


def restart(id: str) -> None:
    Process().restart(id)


def status(id: str) -> None:
    Process().status(id)


def log(id: str) -> None:
    print(Process().log(id))


def delete(id: str) -> None:
    Process().delete(id)
