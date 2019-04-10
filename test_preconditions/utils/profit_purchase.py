import os

import requests

PROFIT = f"http://profit.{os.environ['CLUSTER_TEST']}.notkube.dev.ivi.ru"


def make_purchase(uid, content_id, content_type, ownership, quality='HD', finish_time='2020-06-23'):
    data = {
        "SubsiteId": 353,
        "Purchase": {
            "Options": {
                "quality": f"{quality}"
            },
            "FinishTime": f"{finish_time}T20:37:09.253663+03:00",
            "ObjectType": f"{content_type}",
            "ObjectId": content_id,
            "OwnershipType": f"{ownership}"
        },
        "UserPrice": "10.0000",
        "Price": "11.0000",
        "PsKey": "ivi",
        "PlaceId": 1488
    }
    make_money(uid, "RUB")
    r = requests.post(url=PROFIT+f'/user/{uid}/purchase', json=data)
    result = {'uid': uid, 'content_id': content_id,
              'content_type': content_type, 'ownership': ownership, 'quality': quality}

    return result


def make_money(uid, currency, amount='11'):
    """
    :param uid: id пользователя, для которого начисляем деньги
    :param currency: валюта, в которой начисляем деньги
    :param amount: количество денег
    :return: а мы ничего не возвращаем. зачем?
    """
    data = {'Currency': f'{currency}', 'Amount': {'B2b': f'{amount}'},
            'PlaceId': 41207, 'PsKey': 'manual', 'SubsiteId': 195}
    r = requests.post(url=PROFIT+f'/user/{uid}/balance', json=data)
