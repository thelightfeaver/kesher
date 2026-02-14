import subprocess

from command import Command

from util import generate_random_name, read_state


def test_delete_process(python_venv):
    # Start a process
    app_name = generate_random_name()
    cmd = Command(python_venv)
    command_start = cmd.start(app_name)
    result = subprocess.run(command_start, capture_output=True, text=True, check=True)
    assert "Process started with PID" in result.stdout, (
        "CLI output did not confirm process start"
    )

    # Delete the process
    command_delete = cmd.delete(app_name)
    result = subprocess.run(command_delete, capture_output=True, text=True, check=True)
    assert "deleted" in result.stdout, "CLI output did not confirm process deletion"

    # Check if the process is removed from state
    state = read_state("./state.json")
    assert len(state) == 0, "Process was not removed from state after deletion"
