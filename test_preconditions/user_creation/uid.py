from test_preconditions.utils.db_connection import auth_cursor


def get_uid_by_email(email):
    """ Получение UID по e-mail.
    :param email: e-mail
    :return: uid
    """

    query = f"""
        SELECT uid
        FROM email
        WHERE value='{email}'
    """

    result = auth_cursor.list_query(query)

    return result[0] if result else None


def get_uid_by_phone(phone):
    """ Получение UID по номеру телефона.
    :param phone: номер телефона
    :return: uid
    """

    query = f"""
        SELECT uid
        FROM phone
        WHERE value = '{phone}'
    """

    result = auth_cursor.list_query(query)

    return result[0] if result else None


def get_uid(login):
    """ Получение UID по email или номеру телефона.
    :param login: email или номер телефона
    :return: uid
    """

    if '@' in login:
        return get_uid_by_email(login)
    return get_uid_by_phone(login)
