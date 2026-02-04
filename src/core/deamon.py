import asyncio
import os

import psutil
import uvloop
from process import Process


class Daemon:
    def __init__(self):
        self.process_manager = Process()

    async def monitor_processes(self):
        """Monitor all processes and print their status."""
        while True:
            for pid, info in self.process_manager.info_process.items():
                if psutil.pid_exists(int(pid)):
                    proc = psutil.Process(int(pid))
                    if (
                        not proc.is_running()
                        or proc.status() == psutil.STATUS_ZOMBIE
                        and info["auto_start"] == True
                    ):
                        print(
                            f"Process {info['name']} with PID {pid} has stopped. Restarting..."
                        )
                        self.process_manager.execute(
                            info["commands"],
                            name=info["name"],
                            auto_start=info["auto_start"],
                        )

            await asyncio.sleep(10)  # Monitor every 10 seconds

    def run(self):
        """Run the daemon to monitor processes."""
        uvloop.install()
        asyncio.run(self.monitor_processes())


if __name__ == "__main__":
    daemon = Daemon()
    daemon.run()
