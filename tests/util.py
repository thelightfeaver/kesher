import json

import psutil
from faker import Faker


def clean_state() -> None:
    with open("./state.json", "r") as f:
        state = json.load(f)

    pid = next(iter(state.values()), None)["pid"]

    if psutil.pid_exists(pid):
        p = psutil.Process(pid)
        p.terminate()
        p.wait(timeout=3)

    with open("./state.json", "w") as f:
        json.dump({}, f)


def read_state(path) -> any:
    with open(path, "r") as f:
        return json.load(f)


def generate_random_name() -> str:
    fake = Faker()
    return fake.word() + "_" + str(fake.random_number(digits=4, fix_len=True))


def read_log_file(log_path) -> str:
    with open(log_path, "r") as f:
        return f.read()
