from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.widgets import DataTable, Footer, Header, Log

from core.process import Process


class KesherTUI(App):
    CSS = """
    DataTable {
        height: 1fr;
    }

    #process-table {
        border: solid $primary;
    }

    #log-view {
        height: 30%;
        border: solid $primary;
    }

    #resource-container {
        height: 20%;
        border: solid $primary;
    }
    """

    BINDINGS = [
        Binding(key="s", action="stop", description="Stop"),
        Binding(key="r", action="restart", description="Restart"),
        Binding(key="d", action="delete", description="Delete"),
        Binding(key="f", action="refresh", description="Refresh"),
        Binding(key="q", action="quit", description="Quit"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.process_manager = Process()
        self.selected_pid: str | None = None

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            DataTable(id="process-table", cursor_type="row"),
            id="main-container",
            markup=True,
        )
        yield Log(id="log-view", highlight=True)
        yield Container(
            DataTable(id="resource-table", cursor_type="line"),
            id="resource-container",
            markup=True,
        )
        yield Footer(show_command_palette=False, compact=True)

    def on_mount(self) -> None:
        self.title = "Kesher - Process Manager"
        self.sub_title = "Monitoring Application Processes"

        table = self.query_one("#process-table", DataTable)
        table.add_columns(
            "PID",
            "Name",
            "Status",
            "Auto Start",
            "Technology",
            "Memory (MB)",
        )
        self.load_processes()

        resource_table = self.query_one("#resource-table", DataTable)
        resource_table.add_columns("Key", "Value")

        self.load_resource()

        self.set_interval(
            interval=1,
            callback=self.load_log,
            name="log_refresh",
        )

        self.set_interval(
            interval=0.1,
            callback=self.load_resource,
            name="resource_refresh",
        )

    def load_processes(self) -> None:
        """Load and display all processes in the table."""
        process_table = self.query_one("#process-table", DataTable)
        process_table.clear()

        all_processes = self.process_manager.state.search("all")
        if not all_processes:
            return

        for pid, info in all_processes.items():
            status_style = "green" if info["status"] == "running" else "red"
            process_table.add_row(
                str(pid),
                info["name"],
                f"[{status_style}]{info['status']}[/{status_style}]",
                "Y" if info["auto_start"] else "N",
                info.get("technology", "N/A") or "N/A",
                str(info["size"]),
                key=str(pid),
            )

        self.query_one("#log-view", Log).clear()
        self.selected_pid = None

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        """Track selected PID for actions."""
        self.selected_pid = event.row_key.value

    def _ensure_selected(self) -> bool:
        if self.selected_pid:
            return True
        return False

    def action_stop(self) -> None:
        """Stop the selected process."""
        if not self._ensure_selected():
            return
        self.process_manager.stop(self.selected_pid)
        self.load_processes()
        self.notify(f"Process {self.selected_pid} stopped")

    def action_restart(self) -> None:
        """Restart the selected process."""
        if not self._ensure_selected():
            return
        self.process_manager.restart(self.selected_pid)
        self.load_processes()
        self.notify(f"Process {self.selected_pid} restarted")

    def load_log(self) -> None:
        """Show log for the selected process."""

        # Ensure a process is selected before attempting to show logs
        if not self._ensure_selected():
            return

        data = self.process_manager.state.search(self.selected_pid)
        data = next(iter(data.values()), None)

        if data is not None:
            log_widget = self.query_one("#log-view", Log)
            log_widget.clear()
            with open(data.get("log"), "r") as log_file:
                log_content = log_file.read().replace("None", "")
                log_widget.write(log_content)

    def action_refresh(self) -> None:
        """Manually refresh the process list."""
        self.load_processes()
        self.notify("Process list refreshed", timeout=0.2)

    def action_delete(self) -> None:
        """Delete the selected process."""
        if not self._ensure_selected():
            return
        self.process_manager.delete(self.selected_pid)
        self.load_processes()
        self.notify(f"Process {self.selected_pid} deleted")

    def load_resource(self) -> None:
        """Load and display resource usage for the selected process."""
        resource_table = self.query_one("#resource-table", DataTable)
        resource_table.clear()

        for key, value in self.process_manager.get_resources().items():
            resource_table.add_row(key, str(value))
