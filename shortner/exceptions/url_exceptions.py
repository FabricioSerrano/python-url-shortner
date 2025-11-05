class ProtocolException(Exception):
    def __init__(self):
        super().__init__('Protocol not found or not suported.')


class HostException(Exception):
    def __init__(self):
        super().__init__('Invalid or broken host.')
