import subprocess

from command import Command

from util import generate_random_name, read_state


def test_start_process(python_venv):
    # Test that the process starts successfully
    app_name = generate_random_name()
    cmd = Command(python_venv)
    command = cmd.start(app_name)
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    state = read_state("./state.json")
    process_info = next(iter(state.values()), None)
    assert "Process started with PID" in result.stdout, (
        "CLI output did not confirm process start"
    )
    assert app_name in result.stdout, "CLI output did not include the process name"
    assert app_name == process_info["name"], "Process haven't started successfully"
