import shutil


def check_steam_client():
    if shutil.which("steam"):
        answer = "steam client is installed"
    else:
        answer = "steam client is not installed"

    return answer


def check_steamcmd():
    if shutil.which("steamcmd"):
        answer = "steamcmd is installed"
    else:
        answer = "steamcmd is not installed"

    return answer


def dependencies():
    return check_steamcmd() + " " + check_steam_client()
