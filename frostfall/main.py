from frostfall import validator


def main():
    is_installed = validator.dependencies()
    print(is_installed)
