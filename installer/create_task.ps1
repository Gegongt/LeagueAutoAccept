param(
    [string]$installPath
)

if (-not $installPath) {
    Write-Error "No installationspath given!"
    exit 1
}

$watcherPath = Join-Path $installPath "auto_accept_watcher.exe"

if (Get-ScheduledTask -TaskName "LeagueAutoAccept" -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName "LeagueAutoAccept" -Confirm:$false
}

$Action = New-ScheduledTaskAction -Execute $watcherPath

$Trigger = New-ScheduledTaskTrigger -AtLogOn

$Principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -RunLevel Highest

$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Hours 12)

Register-ScheduledTask -TaskName "LeagueAutoAccept" -Action $Action -Trigger $Trigger -Principal $Principal -Settings $Settings -Force