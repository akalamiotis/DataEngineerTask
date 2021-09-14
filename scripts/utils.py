import os
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def get_data(api_url):
    """
    Gets data from api.
    :param api_url: url to get posts
    :type api_url: str
    :return: all posts
    """
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)

    try:
        response = session.get(api_url)
        response.raise_for_status()
    except (requests.exceptions.RequestException, requests.HTTPError) as e:
        raise RuntimeError(f"Unable to connect to {api_url} with error: {e}")
    else:
        return response


def save_data(data, output_dir=None):
    """
    Saves data to a csv file.
    :param data: DataFrame
    :param output_dir: Directory to save the csv file
    """
    if output_dir:
        save_name = os.path.join(output_dir, "posts.csv")
    else:
        save_name = "posts.csv"
    data.to_csv(save_name, index=False, encoding='utf-8')

