import json

import psutil


def clean_state(pid: int):
    if psutil.pid_exists(pid):
        p = psutil.Process(pid)
        p.terminate()
        p.wait(timeout=3)
    with open("./state.json", "w") as f:
        json.dump({}, f)
