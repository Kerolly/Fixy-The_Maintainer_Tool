# ⚙️ Enable / Disable Fixy Auto‑Start

## 🚀 Enable (auto‑start at user log‑on)

To make **Fixy The Maintainer Tool** start automatically each time you log into Windows:

1. Run the script **`setup_fixy_task_scheduler.ps1`** manually  
   (right‑click → 💻 **Run with PowerShell**)

2. The script will create a scheduled task named:  
   👉 **Fixy Auto Launch**

3. On your next Windows log‑in, **Fixy** will launch automatically.  
   🔹 The main window will not show immediately – it will go straight to the **system tray**.  
   🔹 A small CMD window might flash briefly at startup – ✅ that’s normal! It’s only checking for updates.

---

## 🛑 Disable (stop auto‑start)

If you want to disable automatic startup:

1. Run the script **`delete_fixy_task_scheduler.ps1`**  
   (right‑click → 💻 **Run with PowerShell**)

2. The scheduled task **Fixy Auto Launch** will be removed from Task Scheduler.

---

## 🧩 Quick Summary

| Action | Script to run |
|---------|----------------|
| 🔄 Enable auto‑start | `setup_fixy_task_scheduler.ps1` |
| ❌ Disable auto‑start | `delete_fixy_task_scheduler.ps1` |
| ▶️ How to run | right‑click → **Run with PowerShell** |

---

✨ After activation, Fixy will:
- start automatically on Windows log‑on;  
- perform an update check;  
- remain hidden in the **system tray** (bottom‑right near the clock).

> ℹ️ That short CMD window you see at startup only checks for updates — the app will continue running quietly in the background.