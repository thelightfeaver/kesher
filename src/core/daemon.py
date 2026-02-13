"""Daemon class to monitor and manage processes."""

import asyncio
import os
import sys

import psutil
import uvloop

from core.process import Process

# TODO: CHANGE WAY HOW ADD PROCESS BECAUSE I DONT LIKE WAY I DO
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Daemon:
    def __init__(self):
        pass

    async def monitor_processes(self):
        """Monitor all processes and print their status."""
        while True:
            # Initialize Process manager
            process_manager = Process()
            processes = process_manager.state.search("all")

            # If there are no processes, wait and continue
            if not processes:
                print("No processes to monitor.")
                await asyncio.sleep(1)
                continue

            # Check each process status and restart if necessary
            for pid, info in processes.items():
                if (
                    psutil.pid_exists(int(pid))
                    and psutil.Process(int(pid)).is_running()
                ):
                    print(f"Process {info['name']} with PID {pid} is running.")
                elif not psutil.pid_exists(int(pid)) and bool(info["auto_start"]):
                    print(
                        f"Process {info['name']} with PID {pid} has stopped. Restarting..."
                    )
                    process_manager.start(
                        commands=info["commands"],
                        name=info["name"],
                        auto_start=info["auto_start"],
                        technology=info["technology"],
                    )
                    process_manager.state.delete(pid)

                elif not psutil.pid_exists(int(pid)) and info["status"] == "running":
                    print(
                        f"Process {info['name']} with PID {pid} has stopped. Auto-start is disabled."
                    )
                    process_manager.state.delete(pid)

            await asyncio.sleep(1)

    def run(self):
        """Run the daemon to monitor processes."""
        uvloop.install()
        asyncio.run(self.monitor_processes())


if __name__ == "__main__":
    daemon = Daemon()
    daemon.run()
