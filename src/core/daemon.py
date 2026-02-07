import asyncio

import psutil
import uvloop
from process import Process


class Daemon:
    def __init__(self):
        pass

    async def monitor_processes(self):
        """Monitor all processes and print their status."""
        while True:
            # Initialize Process manager
            process_manager = Process()
            processes = process_manager.state.processes.copy()

            # If there are no processes, wait and continue
            if not processes:
                print("No processes to monitor.")
                await asyncio.sleep(10)
                continue

            # Check each process status and restart if necessary
            for pid, info in processes.items():
                if not psutil.pid_exists(int(pid)) and bool(info["auto_start"]) == True:
                    print(
                        f"Process {info['name']} with PID {pid} has stopped. Restarting..."
                    )
                    process_manager.execute(
                        commands=info["commands"],
                        name=info["name"],
                        auto_start=info["auto_start"],
                        technology=info["technology"],
                    )
                    process_manager.state.delete(pid)
                # Check if process is stopped but is marked as running
                # TODO: IMPROVE THIS CHECK
                elif not psutil.pid_exists(int(pid)) and info["status"] == "running":
                    print(f"Process {info['name']} with PID {pid} has stopped.")
                    process_manager.state.delete(pid)
                    
                else:
                    print(f"Process {info['name']} with PID {pid} is running.")
                    continue

            await asyncio.sleep(10)  # Monitor every 10 seconds

    def run(self):
        """Run the daemon to monitor processes."""
        uvloop.install()
        asyncio.run(self.monitor_processes())


if __name__ == "__main__":
    daemon = Daemon()
    daemon.run()
