import toml


def bump_version():
    # Load the pyproject.toml file
    pyproject = toml.load("pyproject.toml")

    # Get the current version
    version = pyproject['tool']['poetry']['version']

    # Split the version into major, minor, and patch
    major, minor, patch = map(int, version.split('.'))

    # Increment the patch version
    patch += 1

    # Combine the major, minor, and patch into the new version
    new_version = f"{major}.{minor}.{patch}"

    # Update the version in the pyproject.toml file
    pyproject['tool']['poetry']['version'] = new_version

    # Write the pyproject.toml file back to disk
    with open("pyproject.toml", "w") as f:
        toml.dump(pyproject, f)

    print(f"Bumped version to {new_version}")


if __name__ == '__main__':
    bump_version()
