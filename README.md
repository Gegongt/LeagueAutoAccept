# League AutoAccept

> Automatically accepts queues in League of Legends as soon as they pop — fully automatic, running silently in the background.

---

## 💡 Project Overview

League AutoAccept is a lightweight tool that monitors the League of Legends client locally via the **LCU API** and automatically accepts queues.

**Features:**

- Auto-accept as soon as queue pops
- Fully local, no servers, no data sharing
- Automatic start at system boot (Windows Task Scheduler)
- Clean uninstallation: removes tasks, kills running processes
- Installer and Uninstaller included

**Version:** 1.0.0

---

## 🔧 Installation

**1. Download**

- Download the latest release installer from [GitHub Releases](https://github.com/Gegongt/LeagueAutoAccept/releases).

**2. Run**

- Launch the installer.
- League AutoAccept installs by default to `C:\Program Files\LeagueAutoAccept`.
- After installation, the watcher automatically starts silently in the background.

**3. Done!**

- As soon as you start League, AutoAccept is ready.
- When a queue pops, it will automatically be accepted.

---

## 📁 Project Structure

```plaintext
LeagueAutoAccept/
├── src/
│   ├── auto_accept_core.py
│   ├── auto_accept.py
│   ├── auto_accept_task.py
│   └── auto_accept_watcher.py
├── installer/
│   └── create_task.ps1
├── setup.iss
└── README.md
```

---

## 🔐 Security and Privacy

- ⚠️ **Only local access** to the League client.
- ⚠️ **No data sent** to any servers.
- ⚠️ **Uses official, public LCU API** — no memory reads, no packet sniffing.
- ✅ **Fully safe** regarding Riot's third-party tool policies.

---

## 🌟 Planned Features

- ✨ **Auto-Lock-In favorite champion** once champion select starts
- ✨ **Auto-rune change** based on selected champion
- ✨ **Auto-Select summoner spells** based on config files

---

## 👻 License

**MIT License** — Free to use

> "Built with passion for a smoother ranked grind with quick toilet breaks ;)."

---

# GLHF and good luck on the Rift! 🚀
