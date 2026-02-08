import json
import subprocess
from random import randint

from command import Command

from util import clean_state


def test_stop_process(python_venv):
    # Start a process
    app_name = "test_process" + str(randint(1000, 9999))
    cmd = Command(python_venv)
    command_start = cmd.start(app_name)
    result = subprocess.run(command_start, capture_output=True, text=True, check=True)
    assert "Process started with PID" in result.stdout, (
        "CLI output did not confirm process start"
    )

    # Stop the process
    command_stop = cmd.stop(app_name)
    result = subprocess.run(command_stop, capture_output=True, text=True, check=True)
    assert "stopped." in result.stdout, "CLI output did not confirm process stop"

    with open("./state.json", "r") as f:
        state = json.load(f)
    process_info = next(iter(state.values()), None)
    assert process_info["status"] == "stopped", (
        "Process status is not 'stopped' after stopping the process"
    )

    # Clean up:
    clean_state(process_info["pid"])
