import requests
import uuid
import typing as tp

from ...domain import Post


class BackendService:
    def __init__(self, host: str):
        self.host = host

    def get_post_by_id(self, post_id: uuid.UUID) -> Post:
        try:
            response = requests.get(
                f"{self.host}/api/v1/admin/posts/{post_id}"
            )
            response.raise_for_status()
            return Post(**response.json())
        except requests.exceptions.HTTPError as err:
            raise err

    def get_friends_by_user_id(self, user_id: uuid.UUID) -> tp.List[uuid.UUID]:
        try:
            response = requests.get(
                f"{self.host}/api/v1/admin/friends/{user_id}"
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            raise err

    def get_posts_by_author_id(self, author_id: uuid.UUID) -> tp.List[Post]:
        try:
            response = requests.get(
                f"{self.host}/api/v1/admin/posts/author/{author_id}"
            )
            response.raise_for_status()
            return [Post(**post) for post in response.json()]
        except requests.exceptions.HTTPError as err:
            raise err
