# ⚙️ Enable / Disable Fixy Auto‑Start

## 🚀 Enable (auto‑start at user log‑on)

To make **Fixy The Maintainer Tool** start automatically each time you log into Windows:

1. Run the script **`FixyTaskSchedulerManager.bat`** from **`tools`** folder, manually  
   (double‑click → 💻 **Will run the script**)


2. Choose the action **`1`**:
- **`1` → Enable Auto‑Start** – creates or updates the task **“Fixy Auto Launch”**
- **`2` → Disable Auto‑Start** – removes the Fixy task from Task Scheduler
- **`0` → Exit** – closes the menu

---

3. The script will create a scheduled task named:  
   👉 **Fixy Auto Launch**


4. At your next Windows log‑in, **Fixy** will launch automatically.  
   🔹 The main window will not show immediately – it will go straight to the **system tray**.  
   🔹 A small CMD window might flash briefly at startup – ✅ that’s normal! It’s only checking for updates.

---

## 🛑 Disable (stop auto‑start)

If you want to disable automatic startup:

1.  Run the script **`FixyTaskSchedulerManager.bat`** from **`tools`** folder, manually 
   (double‑click → 💻 **Will run the script**)


2. Choose the action **`2`**:
- **`1` → Enable Auto‑Start** – creates or updates the task **“Fixy Auto Launch”**
- **`2` → Disable Auto‑Start** – removes the Fixy task from Task Scheduler
- **`0` → Exit** – closes the menu


3. The scheduled task **Fixy Auto Launch** will be removed from Task Scheduler.

---


## 🧩 Quick commands (for power users)

| Action | Description | Script used |
|---------|--------------|-------------|
| 🔄 Enable Auto‑Start | Creates or updates Fixy Auto Launch task | `setup_fixy_task_scheduler.ps1` |
| ❌ Disable Auto‑Start | Deletes the Fixy Auto Launch task | `delete_fixy_task_scheduler.ps1` |
| 🧰 Interactive Menu | Lets you choose 1, 2 or 0 from CMD | `FixyTaskSchedulerManager.bat` |
---

✨ After activation, Fixy will:
- start automatically on Windows log‑on;  
- perform an update check;  
- remain hidden in the **system tray** (bottom‑right near the clock).

> ℹ️ That short CMD window you see at startup only checks for updates — the app will continue running quietly in the background.