from pydantic import BaseModel


class UrlShortenCreated(BaseModel):
    short_url: str


class UrlSchema(BaseModel):
    url: str


class ServerStatus(BaseModel):
    status: str
