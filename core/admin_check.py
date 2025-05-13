import os
import sys
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    if not is_admin():
        print("[DEBUG] Relansăm cu admin...", flush=True)  # flush=True forțează afișarea

        # Obține calea absolută a scriptului curent
        script = os.path.abspath(sys.argv[0])

        # Pasează parametrul --admin
        params = " ".join([f'"{arg}"' for arg in sys.argv[1:]] + ["--admin"])

        # Rulează cu drepturi de admin
        ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            sys.executable,
            f'"{script}" {params}',
            None,
            1  # SW_SHOWNORMAL
        )
        sys.exit(0)  # Ieși imediat