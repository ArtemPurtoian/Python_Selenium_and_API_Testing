import configparser
import os
import sys


relative_path = "./configurations/app_config.ini"
abs_path = os.path.abspath(relative_path)
config = configparser.RawConfigParser()
config.read(relative_path)


class ReadConfig:
    @staticmethod
    def get_browser_id():
        return config.get("browser_data", "browser_id")

    @staticmethod
    def get_app_base_url():
        return config.get("app_data", "base_url")

    @staticmethod
    def get_app_title():
        return config.get("app_data", "title")

    @staticmethod
    def get_user_email():
        return config.get("user_data", "email")

    @staticmethod
    def get_user_password():
        return config.get("user_data", "password")

    @staticmethod
    def get_suggested_pages_url():
        return config.get("home_page", "suggested_pages_url")

    @staticmethod
    def get_user_name():
        return config.get("user_data", "user_name")

    @staticmethod
    def get_user_profile_url():
        return config.get("user_data", "user_profile_url")

    @staticmethod
    def get_new_collection_name():
        return config.get("user_page", "new_collection")

    @staticmethod
    def get_edited_collection_name():
        return config.get("user_page", "edited_collection_name")

    @staticmethod
    def get_bio_info():
        return config.get("user_page", "bio")

    @staticmethod
    def get_page_name_to_search():
        return config.get("search_page", "page_name")

    @staticmethod
    def get_desired_page_title():
        return config.get("search_page", "page_title")

    @staticmethod
    def get_message_recipient():
        return config.get("message_page", "recipient_name")

    @staticmethod
    def get_message_body():
        return config.get("message_page", "message")

    @staticmethod
    def get_about_tab_url():
        return config.get("footer", "about_tab_url")

    @staticmethod
    def get_footer_date_string():
        return config.get("footer", "footer_date_string")

    @staticmethod
    def get_extension_path():
        return config.get("extension_path", sys.platform)

    @staticmethod
    def get_base_api_url():
        return config.get("api", "base_api_url")

    @staticmethod
    def get_base_headers():
        return config.get("api", "base_headers")

    @staticmethod
    def get_api_content_header():
        return config.get("api", "content_header")

    @staticmethod
    def get_api_content_json():
        return config.get("api", "content_json")

    @staticmethod
    def get_post_request_body():
        return config.get("api", "post_request_body")

    @staticmethod
    def get_put_request_body():
        return config.get("api", "put_request_body")

    @staticmethod
    def get_posts_url():
        return config.get("api", "posts_url")

    @staticmethod
    def get_post_to_update_url():
        return config.get("api", "post_to_update_url")

    @staticmethod
    def get_invalid_posts_url():
        return config.get("api", "invalid_posts_url")

    @staticmethod
    def get_users_url():
        return config.get("api", "users_url")

    @staticmethod
    def get_invalid_users_url():
        return config.get("api", "invalid_users_url")
