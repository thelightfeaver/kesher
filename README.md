# Kesher - Process Manager

## Features
- 📊 Monitor processes
- ▶️ Start and stop processes
- 📋 View process status
- 📝 Log management
- ⚙️ Auto-start configuration
- 🖥️ Interactive monitor interface

## Installation

```bash
uv venv
source .venv/bin/activate
uv pip install .
```

## Commands

### Start a process

```bash
kesher start <path> [--name NAME] [--auto-start]
```

Options:
- `--name`: Custom name for the process
- `--auto-start`: Enable auto-start for the process

### Stop a process

```bash
kesher stop <id | name | all>
```

### Check process status

```bash
kesher status <id | name | all>
```

### View process logs

```bash
kesher log <id | name>
```

### Restart a process

```bash
kesher restart <id | name | all>
```
### Interactive monitor

```bash
WIP ⚠️
kesher monitor
```

Launches an interactive TUI to manage all processes.

## Usage Examples

```bash
# Start a Python script with auto-start enabled
kesher start /path/to/script.py --name my-app --auto-start

# Stop a process by ID
kesher stop my-app

# Check status
kesher status my-app

# View logs
kesher log my-app

# Open interactive monitor
kesher monitor
```
