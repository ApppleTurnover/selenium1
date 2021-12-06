from urllib.parse import urlparse, parse_qs


class URLs(list):
    def __init__(self, *urls: str):
        super().__init__(urls)
