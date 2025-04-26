__version__ = "1.0.0"

import requests
import urllib3
import base64
import time
import psutil

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class AutoAccept:
    def __init__(self):
        self.session = None
        self.port = None

    def find_lcu_credentials(self):
        for proc in psutil.process_iter(['name', 'cmdline']):
            if proc.info['name'] == 'LeagueClientUx.exe':
                cmdline = proc.info['cmdline']
                port = next((arg.split('=')[1] for arg in cmdline if '--app-port=' in arg), None)
                token = next((arg.split('=')[1] for arg in cmdline if '--remoting-auth-token=' in arg), None)
                return port, token
        return None, None

    def create_session(self, token):
        session = requests.Session()
        auth = base64.b64encode(f"riot:{token}".encode()).decode()
        session.headers.update({"Authorization": f"Basic {auth}"})
        return session

    def check_ready_check(self):
        try:
            response = self.session.get(f"https://127.0.0.1:{self.port}/lol-matchmaking/v1/ready-check", verify=False)
            if response.status_code == 200:
                return response.json()
        except Exception:
            pass
        return None

    def accept_ready_check(self):
        try:
            response = self.session.post(f"https://127.0.0.1:{self.port}/lol-matchmaking/v1/ready-check/accept", verify=False)
            if response.status_code == 204:
                print("Match accepted!")
        except Exception as e:
            print(f"Accept error: {e}")

    def league_running(self):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == 'LeagueClientUx.exe':
                return True
        return False

    def creds(self):
        port, token = self.find_lcu_credentials()
        if port and token:
            self.port = port
            self.session = self.create_session(token)
            return True
        return False
