import argparse
import logging
import pandas as pd

from utils import get_data, save_data


parser = argparse.ArgumentParser(description='Get all posts for all users from api.')
parser.add_argument('--api_url', type=str, default='https://jsonplaceholder.typicode.com/posts',
                    help='The url to get all posts.')
parser.add_argument('-od', '--output_directory', type=str, default=None, help='The path to save the posts csv')

cmd_args = parser.parse_args()


def main():
    """
    Get all posts from api.
    """
    logger = logging.getLogger(__name__)
    logger.info(f'Getting posts from: {cmd_args.api_url}')
    posts = get_data(cmd_args.api_url)
    posts_df = pd.DataFrame(posts.json())
    logger.info('Saving posts')
    save_data(posts_df, output_dir=cmd_args.output_directory)


if __name__ == '__main__':
    main()
