from collections import namedtuple
from xml.etree import ElementTree

import requests

Episode = namedtuple('Episode', 'title link pubdate show_id')
episode_data = {}


def download_info():
    url = 'https://pythonbytes.fm/episodes/rss'

    resp = requests.get(url)
    resp.raise_for_status()

    dom = ElementTree.fromstring(resp.text)

    items = dom.findall('channel/item')
    episode_count = len(items)

    for idx, item in enumerate(items):
        episode = Episode(
            item.find('title').text,
            item.find('link').text,
            item.find('pubDate').text,
            episode_count - idx
        )
        episode_data[episode.show_id] = episode


def get_episode(show_id: int) -> Episode:
    return episode_data.get(show_id)


def get_latest_show_id():
    if not episode_data:
        return 0
    return max(episode_data.keys())


def get_min_show_id():
    if not episode_data:
        return 0
    return min(episode_data.keys())
