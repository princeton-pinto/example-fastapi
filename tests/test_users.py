# import pytest
# from jose import jwt
# from app import schemas
# from .database import client, session
# from app.config import settings


# def test_root(client):
#     res = client.get("/")
#     print(res.json().get('message'))
#     assert res.json().get('message') == 'Hello World!!! Peace be with you all!'
#     assert res.status_code == 200

# def test_create_user(client):
#     res = client.post("/users/",json={"email":"LukeRockhold@ufc.com","password":"PoloCosta"})
#     new_user = schemas.UserOut(**res.json())
#     assert new_user.email == "LukeRockhold@ufc.com"
#     assert res.status_code == 201

# def test_login_user(client, test_user):
#     res = client.post("/login",data={"username":test_user['email'],"password":test_user['password']})
#     # print(res.json())
#     login_res = schemas.Token(**res.json())
#     payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
#     id = payload.get("user_id")
#     assert id == test_user["id"]
#     assert login_res.token_type == "bearer"
#     assert res.status_code == 200

# @pytest.mark.parametrize("email, password, status_code", [
#     ('wrongemail@gmail.com', 'PoloCosta', 403),
#     ('LukeRockhold@ufc.com', 'wrongpassword', 403),
#     ('wrongemail@gmail.com', 'wrongpassword', 403),
#     (None, 'PoloCosta', 422),
#     ('LukeRockhold@ufc.com', None, 422)
# ])
# def test_incorrect_login(test_user, client, email, password, status_code):
#     res = client.post("/login", data={"username": email, "password": password})
#     assert res.status_code == status_code

# # pytest --disable-warnings -v -s

import pytest
from jose import jwt
from app import schemas

from app.config import settings


# def test_root(client):

#     res = client.get("/")
#     print(res.json().get('message'))
#     assert res.json().get('message') == 'Hello World'
#     assert res.status_code == 200


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "hello123@gmail.com", "password": "password123"})

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201


def test_login_user(test_user, client):
    res = client.post(
        "/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token,
                         settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'password123', 403),
    ('PauloCosta@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'password123', 422),
    ('PauloCosta@gmail.com', None, 422)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post(
        "/login", data={"username": email, "password": password})

    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid Credentials'