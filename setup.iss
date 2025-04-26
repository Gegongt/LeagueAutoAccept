[Setup]
AppName=League AutoAccept
AppVersion=1.0.0
AppVerName=League AutoAccept
DefaultDirName={autopf}\LeagueAutoAccept
DefaultGroupName=League AutoAccept
UninstallDisplayIcon={app}\auto_accept_watcher.exe
OutputDir=dist
OutputBaseFilename=LeagueAutoAcceptInstaller
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64os

[Files]
Source: "dist\auto_accept_watcher.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\auto_accept_task.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\auto_accept.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "installer\create_task.ps1"; DestDir: "{app}"; Flags: ignoreversion

[Run]
Filename: "powershell.exe"; Parameters: "-ExecutionPolicy Bypass -File ""{app}\create_task.ps1"" -installPath ""{app}"""; StatusMsg: "Task schedule is being created..."; Flags: runhidden
Filename: "{app}\auto_accept_watcher.exe"; Description: "LeagueAutoAccept Watcher starten"; Flags: runhidden nowait skipifsilent

[UninstallRun]
Filename: "schtasks.exe"; Parameters: "/Delete /TN LeagueAutoAccept /F"; Flags: runhidden
Filename: "taskkill.exe"; Parameters: "/IM auto_accept_watcher.exe /F"; Flags: runhidden
Filename: "taskkill.exe"; Parameters: "/IM auto_accept_task.exe /F"; Flags: runhidden