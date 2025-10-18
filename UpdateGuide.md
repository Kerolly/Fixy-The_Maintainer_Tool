# 🧭 Fixy – Update Guide

A short guide for **creating and publishing a Fixy update**  
*(Bootstrapper, Updater, and Main application)*

---

## 🏗️ 1. Build the Application

In your project terminal, run:

```bash
python setup.py build_exe
```

After the build completes, you’ll have this structure:

```
build/
  exe.win-amd64-3.x/
    Fixy.exe
    updater.exe
    bootstrapper.exe
    lib/
    assets/
```

---

## 📦 2. Create the Update Packages (.zip)

From `build/...`, take only the required files and create **three .zip archives**, one for each component.

💡 **Simple rule:**  
Each ZIP contains the executable + only the `lib/*` folders where changes were made.

### 🔧 Bootstrapper.zip

```
bootstrapper.exe
lib/       (# only modified folders)
 ├─ core/     
 └─ utils/
```

### ⚙️ Updater.zip

```
updater.exe
lib/
 ├─ core/
 └─ utils/
```

### 🧩 Fixy.zip

```
Fixy.exe
lib/
 ├─ core/
 └─ utils/
assets/
versions.json
```

---

## 🌐 3. Create a New Version on GitHub

1. Go to the **Releases** section.  
2. Create a new release:
   - **Tag:** `vX.Y.Z` (e.g., `v2.1.0`)
   - **Title:** `Fixy Update v2.1.0`
   - **Description:** short changelog
3. Attach:
   - `Fixy_APP_X.Y.Z.zip` *(full app)*  
   - plus separately: `Fixy.zip`, `Updater.zip`, `Bootstrapper.zip`

---

## 🧾 4. Update `versions.json`

In the `main` branch, update the versions and download URLs:

```json
{
  "fixy_version": "0.1.1",
  "fixy_zip_url": "https://github.com/Kerolly/Fixy-The_Maintainer_Tool/releases/download/v0.0.1/Fixy.zip",
  
  "updater_version": "2.1",
  "updater_zip_url": "https://github.com/Kerolly/Fixy-The_Maintainer_Tool/releases/download/v0.0.1/Updater.zip",
  
  "bootstrapper_version": "1.0",
  "bootstrapper_zip_url": "https://github.com/Kerolly/Fixy-The_Maintainer_Tool/releases/download/v0.0.1/Bootstrapper.zip"
}
```

🪄 **Tip:**  
If only one component changed, update **only its section**.

---

## 🔁 5. How the Update Flow Works

### 🧩 Bootstrapper.exe
- Reads the remote `versions.json`.  
- If an update for Updater is found, downloads and installs the corresponding ZIP.  
- Then launches `updater.exe`.

### ⚙️ Updater.exe
- Checks `versions.json` for the **Main** app and **bootstrapper**.  
- Closes `Fixy.exe`, downloads `Fixy.zip` / `Bootstrapper.zip`, and extracts updated files.  
- Updates the local `versions.json`.  
- Manual restart the main Fixy application.

---

## ✅ Release Checklist

| Step | Detail | Status |
|------|---------|--------|
| 🏗️ | Run `python setup.py build_exe` | ☐ |
| 📦 | Create ZIP files for each component | ☐ |
| 🧾 | Update `versions.json` (versions + URLs) -> GitHub | ☐ |
| 🌐 | Create a new GitHub release & attach files | ☐ |
| 🧪 | Test the full update on a clean system | ☐ |

---

## 💡 Useful Tips

- Always publish a **Fixy_APP_X.Y.Z.zip** for fresh installations.  

---

🛠️ *Fixy – The Maintainer Tool*  
© 2025 Fixy
