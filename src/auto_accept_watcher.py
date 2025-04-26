from auto_accept_core import AutoAccept
import os
import subprocess
import time
import sys

def main():
    aa = AutoAccept()

    print("Auto-Accept Watcher started!")
    task_process = None
    task_path = task_path = os.path.join(os.path.dirname(sys.executable), 'auto_accept_task.exe')

    try:
        while True:
            if aa.league_running():
                if task_process is None or task_process.poll() is not None:
                    print("League opened. Starting AutoAcceptTask...")
                    try:
                        task_process = subprocess.Popen([task_path])
                    except Exception as e:
                        print(f"Error while starting AutoAcceptTask: {e}")
            else:
                if task_process is not None and task_process.poll() is None:
                    print("League closed. Quitting AutoAcceptTask...")
                    task_process.terminate()
                    task_process = None

            time.sleep(5)
    except KeyboardInterrupt:
        if task_process is not None and task_process.poll() is None:
            task_process.terminate()
        print("Auto-Accept Watcher exited.")

if __name__ == "__main__":
    main()