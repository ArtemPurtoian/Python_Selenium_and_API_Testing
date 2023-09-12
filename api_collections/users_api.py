from utilities.allure_decorator import allure_auto_step
from utilities.config_reader import ReadConfig
from utilities.api.base_api import BaseAPI


@allure_auto_step
class UsersAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__users_url = ReadConfig.get_users_url()
        self.__invalid_users_url = ReadConfig.get_invalid_users_url()

    def get_all_users(self, headers=None):
        response = self.get(f"{self.__users_url}", headers=headers)
        return response

    def get_user_by_id(self, user_id, headers=None):
        response = self.get(f"{self.__users_url}/{user_id}", headers=headers)
        return response

    def get_user_by_name(self, name, headers=None):
        response = self.get(f"{self.__users_url}?name={name}", headers=headers)
        return response

    def get_all_users_invalid_url(self):
        response = self.get(f"{self.__invalid_users_url}")
        return response
