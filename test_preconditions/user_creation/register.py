import os
import re
import string
from random import choices
import requests
from test_preconditions.exceptions import mapi_exceptions

MAPI = f"http://api.{os.environ['CLUSTER_TEST']}.notkube.dev.ivi.ru/mobileapi"
REGISTER_ENDPOINT = '/user/register/v5/'
APP_VERSION = '870'
CYRILLIC_SYMBOLS = 'абвгдеёзжийклмнопрстуфхцчшщъыьэюя'


def register_email(amount=1, random_len=10, email_pattern='test@ivi.ru', password='1111111'):
    """
    :param email_pattern: строка шаблона email, в которой будет добавлен уникальный суффикс
    :param password: строка пароля
    :param amount: принимает количество юзеров, которых нужно зарегить
    :param random_len: принимает число, обозначающее количество символов в email после test
    :return: возвращает список словарей с информацией о юзерах: app_version, email, password, uid, session
    """
    users = []
    box_name, domain = email_pattern.split('@')
    alphabet = string.ascii_lowercase
    if bool(re.search('[а-яА-ЯёЁ]', box_name)):
        alphabet = CYRILLIC_SYMBOLS
    for i in range(amount):
        random_suffix = ''.join(choices(alphabet + string.digits, k=random_len))
        email = f"{box_name}{random_suffix}@{domain}"
        users.append(register_user_by_email(email, password))
    return users


def register_user_by_email(email, password='1111111'):
    """
    :param email: строка имейла
    :param password: строка пароля
    :return: словарь с информацией о юзере: : app_version, email, password, uid, session
    """
    data = {
        'app_version': APP_VERSION,
        'email': email,
        'password': f'{password}'
    }
    r = requests.post(url=MAPI + REGISTER_ENDPOINT, data=data)
    r.raise_for_status()
    response_body = r.json()
    if 'error' in response_body:
        raise mapi_exceptions.MapiError(
            message=f"register_user_by_email(): got error from mapi: {response_body['error']}")
    session = response_body['result']['session']
    # TODO: Переписать этот стремный костыль в нормальную регулярку
    data['uid'], data['session'] = re.search(r'.{8}(\d+)_', session).groups()[0], session
    return data

