from utilities.allure_decorator import allure_auto_step
from utilities.config_reader import ReadConfig
from utilities.api.base_api import BaseAPI


@allure_auto_step
class PostsAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__posts_url = ReadConfig.get_posts_url()
        self.__post_to_update_url = ReadConfig.get_post_to_update_url()
        self.__invalid_posts_url = ReadConfig.get_invalid_posts_url()

    def get_all_posts(self):
        response = self.get(f"{self.__posts_url}")
        return response

    def get_post_by_id(self, post_id, headers=None):
        response = self.get(f"{self.__posts_url}/{post_id}", headers=headers)
        return response

    def get_posts_by_userid(self, userid, headers=None):
        response = self.get(f"{self.__posts_url}?userId={userid}", headers=headers)
        return response

    def get_all_posts_invalid_url(self):
        response = self.get(f"{self.__invalid_posts_url}")
        return response

    def create_post(self, request_body):
        response = self.post(f"{self.__posts_url}", request_body)
        return response

    def update_post(self, request_body):
        response = self.put(f"{self.__post_to_update_url}", request_body)
        return response

    def delete_post(self):
        response = self.delete(f"{self.__post_to_update_url}")
        return response
