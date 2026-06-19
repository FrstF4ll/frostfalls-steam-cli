import shutil


def dependencies():
    steam_client = shutil.which("steam")
    steam_cmd = shutil.which("steamcmd")
    success = "All dependencies installed"

    if steam_client and steam_cmd:
        return success
    elif steam_client:
        return "Steamcmd is missing, please install steamcmd"
    elif steam_cmd:
        return "Steam client is missing, please install steam client"
