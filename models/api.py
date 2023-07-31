from utils.helper import reqres_session


def get_list_users(params):
    response = reqres_session.get(f'/api/users', params=params)
    return response


def post_create_users(name, job):
    json = {'name': name, 'job': job}
    response = reqres_session.post(f'/api/users', json=json)
    return response


def get_user(id_user):
    response = reqres_session.get(f'/api/users/{id_user}')
    return response


def update_user(id_user, name, job):
    json = {'name': name, 'job': job}
    response = reqres_session.put(f'/api/users/{id_user}', json=json)
    return response


def delete_user(id_user):
    response = reqres_session.delete(f'/api/users/{id_user}')
    return response


def post_login_user(email, password):
    json = {'email': email, 'password': password}
    response = reqres_session.post(f'/api/login', json=json)
    return response


def post_register_user(email):
    json = {'email': email}
    response = reqres_session.post(f'/api/register', json=json)
    return response
