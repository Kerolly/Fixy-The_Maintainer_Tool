# ---------------------------------------------------------
# Deleting Fixy Auto-Start Task (PowerShell)
# ---------------------------------------------------------

# Ensure script runs as Administrator

# Verify if is admin
$IsAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).
            IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $IsAdmin) {
    Write-Host "Not running as Administrator. Requesting elevation..."

    # Relaunch script with admin
    Start-Process -FilePath "powershell.exe" `
                  -ArgumentList "-ExecutionPolicy Bypass -File `"$PSCommandPath`"" `
                  -Verb RunAs
    # colse the actual instance
    exit
}

Write-Host "Running with Administrator privileges!"

$TaskName = "Fixy Auto Launch"
Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
Write-Host "Task '$TaskName' removed."