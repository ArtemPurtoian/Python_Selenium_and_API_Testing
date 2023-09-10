import json
from utilities.config_reader import ReadConfig
import requests


class BaseAPI:
    def __init__(self):
        self.__base_url = ReadConfig.get_base_api_url()
        self.__headers = json.loads(ReadConfig.get_base_headers())
        self.__request = requests

    def get(self, url, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.get(f"{self.__base_url}{url}",
                                      headers=headers)
        return response

    def post(self, url, json_data, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.post(f"{self.__base_url}{url}", json_data,
                                       headers=headers)
        return response

    def put(self, url, json, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.put(f"{self.__base_url}{url}", json,
                                      headers=headers)
        return response

    def delete(self, url):
        response = self.__request.delete(f"{self.__base_url}{url}")
        return response
