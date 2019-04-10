import requests

from test_preconditions.utils import profit_purchase


def content_purchase(uids, content_ids, content_type, ownership, quality='HD'):
    """
    :param uids: список вида [1, 2, 3, 4]
    :param content_ids: список вида [7029, 40468]
    :param content_type: content, compilation, season, subscription, collection, product, gift, manual_debit
    :param ownership: eternal для EST, temporal для TVOD
    :param quality: SD, HD, UHD
    :return: возвращает список словарей с покупками. внутри словаря: uid, content_id, content_type, ownership, quality
    """
    purchases = []
    for uid in uids:
        for content_id in content_ids:
            purchases.append(profit_purchase.make_purchase(uid, content_id, content_type, ownership, quality))
    return purchases


def subscription_purchase(uids, finish_time='2020-06-23'):
    """
    :param uids: id пользователей, кому покупаем подписку
    :return: возвращает список словарей с покупками. внутри словаря: uid, content_id, content_type, ownership, quality
    """
    purchases = []
    for uid in uids:
        purchases.append(
            profit_purchase.make_purchase(
                uid,
                content_id=6,
                content_type='subscription',
                ownership='temporal',
                finish_time=finish_time)
        )
    return purchases


def add_money(uid, currency, amount='11'):
    """
    :param uid: id пользователя, для которого начисляем деньги
    :param currency: валюта, в которой начисляем деньги
    :param amount: количество денег
    :return: метод позволяет добавлять деньги, не
    """
    profit_purchase.make_money(uid, currency=currency, amount=amount)


def cancel_subscription(uid):
    """ Отмена подписки

    :param uid: id пользователя
    """

    requests.put(url=f"{profit_purchase.PROFIT}/user/{uid}/subscription/cancel")
