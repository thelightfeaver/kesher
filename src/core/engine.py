from util.enviroment import Environment

from .process import Process


def start(file_path: str, name=str | None, auto_start=False) -> None:
    env = Environment(file_path)
    if not env.file_path:
        print("The specified file does not exist.")
        return 
    
    if env.venv_path:
        if env.api_type == "fastapi":
            commands = [f"{env.venv_path}", "-u", "-m", "fastapi", "dev", f"{file_path}"]
        elif env.api_type == "flask":
            commands = [f"{env.venv_path}", "-u", f"{file_path}"]
        elif env.api_type == "django":
            commands = [f"{env.venv_path}", "-u", f"{file_path}", "runserver"]
        elif env.api_type == "general":
            commands =    [f"{env.venv_path}", "-u", f"{file_path}"],
              
        Process().execute(
            commands=commands
            name=name,
            auto_start=auto_start,
            technology=env.api_type,
        )    
           
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
