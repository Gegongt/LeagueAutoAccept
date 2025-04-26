from auto_accept_core import AutoAccept
import time

def main():
    print("Auto-Accept started! (Strg+C to quit)")
    aa = AutoAccept()
    
    try:
        while True:
            if not aa.league_running():
                print("League Client not found. Waiting...")
                aa.session = None
                aa.port = None
                time.sleep(5)
                continue

            if aa.session is None:
                if not aa.creds():
                    time.sleep(2)
                    continue

            ready_check = aa.check_ready_check()
            print("Waiting for match...")

            if ready_check and ready_check.get("state") == "InProgress" and ready_check.get("playerResponse") == "None":
                print("Match found! Accepting...")
                aa.accept_ready_check()
                time.sleep(2)

            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nAuto-Accept stopped.")
    

if __name__ == "__main__":
    main()