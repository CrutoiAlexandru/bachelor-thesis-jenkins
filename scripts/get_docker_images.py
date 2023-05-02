import subprocess


def get_versions(repository):
    cmd = f'sudo docker search "{repository}"'
    output = subprocess.check_output(cmd, shell=True)
    lines = output.decode('utf-8').splitlines()
    try:
        versions = [line.split(':')[1] for line in lines]
    except IndexError:
        versions = []
    return versions
