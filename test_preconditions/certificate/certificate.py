import random
import string


from test_preconditions.utils.db_connection import profit_cursor


def create(type='subscription', card='f', id=6, quality='HD', count=1):
    """
    Метод создания сертификатов
    По умолчанию создается один сертификат на подписку

    :param type: На что сертификат - 'subscription' (по умолчанию), 'content', 'compilation'
    :param card: Требуется ли привязка карты. 't' - да, 'f' - нет (по умолчанию).
    :param id: id контента. Для подписки 6 (по умолчанию).
    :param quality: Качество контента. 'HD' (по умолчанию)
    :param count: Количество сертификатов. 1 (по умолчанию)
    """

    # Генерирую случайное название для пула
    random_title = ''.join(random.choice(string.ascii_letters) for i in range(20)).lower()

    # Добавляю пул сертификатов в бд
    query = f'''
    INSERT INTO certificate_pool 
        (partner_id, title, bank_card_required, start_time, finish_time, 
        certificate_type, object_type, object_id, ownership_type, duration_days, enabled, renewal_period, quality, 
        certificate_pool_category_id,renewal_price, b2b, bonus, key_length, can_be_renew)
    VALUES 
        ('1', '{random_title}', '{card}', '2018-11-29 09:19:00', '2222-03-10 23:59:00',
        'personal', '{type}', '{id}', 'temporal', '365', 't', '2592000', '{quality}',
        '2', '399.0000','2999.0000','1789.0000', '6', 't');
    '''
    profit_cursor.execute(query)

    # Получаю id добавленного пула сертификатов
    get_pool_id_query = f"""
        SELECT id
        FROM certificate_pool
        WHERE title='{random_title}'
    """
    pool_id = profit_cursor.list_query(get_pool_id_query)[0]

    keys = []
    for i in range(count):
        # Добавляю сертификат в пул сертификатов
        random_key = ''.join(random.choice(string.ascii_letters) for i in range(6)).lower()
        add_cert_query = f"""
                INSERT INTO
                certificate
                (pool_id, key)
                VALUES ('{pool_id}', '{random_key}')
            """
        profit_cursor.execute(add_cert_query)

        # Получаю ключи добавленного сертификата
        get_keys_query = f"""
            SELECT key
            FROM certificate
            WHERE pool_id='{pool_id}'
        """
        keys = profit_cursor.list_query(get_keys_query)

    return keys
