from conftest import HOST


class Endpoints:
    create_user = f'{HOST}/users'
    get_user_by_id = lambda self, uuid: f'{HOST}/users/{uuid}'
