import logging
import requests
logging.basicConfig(level=logging.INFO)


def get_versions(repository):

    # Set the registry URL and image name
    registry_url = 'https://registry-1.docker.io'
    image_name = repository

    # Construct the API endpoint URL to list image tags
    tags_url = f'{registry_url}/v2/{image_name}/tags/list'

    # Make a GET request to the API endpoint
    response = requests.get(tags_url)

    # Parse the response JSON to get the available versions
    if response.ok:
        tags = response.json()['tags']
        print(f'The available versions for {image_name} are: {tags}')
        return tags
    else:
        print(
            f'Failed to get tags for {image_name}: {response.status_code} {response.reason}')
        return []
