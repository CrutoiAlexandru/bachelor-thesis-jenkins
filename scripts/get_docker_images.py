import subprocess


def get_versions(repository):
    cmd = f'docker search "{repository}"'
    output = subprocess.check_output(cmd, shell=True)
    lines = output.decode('utf-8').splitlines()
    versions = [line.split(':') for line in lines]
    return versions
