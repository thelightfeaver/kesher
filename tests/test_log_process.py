import os
import subprocess

from command import Command

from util import generate_random_name, read_log_file, read_state


def test_log_process(python_venv):
    # Start a process
    app_name = "test_process" + generate_random_name()
    cmd = Command(python_venv)
    command_start = cmd.start(app_name)
    result = subprocess.run(command_start, capture_output=True, text=True, check=True)
    assert "Process started with PID" in result.stdout, (
        "CLI output did not confirm process start"
    )

    # get the process info from state.json
    state = read_state("./state.json")
    process_info = next(iter(state.values()), None)

    # Log the process
    command_log = cmd.log(app_name)

    # Check that the log command returns output and that the log file exists
    result = subprocess.run(command_log, capture_output=True, text=True, check=True)
    assert result.stdout, "CLI output did not return any logs for the process"
    assert os.path.exists(process_info["log"]), (
        "Log file does not exist at the expected path"
    )
    log = read_log_file(process_info["log"])
    assert log, "Log file is empty, expected logs for the process"
