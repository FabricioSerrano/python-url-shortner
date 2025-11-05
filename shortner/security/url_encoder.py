from hashids import Hashids

from shortner.settings import Settings


def encode(base62Url: int) -> str:
    alphabet = '0123456789ABCDEFGHIJKLMOPQRSTUVWZYZabcdefghijklmnopqrstuvwxyz'
    hasher = Hashids(salt=Settings().SECRET_KEY, alphabet=alphabet)

    return hasher.encode(base62Url)
