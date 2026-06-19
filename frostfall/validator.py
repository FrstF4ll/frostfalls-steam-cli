import shutil


def dependencies():
    steam_client = shutil.which("steam")
    steam_cmd = shutil.which("steamcmd")
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
