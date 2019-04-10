from test_preconditions.utils.db_connection import bd1_cursor


def content_by_type(paid_types, count=1, content_type="single", age_restrict=None, adult=None):
    """
    :param content_type: одиночный контент, одиночный контент из бандла (single, bundle)
    :param paid_types: список типов монетизации, которым должен соотвествовать контент
    :param count: количество id контента в возвращаемом списке
    :param age_restrict: возрастное ограничение (по-умолчанию не учитывается, функция берет весь контент,
        у которого значение restrict меньше либо равно заданному)
    :param adult: возрастное ограничение (по-умолчанию не учитывается, True - контент 18+, False - весть
        остальной контент)
    :return: возвращает список id и title контента
    """

    query = f"""
        SELECT cs.content_id, c.title
        FROM content_subsite_formats_mapi AS cs
        JOIN content AS c ON cs.content_id=c.id
        """

    if content_type == "single":
        query += f"""
            WHERE c.compilation_id IS NULL
            """
    elif content_type == "bundle":
        query += f"""
            JOIN collection_catalog AS cc ON cs.content_id=cc.content_id
            JOIN collection AS cl ON cl.id=cc.collection_id
            WHERE cl.store_price_tier_id IS NOT NULL
                AND c.compilation_id IS NULL
            """

    query += f"AND paid_types = ARRAY{paid_types} "

    if age_restrict:
        print("Вместо age_restrict используйте параметр adult.")
        query += f"AND c.restrict <= {age_restrict} "
    elif adult:
        query += f"AND c.restrict >= 18 "
    elif adult is False:
        query += f"AND c.restrict < 18 "

    query += f"LIMIT {count};"

    content_list = bd1_cursor.dict_query(query)
    return content_list


def compilation_by_type(compilation_type, paid_types, count=1, age_restrict=0):
    """
    :param compilation_type: тип сборника по наличию сезонов(with_seasons, without_seasons)
    :param paid_types: список типов монетизации, которым должен соотвествовать сборник
    :param count: количество id сборников в возвращаемом списке
    :param age_restrict: возрастное ограничение (по-умолчанию не учитывается, функция берет все сборники, у которых
        значение restrict меньше либо равно заданному)
    :return: возвращает список id и title сборников
    """

    query = f"""
        SELECT DISTINCT cs.compilation_id, c.title
        FROM compilation_subsite_formats_mapi AS cs
        """

    if compilation_type == "with_seasons":
        query += f"""
            JOIN compilation_season_description AS s ON
                cs.compilation_id=s.compilation_id
                AND cs.paid_types=ARRAY{paid_types}
            JOIN compilation AS c ON cs.compilation_id=c.id
            WHERE season IS NOT null
            """
    elif compilation_type == "without_seasons":
        query += f"""
            JOIN compilation AS c ON cs.compilation_id=c.id
            WHERE NOT EXISTS
                ( SELECT *
                  FROM compilation_season_description
                  WHERE compilation_id=cs.compilation_id )
                AND cs.paid_types=ARRAY{paid_types}
            """

    if age_restrict:
        query += f"AND c.restrict <= {age_restrict} "

    query += f"LIMIT {count};"

    compilation_list = bd1_cursor.dict_query(query)
    return compilation_list


def preorder(count=1):
    """
    :param count: Количество предзаказов в возвращаемом списке
    :return: возвращает список id и title предзаказов
    """
    query = f"""
        SELECT c.id, c.title 
        FROM content c JOIN content_subsite cs 
        ON cs.content_id = c.id AND ARRAY[353] <@ subsite_ids LEFT JOIN content_app_version_mapi cam 
        ON cam.content_id = c.id AND ARRAY[870] <@ versions_with_allowed_formats JOIN content_preorder_mapi cp 
        ON cp.content_id = c.id WHERE c.compilation_id IS NULL
        AND cam.id IS NULL LIMIT {count}
        """
    preorder_list = bd1_cursor.dict_query(query)
    return preorder_list
