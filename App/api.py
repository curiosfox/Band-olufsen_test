import logging
from typing import List, Optional
from .models import User, Post, Geo, Address, Company
import requests


class ApiClass(object):
    """ Wrapper class for Apis used in the application """

    def __init__(self, logger: logging.Logger) -> None:
        """ Constructor to hold all API class variables

        :param logger (logging.Logger): Logger instance to use.
        """

        self.api_path: str = "https://jsonplaceholder.typicode.com"
        self.log = logger

    @staticmethod
    def _parse_user_data(user_data_dump: dict) -> User:
        """ Parses the User data blob into objects

        :param user_data_dump (dict) : Input user data dump from /users API response
        :return (object) : Return User object with all data from user_data_dump
        """

        geo_data = user_data_dump['address']['geo']
        geo = Geo(lat=geo_data['lat'], lng=geo_data['lng'])
        address_data = user_data_dump['address']
        address = Address(
            street=address_data['street'],
            suite=address_data['suite'],
            city=address_data['city'],
            zipcode=address_data['zipcode'],
            geo=geo
        )
        company_data = user_data_dump['company']
        company = Company(
            name=company_data['name'],
            catchPhrase=company_data['catchPhrase'],
            bs=company_data['bs']
        )
        user = User(
            id=user_data_dump['id'],
            name=user_data_dump['name'],
            username=user_data_dump['username'],
            email=user_data_dump['email'],
            address=address,
            phone=user_data_dump['phone'],
            website=user_data_dump['website'],
            company=company
        )

        return user

    def get_api_data(self, api_path: str) -> Optional[dict]:
        """ Obtains GET response from APIs sent by user parameter

        :param api_path (str): Path to trigger GET request
        :return (dict) : Return response data from the GET API
        """

        get_url = f"{self.api_path}/{api_path}"
        try:
            response = requests.get(get_url)
            return response.json()
        except Exception as api_ex:
            self.log.error(f"Caught Exception during Get API execution for :{get_url}\n Exception raised :{api_ex}")
            return None

    def get_users(self) -> List[User]:
        """ Fetches and returns a list of User objects.

        :return (list) : Return list of User objects
        """

        user_api_path: str = "users"
        users_data = self.get_api_data(user_api_path)
        if users_data is None:
            self.log.error("Failed to fetch users data.")
            return []
        users: List[User] = [self._parse_user_data(user_dict) for user_dict in users_data]
        return users

    def get_posts(self) -> List[Post]:
        """ Fetches and returns a list of Post objects.

        :return (list) : Return list of Post objects
        """

        post_api_path: str = "posts"
        posts_data = self.get_api_data(post_api_path)
        if posts_data is None:
            self.log.error("Failed to fetch posts data.")
            return []
        posts: List[Post] = [Post(**post_dict) for post_dict in posts_data]
        return posts
