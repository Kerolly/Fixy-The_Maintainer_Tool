import os
import sys
from ctypes import windll

def is_admin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(f"Eroare: {e}")
        return False

def run_as_admin():
    if not is_admin():
        print("Nu ai drepturi de admin. Relansăm scriptul...")
        script = os.path.abspath(sys.argv[0])
        params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
        windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, f'"{script}" {params}', None, 1
        )
        sys.exit(0)


if __name__ == "__main__":
    run_as_admin()
