# 🛠️ Fixy — The Maintainer Tool

Fixy is a lightweight Windows maintenance utility focused on being reliable, self‑updatable, and easy to distribute.
Current release implements the Hosts Block module and the full update/bootstrapping pipeline. Additional modules will be added incrementally.

**Status:** functional core (self‑update, tray mode, installer/portable). Features expand over time.

---

## 🚀 Key features (current)

- **Hosts Block**
  - Applies a curated blocklist to the Windows hosts file.
  - Creates a safe backup before any change and can restore on demand, manually.
  - Requires administrator privileges to modify the system hosts file.
- **Self‑update pipeline**
  - Bootstrapper checks and updates Updater.
  - Updater checks and updates Main and, if needed, updates Bootstrapper (downloads release assets from GitHub).
  - Robust file replacement with the shutdown of Fixy and manual restart.
- **Tray mode and optional auto‑start**
  - Runs quietly in the system tray.
  - Optional Task Scheduler entry (“`Fixy Auto Launch`”) to start at user log‑on.
- **Logging**
  - Structured logs for troubleshooting (app, update flow, errors).

### 🗺️ Planned (roadmap)

- UI for additional maintenance tools.
- Rich Updater UI.
- More modules (System Clean, Maintenance).

---

## 💻 System requirements

- Windows 10/11 (64‑bit)
- Administrator rights
- Internet access for update checks and downloads

---

## 📦 Download and install

There are two ways to get Fixy:

### 1) Installer (recommended for fresh installs)

- Download `FixyTheMaintainerTool_SETUP_X.Y.Z.exe` from the GitHub Releases page.
- Run the installer (UAC prompt is expected).
- (Optional) Enabled “auto‑start at log‑on” during setup; a scheduled task will be created.

### 2) Portable ZIP (for direct updates or portable usage)

- Download `Fixy_APP_X.Y.Z.zip`.
- Unzip into your desired application folder (e.g., `C:\Program Files\FixyTheMaintainerTool`).
- (Optional) To enable auto‑start, run `tools\FixyTaskSchedulerManager.bat` (Run as Administrator) and choose Create/Update task.

Release assets are published on the repository’s Releases page:
- Setup: `FixyTheMaintainerTool_SETUP_X.Y.Z.exe`
- Portable: `Fixy_APP_X.Y.Z.zip`

---

## 🔄 How updates work

- On start, Bootstrapper verifies if a newer Updater is available; if yes, it updates it first.
- Updater checks the online `versions.json` hosted in the repository (GitHub) and, if a new Main version is available, downloads and installs it, and so on for BootstBrapper.
- Fixy (manually) restarts with the new binaries.

> **Notes**
> - Updates are fetched over HTTPS.
> - A short console window may flash during update checks—this is expected.

---

## 🛡️ Hosts Block (current module)

### What it does

- Writes a blocklist of domains to the system hosts file:
  `C:\Windows\System32\drivers\etc\hosts`

### Safety

- Fixy creates a backup of the hosts file before any change.
- You can restore the previous state if needed.

### Requirements

- Run as Administrator (hosts is protected by the OS).
- Some antivirus products may prompt during first run; allow the action.

### Advanced

- The blocklist source file (for advanced users) is included with the app (e.g., `/blocked_sites.txt`). You may extend it if you understand the implications.

> **Disclaimer**
> - Modifying the hosts file affects name resolution system‑wide. Apply lists you trust and always keep a backup.

---

## ⏱️ Tray behavior and auto‑start

- Fixy can minimize to the system tray and run in the background.
- Optional auto‑start is implemented via a scheduled task named “`Fixy Auto Launch`”.
- **Manage auto‑start:**
  - Installer: choose the checkbox during setup (is selected by default).
  - Portable: run `tools\FixyTaskSchedulerManager.bat` (Run as Administrator) and use the interactive menu to create or delete the task.

---

## ♻️ Uninstall

### 1) Uninstall from the installer setup:

- Use Windows “Apps & Features” (Settings) or the uninstaller in the installation folder.
- The uninstaller stops Fixy (even if it’s in the tray) and removes the entire installation directory.
- If auto‑start was enabled, the scheduled task is removed.

### 2) Uninstall from zip setup:

- Uninstall manually the portable folder.

---

## ⚙️ Troubleshooting

- **“Update didn’t trigger”**
  - Ensure internet access; try running Fixy as Administrator.
  - Verify that the online `versions.json` points to the latest release asset.
- **“Hosts change failed”**
  - Run as Administrator; confirm that the hosts file is not locked by another process.
- **Logs**
  - Check the logging folder inside the application directory for diagnostic details.

---

## 🔒 Security and privacy

- Fixy does not collect personal data.
- Network activity is limited to update checks and downloads from official release sources (e.g., GitHub Releases).
- Editing the hosts file requires elevated permissions; Fixy requests or runs with Administrator rights for these actions.

---

## 📄 License

MIT License. See the `LICENSE` file for details.

---

## 🆘 Support

- Issues and feature requests: use the repository’s Issues page.
- For critical problems, attach the relevant log files and describe the steps to reproduce.
