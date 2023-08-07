import allure
from allure_commons.types import Severity
import schemas.schemas_api
from models.api import get_list_users, post_create_users, update_user, \
    get_user, delete_user, post_register_user
from pytest_voluptuous import S


@allure.tag('api')
@allure.label('owner', 'Morilova')
@allure.feature('Проверка метода на возвращение списка пользователей')
@allure.link(f'/api/users')
def test_list_users():
    with allure.step(f'  GET запрос c параметром page=2'):
        response = get_list_users(params={"page": 2})
    with allure.step('Проверка статус-кода и списка пользователей'):
        assert response.status_code == 200
        assert response.json()['page'] == 2


@allure.tag('api')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Morilova')
@allure.feature('Проверка создания пользователя при вводе валидных данных')
@allure.link(f'/api/users')
def test_create_user(name='Nina', job='postman'):
    with allure.step(f'POST запрос c валидными данными в теле запроса'):
        response = post_create_users(name, job)
    with allure.step('Проверка успешного создания и соответствия введенных данных'):
        assert response.status_code == 201
        assert response.json()['name'] == name
        assert response.json()['job'] == job
    with allure.step('Проверка соответствия ответа схеме'):
        assert response.json() == S(schemas.schemas_api.create_user_schema)


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Morilova')
@allure.feature(f'Проверка возвращения в ответе пользователя по заданному id {6}')
@allure.link(f'/api/users/{6}')
def test_get_user(id_user=6):
    with allure.step(f'GET запрос c id пользователя'):
        response = get_user(id_user)
    with allure.step(f'Проверка получения в ответе данных пользователя с id {6}'):
        assert response.status_code == 200
        assert response.json()['data']['id'] == 6
        assert response.json()['data']['email'] == 'tracey.ramos@reqres.in'
        assert response.json()['data']['first_name'] == 'Tracey'
        assert response.json()['data']['last_name'] == 'Ramos'
    with allure.step('Проверка соответствия ответа схеме'):
        assert response.json() == S(schemas.schemas_api.get_user_schema)


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Morilova')
@allure.feature('Проверка обновления id, name, job пользователя')
@allure.link(f'/api/users/{4}')
def test_update(id_user=4, name='Egor',
                job='driver'):
    with allure.step('POST запрос с валидными данными'):
        response = update_user(id_user, name, job)
    with allure.step('Проверка успешного обновления пользователя'):
        assert response.status_code == 200
        assert response.json()['name'] == name
        assert response.json()['job'] == job
    with allure.step('Проверка соответствия ответа схеме'):
        assert response.json() == S(schemas.schemas_api.update_user_schema)


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Morilova')
@allure.feature('Проверка удаления пользователя')
@allure.link(f'/api/users/4')
def test_delete(id_user=4):
    with allure.step(f'Отправка запроса DELETE с id 4'):
        response = delete_user(id_user)
    with allure.step('Проверка соответствия статус-коду'):
        assert response.status_code == 204


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Morilova')
@allure.feature('Проверка авторизации пользователя без пароля в теле запроса')
@allure.link(f'/api/register')
def test_failed_register():
    with allure.step('POST запрос без обязательного параметра password'):
        response = post_register_user(email='test@test.ru')
    with allure.step('Проверка статус-кода и ошибки в ответе'):
        assert response.status_code == 400
        assert response.json()['error'] == 'Missing password'
    with allure.step('Проверка соответствия ответа схеме'):
        assert response.json() == S(schemas.schemas_api.post_unsuccesses_register_user)
