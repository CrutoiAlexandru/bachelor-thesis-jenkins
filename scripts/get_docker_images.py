import subprocess
import logging
logging.basicConfig(level=logging.INFO)


def get_versions(repository):
    cmd = f'sudo docker search "{repository}"'
    output = subprocess.check_output(cmd, shell=True)
    lines = output.decode('utf-8').splitlines()
    try:
        versions = [line.split(':')[1] for line in lines]
    except IndexError as e:
        versions = []
        logging.info(e)
    return versions
