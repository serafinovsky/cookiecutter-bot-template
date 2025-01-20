import html
import re

from bs4 import BeautifulSoup
from django.template.loader import render_to_string
from telegram import InlineKeyboardButton

from {{cookiecutter.project_slug}}.bot_config import CB_SEP


def pad(cnt, *values):
    cnt = int(cnt)
    if (cnt % 100 > 20 or cnt % 100 < 10) and cnt % 10 == 1:
        return values[0]
    elif (cnt % 100 > 20 or cnt % 100 < 10) and 1 < cnt % 10 < 5:
        return values[1]
    else:
        return values[2]


def encode_callback(action, *params):
    return CB_SEP.join([action] + list(map(str, params)))


def decode_callback(text: str, pattern: re.compile):
    match = re.search(pattern, text)
    if not match:
        return {}
    return match.groupdict()


def make_inline_kbb(name: str, action: str, *params):
    return InlineKeyboardButton(name, callback_data=encode_callback(action, *params))


def strip_tags(text, tags=None):
    tags = tags or []
    soup = BeautifulSoup(text, 'html.parser')

    for tag in soup.find_all(True):
        if tag.name not in tags:
            tag.unwrap()
        elif isinstance(tags, dict):
            tag.attrs = {attr: value for attr, value in tag.attrs.items() if attr in tags[tag.name]}
    return str(soup)


def render_message(template: str):
    # https://core.telegram.org/bots/api#html-style
    tags = {
        'b': [], 'strong': [],
        'i': [], 'em': [],
        'u': [], 'ins': [],
        's': [], 'strike': [], 'del': [],
        'tg-spoiler': [],
        'a': ['href'],
        'tg-emoji': ['emoji-id'],
        'code': ['class'],
        'pre': [],
        'blockquote': ['expandable']
    }
    text = render_to_string(template)
    return strip_tags(html.unescape(text), tags)

