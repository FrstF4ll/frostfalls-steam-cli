import shutil, pathlib, os, requests


def check_dependencies():
    steam_client = True if shutil.which("steam") else False
    steam_cmd = True if shutil.which("steamcmd") else False
    success = "All dependencies installed"

    match (steam_client, steam_cmd):
        case (True, True):
            return success
        case (True, False):
            return "Steamcmd is missing, please install steamcmd"
        case (False, True):
            return "Steam client is missing, please install steam client"
        case (False, False):
            return """Missing dependencies, please install :
            - Steamcmd
            - Steam client (steam)
            """


def check_directory(path):
    p = pathlib.Path(path).expanduser()
    if not p.is_dir():
        return f"Path not found: {path}"
    if not os.access(p, os.W_OK):
        return f"Can't write in {path}"
    return "Path found, write permission confirmed."


def check_connectivity():
    steam = "https://store.steampowered.com"
    is_online = requests.get(steam)
    return (
        "Connection successful" if is_online else "Failed to connect to steam servers"
    )
