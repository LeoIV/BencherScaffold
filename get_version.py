import toml


def get_version():
    pyproject = toml.load("pyproject.toml")
    version = pyproject['tool']['poetry']['version']
    return version


if __name__ == '__main__':
    print(get_version())
