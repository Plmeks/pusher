from test_preconditions.pusher.delivery import Delivery

from test_preconditions.pusher.config import *


def send_pull(new_parameters, url=PUSHER_DELIVERY_URL, **params):
    """
    функция отправки pull-рассылки с изменёнными параметрами на нужный адрес
    :param new_parameters: словарь, параметры для переопределения
    :param url: строка, ссылка, куда производить отправку запроса
    :return: ответ сервера или False, в случае отсутсвиии отпарвки из-за неверно заполненных параметров
    """
    pull = DeliveryPull()
    pull.change_parameters(new_parameters)
    pull.change_params(**params)
    response = pull.send_delivery(url)
    pull.check_delivery_status()
    return response


def send_set_pull(new_params, url=PUSHER_DELIVERY_URL, **params):
    """
    функция отправки pull-рассылки с заданными параметрами, параметры по умолчанию удалены
    использовать с осторожностью
    :param new_params: словарь, все параметры, которые нужно передать в запросе
    :param url: строка, ссылка, куда производить отправку запроса
    :return: ответ сервера или False, в случае отсутсвиии отпарвки из-за неверно заполненных параметров
    """
    pull = DeliveryPull()
    pull.set_parameters(new_params)
    pull.set_params(**params)
    response = pull.send_delivery(url)
    pull.check_delivery_status()
    return response


class DeliveryPull(Delivery):
    def __init__(self):
        """
        конструктор, инициализирует необходимые параметры, и переопределяет их на дефолтные параметры для pull
        """
        super().__init__()
        self.headers = {"Content-Type": "application/json"}
        self.parameters["feature_id"] = FEATURE_ID_TEXT
        self.parameters["messages"] = self.get_messages_pull()
        self.parameters["rule_params"] = {"user_ids": USER_ID}

    @staticmethod
    def get_messages_pull(template=PULL_TEMPLATE_DEFAULT_ERROR, device=PULL_CLASSIFICATION_ID):
        """
        метод получения сформированного message - списка сообщений с одним словарём-сообщением
        :param template: int, id шаблона сообщения:
        :param device: int, id канала доставки
        :return: список словарей с одним словарём с ключами message_template_id и device_classification_id
        """
        return [{"message_template_id": template,
                 "device_classification_id": device}]
