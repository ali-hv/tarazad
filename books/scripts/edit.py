import re


def remove_page_top_section(text):
    text = re.sub(r'^.*?\]', "", text)
    return text
