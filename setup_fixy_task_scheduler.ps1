# ---------------------------------------------------------
# Fixy Auto-Start Task Creator (PowerShell)
# ---------------------------------------------------------

# Ensure script runs as Administrator

# Verify if is admin
$IsAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).
            IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $IsAdmin) {
    Write-Host "Not running as Administrator. Requesting elevation..."

    # Relansează scriptul cu drepturi de admin
    Start-Process -FilePath "powershell.exe" `
                  -ArgumentList "-ExecutionPolicy Bypass -File `"$PSCommandPath`"" `
                  -Verb RunAs
    # colse the actual instance
    exit
}

Write-Host "Running with Administrator privileges!"

# Name of task from Task Scheduler
$TaskName = "Fixy Auto Launch"

# Get auto path, this script should be in the same folder as the exe
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$FixyExe = Join-Path $ScriptDir "Fixy.exe"

# Arguments to open hidden
$Arguments = "--hidden"

Write-Host "Creating or updating scheduled task: $TaskName"
Write-Host "Executable path: $FixyExe"
Write-Host ""

# Check if the exe exist
if (-not (Test-Path $FixyExe)) {
    Write-Host "File not found: $FixyExe"
    Read-Host -Prompt "Press Enter to exit"
    exit 1
}

# Check if the task already exist
$existingTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existingTask) {
    Write-Host "Existing task found. Removing it..."
    Read-Host -Prompt "Press Enter to continue"
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

# Create the action, run fixy
$action = New-ScheduledTaskAction -Execute $FixyExe -Argument $Arguments

# Create the trigger, at log on
$trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME

# Set to run as Administrator
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -RunLevel Highest

# Description
$desc = "Automatically starts Fixy The Maintainer Tool at user log-on."

# Build and register the task
$task = New-ScheduledTask -Action $action -Trigger $trigger -Principal $principal -Description $desc

Register-ScheduledTask -TaskName $TaskName -InputObject $task -Force

Write-Host ""
Write-Host "Scheduled task '$TaskName' created successfully!"
Write-Host "Fixy will start automatically after log-in with admin rights."
Read-Host -Prompt "Press Enter to exit"