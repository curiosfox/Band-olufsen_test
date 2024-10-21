from dataclasses import dataclass
from typing import Optional


@dataclass
class Geo:
    lat: str
    lng: str


@dataclass
class Address:
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


@dataclass
class Company:
    name: str
    catchPhrase: str
    bs: str


@dataclass
class User:
    id: int
    name: str
    username: str
    email: str
    address: Optional[Address]
    phone: str
    website: str
    company: Optional[Company]


@dataclass
class Post:
    userId: int
    id: int
    title: str
    body: str
