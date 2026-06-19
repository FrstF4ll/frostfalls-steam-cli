from frostfall import validator


def main():
    path = input("Add your steam path: ")
    is_installed = validator.check_dependencies()
    is_path = validator.check_directory(path)
    is_connected = validator.check_connectivity()
    print(is_installed)
    print(is_path)
    print(is_connected)
