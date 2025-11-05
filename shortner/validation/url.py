from shortner.exceptions.url_exceptions import HostException, ProtocolException


class URL:
    def __init__(self, url_as_str: str):
        self.protocol = self.__validate_protocol(url_as_str)
        self.host = self.__validade_host(url_as_str)
        self.query = self.__get_query(url_as_str)
        self.long_url: str = url_as_str

    def __validate_protocol(url: str) -> str:
        if not url.startswith(('http://', 'https://', 'ftp://')):
            raise ProtocolException()

        protocol = url.split('://', maxsplit=1)[0]

        return protocol

    def __validade_host(url: str) -> str:
        splited_url = url.split('://')[1]

        if not splited_url or 'localhost' in splited_url:
            raise HostException()

        host = splited_url.split('/')[0]

        if '.' not in host:
            raise HostException()

        return host

    def __get_query(self, url: str) -> str | None:
        query = url.split(f'{self.protocol}://{self.host}')

        if query[1] == '/' or not query[1]:
            return None

        return query[1].removeprefix('/')
