from auto_accept_core import AutoAccept
import time

def main():
    print("Auto-Accept started! (Taskplaner mode)")
    aa = AutoAccept()

    if not aa.league_running():
        print("League Client not found. Quitting Auto-Accept.")
        return

    if not aa.creds():
        print("Couldn't connect to LCU. Quitting Auto-Accept.")
        return

    try:
        while aa.league_running():
            ready_check = aa.check_ready_check()

            if ready_check and ready_check.get("state") == "InProgress" and ready_check.get("playerResponse") == "None":
                print("Match found! Accepting...")
                aa.accept_ready_check()
                time.sleep(2)

            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Auto-Accept stopped.")

    print("League Client closed. Quitting Auto-Accept.")

if __name__ == "__main__":
    main()