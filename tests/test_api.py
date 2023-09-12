import pytest
from utilities.config_reader import ReadConfig
from api_collections.posts_api import PostsAPI
from api_collections.users_api import UsersAPI
from http import HTTPStatus


@pytest.mark.regression
def test_get_all_users_success():
    users_api = UsersAPI()
    response = users_api.get_all_users()
    assert response.status_code == HTTPStatus.OK, \
        f"HTTP code is not {HTTPStatus.OK} - got {response.status_code}"
    assert (response.headers[ReadConfig.get_api_content_header()] ==
            ReadConfig.get_api_content_json()), "Response is not a JSON."


@pytest.mark.regression
def test_get_user_by_id():
    users_api = UsersAPI()
    response = users_api.get_user_by_id(1)
    assert response.status_code == HTTPStatus.OK, \
        f"HTTP code is not {HTTPStatus.OK} - got {response.status_code}"
    assert (response.headers[ReadConfig.get_api_content_header()] ==
            ReadConfig.get_api_content_json()), "Response is not a JSON."


@pytest.mark.regression
def test_get_user_by_name():
    users_api = UsersAPI()
    response = users_api.get_user_by_name("Leanne Graham")
    assert response.status_code == HTTPStatus.OK, \
        f"HTTP code is not {HTTPStatus.OK} - got {response.status_code}"
    assert (response.headers[ReadConfig.get_api_content_header()] ==
            ReadConfig.get_api_content_json()), "Response is not a JSON."


@pytest.mark.regression
def test_negative_all_users_not_found_404():
    users_api = UsersAPI()
    response = users_api.get_all_users_invalid_url()
    assert response.status_code == HTTPStatus.NOT_FOUND, \
        f"HTTP code is not {HTTPStatus.NOT_FOUND} - got {response.status_code}"


@pytest.mark.regression
def test_get_all_posts_success():
    posts_api = PostsAPI()
    response = posts_api.get_all_posts()
    assert response.status_code == HTTPStatus.OK, \
        f"HTTP code is not {HTTPStatus.OK} - got {response.status_code}"
    assert (response.headers[ReadConfig.get_api_content_header()] ==
            ReadConfig.get_api_content_json()), "Response is not a JSON."


@pytest.mark.regression
def test_get_post_by_id():
    posts_api = PostsAPI()
    response = posts_api.get_post_by_id(1)
    assert response.status_code == HTTPStatus.OK
    assert (response.headers[ReadConfig.get_api_content_header()] ==
            ReadConfig.get_api_content_json()), "Response is not a JSON."


@pytest.mark.regression
def test_get_posts_by_userid():
    posts_api = PostsAPI()
    response = posts_api.get_posts_by_userid(4)
    assert response.status_code == HTTPStatus.OK, \
        f"HTTP code is not {HTTPStatus.OK} - got {response.status_code}"
    assert (response.headers[ReadConfig.get_api_content_header()] ==
            ReadConfig.get_api_content_json()), "Response is not a JSON."


@pytest.mark.regression
def test_negative_all_posts_not_found_404():
    posts_api = PostsAPI()
    response = posts_api.get_all_posts_invalid_url()
    assert response.status_code == HTTPStatus.NOT_FOUND, \
        f"HTTP code is not {HTTPStatus.NOT_FOUND} - got {response.status_code}"
    assert (response.headers[ReadConfig.get_api_content_header()] ==
            ReadConfig.get_api_content_json()), "Response is not a JSON."


@pytest.mark.regression
def test_post_created_201():
    body = ReadConfig.get_post_request_body()
    posts_api = PostsAPI()
    response = posts_api.create_post(body)
    assert response.status_code == HTTPStatus.CREATED, \
        f"HTTP code is not {HTTPStatus.CREATED} - got {response.status_code}"
    assert (response.headers[ReadConfig.get_api_content_header()] ==
            ReadConfig.get_api_content_json()), "Response is not a JSON."


@pytest.mark.regression
def test_update_post():
    body = ReadConfig.get_put_request_body()
    posts_api = PostsAPI()
    response = posts_api.update_post(body)
    assert response.status_code == HTTPStatus.OK, \
        f"HTTP code is not {HTTPStatus.OK} - got {response.status_code}"
    assert (response.headers[ReadConfig.get_api_content_header()] ==
            ReadConfig.get_api_content_json()), "Response is not a JSON."


@pytest.mark.regression
def test_delete_post():
    posts_api = PostsAPI()
    response = posts_api.delete_post()
    assert response.status_code == HTTPStatus.OK, \
        f"HTTP code is not {HTTPStatus.OK} - got {response.status_code}"
    assert len(response.json()) == 0
