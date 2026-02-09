import subprocess

from command import Command

from util import generate_random_name, read_state


def test_status_process(python_venv):
    # Test that the process starts successfully
    app_name = generate_random_name()
    cmd = Command(python_venv)
    command = cmd.start(app_name)
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    assert "Process started with PID" in result.stdout, (
        "CLI output did not confirm process start"
    )

    state = read_state("./state.json")
    process_info = next(iter(state.values()), None)
    # Check the status of the process
    command_status = cmd.status(app_name)
    result = subprocess.run(command_status, capture_output=True, text=True, check=True)
    assert "running" in result.stdout, "CLI output did not confirm process is running"
    assert app_name in result.stdout, "CLI output did not include the process name"
    assert str(process_info["pid"]) in result.stdout, (
        "CLI output did not include the process PID"
    )
