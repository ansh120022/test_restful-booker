import logging

import requests

from model.login import UserData
from api.booking import BookingApi

logger = logging.getLogger()


class Client:
    request = requests.Session()

    def __init__(self, url):
        self.url = url
        self.booking = BookingApi(self)

    def login(self, user_data: UserData):
        data = user_data.__dict__
        return self.request.post(self.url + "/auth", json=data)

    def authorize(self, user_data: UserData):
        res = self.login(user_data)
        if res.status_code != 200:
            raise Exception("Authorization error")
        session_token = res.json().get("token")
        logger.info(f'Get token {session_token}')
        cookie = requests.cookies.create_cookie("token", session_token)
        self.request.cookies.set_cookie(cookie)